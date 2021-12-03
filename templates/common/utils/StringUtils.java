package ${project.base_pkg}.common.utils;

import java.util.Collection;
import java.util.StringJoiner;

/**
 * 字符串工具类
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public final class StringUtils {

    public static boolean isEmpty(final CharSequence cs) {
        return cs == null || cs.length() == 0;
    }

    public static boolean isNotEmpty(final CharSequence cs) {
        return !isEmpty(cs);
    }

    public static boolean isBlank(final CharSequence cs) {
        int strLen;
        if (cs == null || (strLen = cs.length()) == 0) {
            return true;
        }
        for (int i = 0; i < strLen; i++) {
            if (!Character.isWhitespace(cs.charAt(i))) {
                return false;
            }
        }
        return true;
    }

    public static boolean isNotBlank(final CharSequence cs) {
        return !isBlank(cs);
    }

    public static String trim(final String str) {
        return str == null ? null : str.trim();
    }

    public static String join(Collection<String> strings, String sep) {
        StringJoiner joiner = new StringJoiner(sep);
        strings.forEach(joiner::add);
        return joiner.toString();
    }

}
