package com.frankly.restapi.domain;

import lombok.Data;

import java.io.Serializable;

//커스터마이징

@Data
public class JwtResponse implements Serializable {

    private static final long serialVersionUID = -8091879091924046844L;
    private final String jwttoken;
    private final String userEmail;
    private final String auth;

    public JwtResponse(String jwttoken, String userEmail, String auth) {

        this.jwttoken = jwttoken;
        this.userEmail = userEmail;
        this.auth = auth;
    }

    public String getToken() {
        return this.jwttoken;
    }


}
