package com.forhome.zhijia.checkoutlog.service.ao.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.forhome.zhijia.checkoutlog.service.ao.CheckOutLogAoService;
import com.forhome.zhijia.checkoutlog.service.bo.CheckOutLogService;



/**
 *  CheckOutLog Api
 *
 * @author devuser
 * @date 2019-07-23
 */
@Service
public class CheckOutLogAoServiceImpl implements CheckOutLogAoService {

    @Autowired
    private CheckOutLogService checkOutLogService;


}
