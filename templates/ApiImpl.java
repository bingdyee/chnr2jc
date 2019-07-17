package ${package}.${module}.api.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ${package}.${module}.api.${className}Api;
import ${package}.${module}.service.${className}Service;


/**
 *  ${comments} Api
 *
 * @author ${author}
 * @date ${datetime}
 */
@Service
public class ${className}ApiImpl implements ${className}Api {

    @Autowired
    private ${className}Service ${varName}Service;


}