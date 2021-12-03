package ${project.base_pkg}.common.utils;

import java.util.Collection;

/**
 * 集合工具
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public final class CollectionUtils {

    public static boolean isEmpty(Collection<?> coll) {
        return (coll == null || coll.isEmpty());
    }

    public static boolean isNotEmpty(Collection<?> coll) {
        return !CollectionUtils.isEmpty(coll);
    }

}
