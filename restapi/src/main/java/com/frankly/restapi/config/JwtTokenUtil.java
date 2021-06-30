package com.frankly.restapi.config;


import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import java.io.Serializable;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;


/**
 * @author 최제현
 * @Date 2021/06/30
 *
 * JwtToken 사용위한 utils 클래스
 *
 * 참고 : https://www.javainuse.com/spring/boot-jwt
 */

// 개발자가 직접 작성한 class Bean으로 등록 (DI)
    @Slf4j
@Component
public class JwtTokenUtil implements Serializable {

    private static final long serialVersionUID = -2550185165626007488L;

    //토큰 시간을 짧게해서, 보안성 증가
    public static final long JWT_Token_VALIDITY =  5 * 60 * 60;

    @Value("${spring.jwt.secret}")
    private String secretKey;

    //token에서 username 획득

    public String getUsernameFromToken(String token){
        return getClaimFromToken(token, Claims::getSubject);
    }

    //token에서 만료 일자 획득
    public Date getExpireDateFromToken(String token){
        return getClaimFromToken(token, Claims::getExpiration);
    }

    public <Token> Token getClaimFromToken(String token, Function<Claims, Token> claimsResolver){
        final Claims claims = getAllClaimsFromToken(token);
        return claimsResolver.apply(claims);

    }

    // 토큰에서 정보를 찾기 위해선 비밀키가 필요.
    public Claims getAllClaimsFromToken(String token){
        return Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token).getBody();
    }

    //토큰 만료 확인
    //만료시 TRUE 리
    private Boolean isTokenExpired(String token){
        final Date expiration = getExpireDateFromToken(token);
        return expiration.before(new Date());
    }

    //토큰 발급
    public String generateToken(UserDetails userDetails){
        Map<String, Object> claims = new HashMap<>();
        return doGenerateTokens(claims, userDetails.getUsername());
    }

    /**
     * 토큰발급
     * 1. Issuer, Expiration, Subject, ID 같은 요구 정의
     * 2. HS512 알고리즘과 비밀키 사용으로 JWT sign
     * 3. According to JWS Compact Serialization(https://tools.ietf.org/html/draft-ietf-jose-json-web-signature-41#section-3.1)
     *   compaction of the JWT to a URL-safe string
     */

    private String doGenerateTokens(Map<String, Object> claims, String subject){
        return Jwts.builder().setClaims(claims).setSubject(subject).setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + JWT_Token_VALIDITY * 1000))
                .signWith(SignatureAlgorithm.HS512, secretKey).compact();

    }

    public Boolean validateToken(String token, UserDetails userDetails){
        final String username = getUsernameFromToken(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }




}
