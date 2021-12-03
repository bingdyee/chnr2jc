package ${project.base_pkg}.common.bean.status;

/**
 * 默认状态码
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public enum StatusCode implements StatusInfo {
    /** 正常 */
    OK("00000", "OK"),
    /** 客户端错误 */
    INVALID_REQUEST("A0400", "客户端请求错误"),
    /** 请求资源不存在 */
    NOT_FOUND("A0404", "请求资源不存在"),
    /** 权限不足 */
    FORBIDDEN("A0403", "权限不足"),
    /** 系统执行出错 */
    INTERNAL_SERVER_ERROR("B0001", "系统执行出错"),
    /** 调用第三方服务出错 */
    SERVICE_UNAVAILABLE("C0001", "调用第三方服务出错");

    private final String code;
    private final String desc;

    StatusCode(String code, String desc) {
        this.code = code;
        this.desc = desc;
    }

    @Override
    public String getCode() {
        return this.code;
    }

    @Override
    public String getDesc() {
        return this.desc;
    }

}
