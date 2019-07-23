package com.forhome.zhijia.checkoutlog.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.forhome.zhijia.checkoutlog.mapper.AccountMapper;
import com.forhome.zhijia.checkoutlog.service.AccountService;


/**
 *  CheckOutLog Mapper
 *
 * @author devuser
 * @date 2019-07-23
 */
@Service
public class CheckOutLogServiceImpl implements CheckOutLogService {

    @Autowired
    private CheckOutLogMapper checkOutLogMapper;

}
