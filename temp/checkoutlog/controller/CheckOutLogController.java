package com.forhome.zhijia.checkoutlog.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.forhome.zhijia.checkoutlog.service.ao.CheckOutLogAoService;

/**
 *  CheckOutLog Controller
 *
 * @author devuser
 * @date 2019-07-23
 */
@RestController
@RequestMapping("/api")
public class CheckOutLogController {

    @Autowired
    private CheckOutLogAoService checkOutLogAoService;

}
