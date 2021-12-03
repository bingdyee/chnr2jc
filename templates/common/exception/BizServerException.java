package ${project.base_pkg}.common.exception;

import ${project.base_pkg}.common.bean.status.StatusInfo;

/**
 *  业务异常
 *
 * @author Bing D. Yee
 * @since 2021/11/10
 */
public class BizServerException extends AbstractWebException {

    private static final long serialVersionUID = -2167602128463077079L;

    public BizServerException(String message) {
        super(message);
    }

    public BizServerException(StatusInfo errorStatus) {
        super(errorStatus);
    }

    public BizServerException(String errorCode, String errorDesc) {
        super(errorCode, errorDesc);
    }

}
