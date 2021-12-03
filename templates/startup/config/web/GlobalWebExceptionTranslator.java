package ${project.base_pkg}.config.web;


import ${project.base_pkg}.common.bean.ApiResponse;
import ${project.base_pkg}.common.bean.status.StatusCode;
import ${project.base_pkg}.common.exception.AbstractWebException;
import ${project.base_pkg}.common.utils.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.support.DefaultMessageSourceResolvable;
import org.springframework.http.HttpStatus;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.validation.BindingResult;
import org.springframework.web.HttpMediaTypeNotSupportedException;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;
import org.springframework.web.servlet.NoHandlerFoundException;

import javax.validation.ConstraintViolationException;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * 全局异常处理处理
 *
 * @author ${project.author}
 * @since ${project.since}
 */
@RestControllerAdvice
@ResponseStatus(code = HttpStatus.OK)
public class GlobalWebExceptionTranslator {

    private static final Logger logger = LoggerFactory.getLogger(GlobalWebExceptionTranslator.class);

    @ExceptionHandler(NoHandlerFoundException.class)
    @ResponseStatus(code = HttpStatus.OK)
    public ApiResponse<String> handleError(NoHandlerFoundException e) {
        logger.error(StatusCode.NOT_FOUND.getDesc(), e);
        return ApiResponse.of(StatusCode.NOT_FOUND);
    }

    @ExceptionHandler({
            MethodArgumentNotValidException.class,
            ConstraintViolationException.class,
            HttpMessageNotReadableException.class,
            MissingServletRequestParameterException.class,
            MethodArgumentTypeMismatchException.class,
            HttpRequestMethodNotSupportedException.class,
            HttpMediaTypeNotSupportedException.class
    })
    @ResponseStatus(code = HttpStatus.OK)
    public ApiResponse<String> handleInvalidArgumentException(Exception e) {
        logger.error(StatusCode.INVALID_REQUEST.getDesc(), e);
        if (e instanceof MethodArgumentNotValidException) {
            BindingResult bindingResult = ((MethodArgumentNotValidException)e).getBindingResult();
            Set<String> errors = bindingResult
                    .getFieldErrors()
                    .stream()
                    .map(DefaultMessageSourceResolvable::getDefaultMessage)
                    .collect(Collectors.toSet());
            return ApiResponse.of(StatusCode.INVALID_REQUEST.getCode(), StringUtils.join(errors, ", "));
        }

        return ApiResponse.of(StatusCode.INVALID_REQUEST);
    }

    @ExceptionHandler(AbstractWebException.class)
    @ResponseStatus(code = HttpStatus.OK)
    public ApiResponse<String> handleException(AbstractWebException e) {
        logger.error(StatusCode.INTERNAL_SERVER_ERROR.getDesc(), e);
        return ApiResponse.of(e.getErrorCode(), e.getMessage());
    }

    @ExceptionHandler(Throwable.class)
    public ApiResponse<String> handleException(Exception e) {
        logger.error(StatusCode.INTERNAL_SERVER_ERROR.getDesc(), e);
        return ApiResponse.of(StatusCode.INTERNAL_SERVER_ERROR);
    }

}
