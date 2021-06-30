package com.frankly.restapi.config;

import io.jsonwebtoken.ExpiredJwtException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Slf4j
@Component
public class JwtRequestFilter extends OncePerRequestFilter {

    @Autowired
    private JwtUserDetailsService jwtUserDetailsService;

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, FilterChain filterChain) throws ServletException, IOException {

        final String requestTokenHeader = httpServletRequest.getHeader("Authorization");

        String userName = null;
        String jwtToken = null;
        // JWT Token is in the form "Bearer token". Remove Bearer word and get
        // only the Token
        log.info(requestTokenHeader);
        if(requestTokenHeader != null && requestTokenHeader.startsWith("Bearer ")) {
            jwtToken = requestTokenHeader.substring(7);
            try{
                userName = jwtTokenUtil.getUsernameFromToken(jwtToken);
            }catch (IllegalArgumentException e){
                log.warn("JWT Token을 가져올 수 없습니다.");
            }catch (ExpiredJwtException e) {
                log.warn("만료된 토큰입니다.");
            }
        }else {
            log.warn("JWT Token이 Bearer로 시작하지 않습니다.");
        }

        if(userName != null && SecurityContextHolder.getContext().getAuthentication() == null){
            UserDetails userDetails = this.jwtUserDetailsService.loadUserByUsername(userName);

            //토큰이 valid하면, 수동으로 설정하도록 Spring Security set후 인증

            if(jwtTokenUtil.validateToken(jwtToken, userDetails)){
                UsernamePasswordAuthenticationToken usernamePasswordAuthenticationToken = new UsernamePasswordAuthenticationToken(
                        userDetails, null, userDetails.getAuthorities());
                usernamePasswordAuthenticationToken.setDetails(new WebAuthenticationDetailsSource()
                        .buildDetails(httpServletRequest));

                /**
                 * context 안에 auth 세팅 후에 현재 유저가 인증이 되었다고 특정함.
                 * 그러면, Spring Security Configuration 패스 성공함
                 */
                   SecurityContextHolder.getContext().setAuthentication(usernamePasswordAuthenticationToken);

            }
        }

        filterChain.doFilter(httpServletRequest, httpServletResponse);
    }
}
