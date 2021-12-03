package ${project.base_pkg}.common.exception;

import ${project.base_pkg}.common.bean.status.StatusCode;
import ${project.base_pkg}.common.bean.status.StatusInfo;

/**
 * 异常
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public class AbstractWebException extends RuntimeException {

    private static final long serialVersionUID = -1667182340300670050L;

    protected String errorCode;

    public AbstractWebException(String message) {
        this(StatusCode.INTERNAL_SERVER_ERROR.as(message));
    }

    public AbstractWebException(StatusInfo errorStatus) {
        this(errorStatus.getCode(), errorStatus.getDesc());
    }

    public AbstractWebException(String errorCode, String errorDesc) {
        super(errorDesc);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }

}