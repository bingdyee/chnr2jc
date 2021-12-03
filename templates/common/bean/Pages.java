package ${project.base_pkg}.common.bean;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * 分页包装
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public class Pages<E> implements Iterable<E>{

   private final Long totalElements;

    private final Long pageNo;

    private final Long pageSize;

    private final List<E> content;

    public Pages(List<E> content, long size, long number, long total) {
        this.totalElements = total;
        this.content = content == null ? new ArrayList<>() : content;
        this.pageSize = size;
        this.pageNo = number;
    }

    public static<E> Pages<E> of(List<E> content, long size, long number, long total) {
        return new Pages<>(content, size, number, total);
    }

    public Long getTotalElements() {
        return this.totalElements;
    }

    public Long getPageNo() {
        return this.pageNo;
    }

    public Long getPageSize() {
        return this.pageSize;
    }

    public List<E> getContent() {
        return this.content;
    }

    public Long getTotalPages() {
        return this.pageSize == 0 ? 1 : (long) Math.ceil((double) this.totalElements / (double) this.pageSize);
    }

    @Override
    public Iterator<E> iterator() {
        return this.content.iterator();
    }

}
