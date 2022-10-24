package com.frankly.restapi.domain;

import lombok.Data;

import java.io.Serializable;

//커스터마이징

@Data
public class JwtResponse implements Serializable {

    private static final long serialVersionUID = -8091879091924046844L;
    private final String jwttoken;
    private final String email;
    private final String userAuth;



    public JwtResponse(String jwttoken, String email, String userAuth) {

        this.jwttoken = jwttoken;
        this.email = email;
        this.userAuth = userAuth;
    }

    public String getToken() {
        return this.jwttoken;
    }


}
