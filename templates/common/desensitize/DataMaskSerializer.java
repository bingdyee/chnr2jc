package ${project.base_pkg}.common.desensitize;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.BeanProperty;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;
import com.fasterxml.jackson.databind.ser.ContextualSerializer;
import ${project.base_pkg}.common.utils.StringUtils;

import java.io.IOException;
import java.util.Objects;

/**
 * 数据脱敏
 *
 * @author Bing D. Yee
 * @since 2021/08/21
 */
public class DataMaskSerializer extends JsonSerializer<String> implements ContextualSerializer {

    private final MaskType maskType;

    public DataMaskSerializer() {
        this.maskType = MaskType.NONE;
    }

    public DataMaskSerializer(MaskType maskType) {
        this.maskType = maskType;
    }

    @Override
    public void serialize(String value, JsonGenerator gen, SerializerProvider serializers) throws IOException {
        if (StringUtils.isBlank(value)) {
            gen.writeString("");
            return;
        }
        switch (maskType) {
            case MOBILE:
                gen.writeString(DataMasker.maskPhone(value));
                break;
            case ID_CARD:
                gen.writeString(DataMasker.maskIdCard(value));
                break;
            case EMAIL:
                gen.writeString(DataMasker.maskEmail(value));
                break;
            case ADDRESS:
                gen.writeString(DataMasker.mask(value, 3, 3, DataMasker.MASKER));
                break;
            default:
                gen.writeString("********");
                break;
        }
    }

    @Override
    public JsonSerializer<?> createContextual(SerializerProvider prov, BeanProperty property) throws JsonMappingException {
        if (property == null) {
            return prov.findNullValueSerializer(null);
        }
        if (Objects.equals(property.getType().getRawClass(), String.class)) {
            SensitiveField annotation = property.getAnnotation(SensitiveField.class);
            if (annotation == null) {
                annotation = property.getContextAnnotation(SensitiveField.class);
            }
            if (annotation != null) {
                return new DataMaskSerializer(annotation.value());
            }
        }
        return prov.findValueSerializer(property.getType(), property);
    }

}
