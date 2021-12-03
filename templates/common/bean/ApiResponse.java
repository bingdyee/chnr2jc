package ${project.base_pkg}.common.bean;

import ${project.base_pkg}.common.bean.status.StatusCode;
import ${project.base_pkg}.common.bean.status.StatusInfo;

import java.io.Serializable;

/**
 * 接口返回数据封装
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public class ApiResponse<E> implements Serializable {

    private static final long serialVersionUID = 2783079280657737974L;

    private String code;
    private String message;
    private E data;
    private String redirectUri;

    public ApiResponse() {
        this(StatusCode.OK);
    }

    public ApiResponse(StatusInfo status, E data) {
        this(status.getCode(), status.getDesc(), data);
    }

    public ApiResponse(StatusInfo status) {
        this(status, null);
    }

    public ApiResponse(String code, String message, E data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public boolean getSuccess() {
        return StatusCode.OK.getCode().equals(code);
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public E getData() {
        return data;
    }

    public void setData(E data) {
        this.data = data;
    }

    public String getRedirectUri() {
        return redirectUri;
    }

    public void setRedirectUri(String redirectUri) {
        this.redirectUri = redirectUri;
    }

    public static <E> ApiResponse<E> ok() {
        return new ApiResponse<>();
    }

    public static <E> ApiResponse<E> ok(E data) {
        return new ApiResponse<>(StatusCode.OK, data);
    }

    public static <E> ApiResponse<E> failed(String message) {
        return new ApiResponse<>(StatusCode.INTERNAL_SERVER_ERROR.getCode(), message, null);
    }

    public static <E> ApiResponse<E> of(StatusInfo statusInfo) {
        return new ApiResponse<>(statusInfo);
    }

    public static <E> ApiResponse<E> of(StatusInfo statusInfo, E data) {
        return new ApiResponse<>(statusInfo, data);
    }

    public static <E> ApiResponse<E> of(String code, String message) {
        return new ApiResponse<>(code, message, null);
    }

}
