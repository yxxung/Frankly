package com.frankly.restapi.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class HomeController {
    @GetMapping("/")
    public String getHome(){
        return "home";
    }

    //카카오톡 네이버 로그인..

    //회원가입으로
    @RequestMapping(value="/api/users/signup", method = RequestMethod.GET)
    public String getSignup(){
        return "registerUser";
    }

    //일반로그인으로
    @RequestMapping(value="/api/users/signin", method = RequestMethod.GET)
    public String getSignin(){
        return "loginUser";
    }

}
