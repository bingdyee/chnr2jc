package ${project.base_pkg}.common.utils;

import net.sf.cglib.beans.BeanCopier;
import net.sf.cglib.core.Converter;

import java.io.*;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

/**
 * 对象转换
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public final class BeanConverter {

    private static final Map<String, BeanCopier> BEAN_COPIER_CACHE = new ConcurrentHashMap<>();

    public static void copyProperties(Object source, Object target) {
        BeanCopier copier = getBeanCopier(source.getClass(), target.getClass(), null);
        copier.copy(source, target, null);
    }

    public static <T, V> V convert(T source, Class<V> targetClass) {
        if (Objects.isNull(source) || Objects.isNull(targetClass)) {
            return null;
        }
        return copy(source, targetClass, null);
    }

    public static <T, V> V convert(T source, Class<V> targetClass, Converter converter) {
        if (Objects.isNull(source) || Objects.isNull(targetClass)) {
            return null;
        }
        return copy(source, targetClass, converter);
    }

    public static <T, V> List<V> convertList(List<T> sourceList, Class<V> targetClass) {
        if (sourceList == null || sourceList.isEmpty()) {
            return Collections.emptyList();
        }
        return sourceList.stream()
                .map(source -> convert(source, targetClass))
                .collect(Collectors.toList());
    }

    public static <T, V> List<V> convertList(List<T> sourceList, Class<V> targetClass, Converter converter) {
        if (sourceList == null || sourceList.isEmpty()) {
            return Collections.emptyList();
        }
        return sourceList.stream()
                .map(source -> convert(source, targetClass, converter))
                .collect(Collectors.toList());
    }

    private static <T, V> V copy(T source, Class<V> targetClass, Converter converter) {
        BeanCopier copier = getBeanCopier(source.getClass(), targetClass, converter);
        V target = null;
        try {
            target = targetClass.getDeclaredConstructor().newInstance();
            copier.copy(source, target, converter);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return target;
    }

    private static <T> BeanCopier getBeanCopier(Class<T> source, Class<?> target, Converter converter) {
        String beanKey = source.getName() + target.getName();
        BeanCopier copier = BEAN_COPIER_CACHE.get(beanKey);
        if (copier == null) {
            copier = BeanCopier.create(source, target, converter != null);
            BEAN_COPIER_CACHE.put(beanKey, copier);
        }
        return copier;
    }

    public static <T extends Serializable> T clone(T t) {
        try {
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(bos);
            oos.writeObject(t);
            ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
            ObjectInputStream ois = new ObjectInputStream(bis);
            return (T) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }

}
