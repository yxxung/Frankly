package com.frankly.restapi.domain;

import lombok.Data;

import java.io.Serializable;

//커스터마이징

@Data
public class JwtResponse implements Serializable {

    private static final long serialVersionUID = -8091879091924046844L;
    private final String token;
    private final String email;
    private final String userAuth;

    private final int userID;



    public JwtResponse(String token, String email, String userAuth, int userID) {

        this.token = token;
        this.email = email;
        this.userAuth = userAuth;
        this.userID = userID;
    }

    public String getToken() {
        return this.token;
    }


}
