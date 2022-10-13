package com.frankly.restapi.controller;

import org.springframework.web.bind.annotation.GetMapping;

public class WebController {

    @GetMapping("/vue")
    public String vue() {
        return "vue/index";
    }
}
