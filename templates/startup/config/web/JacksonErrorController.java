package ${project.base_pkg}.config.web;


import ${project.base_pkg}.common.bean.ApiResponse;
import ${project.base_pkg}.common.bean.status.StatusCode;
import io.swagger.v3.oas.annotations.Hidden;
import org.springframework.boot.autoconfigure.web.servlet.error.AbstractErrorController;
import org.springframework.boot.web.servlet.error.ErrorAttributes;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


/**
 * 空白页处理
 *
 * @author ${project.author}
 * @since ${project.since}
 */
@Hidden
@RestController
@RequestMapping("${"${server.error.path:/error}"}")
public class JacksonErrorController extends AbstractErrorController {

    public JacksonErrorController(ErrorAttributes errorAttributes) {
        super(errorAttributes);
    }

    @GetMapping
    public ApiResponse<String> error() {
        return ApiResponse.of(StatusCode.INVALID_REQUEST);
    }

    @Override
    public String getErrorPath() {
        return null;
    }

}