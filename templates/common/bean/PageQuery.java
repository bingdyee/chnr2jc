package ${project.base_pkg}.common.bean;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

/**
 * 分页查询
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
@Getter
@Setter
@ToString
public class PageQuery {

    private Integer pageNo = 0;

    private Integer pageSize = 10;

}
