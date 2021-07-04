package com.frankly.restapi.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.*;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
public class UserAuthProvider implements AuthenticationProvider {

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private JwtUserDetailsService jwtUserDetailsService;


    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {

        if(authentication == null){
            throw new InternalAuthenticationServiceException("auth is null");
        }

        String userName = authentication.getName();
        String password = authentication.getCredentials().toString();
        UserDetails DBUser = jwtUserDetailsService.loadUserByUsername(userName);

        if(DBUser == null )
            throw new InternalAuthenticationServiceException("UserDetails return null");

        if(!DBUser.isAccountNonLocked())
            throw new LockedException("account is locked");

        if(!DBUser.isEnabled())
            throw new DisabledException("account is disabled");

        if(!DBUser.isAccountNonExpired())
            throw new AccountExpiredException("account is expired");

        // 실질적인 인증.
        if(!passwordEncoder.matches(password, DBUser.getPassword()))
            throw new BadCredentialsException("password does not match");

        if(!DBUser.isCredentialsNonExpired())
            throw new CredentialsExpiredException("account credentials have expired");

        UsernamePasswordAuthenticationToken result = new UsernamePasswordAuthenticationToken(DBUser, null ,DBUser.getAuthorities());
        result.setDetails(authentication.getDetails());

        return result;


    }

    /**
     * 인증하기 전후의 토큰
     *
     * //인증 전의 토큰 public UsernamePasswordAuthenticationToken(Object principal, Object credentials) {
     * super((Collection)null);
     * this.principal = principal;
     * this.credentials = credentials;
     * this.setAuthenticated(false); }
     *
     * //인증 후의 토큰 public UsernamePasswordAuthenticationToken(Object principal, Object credentials, Collection<? extends GrantedAuthority> authorities) {
     * super(authorities);
     * this.principal = principal;
     * this.credentials = credentials;//인증 후에는 비밀번호를 웬만하면 제거하기 때문에 null로 들어온다.
     * super.setAuthenticated(true);//인증 완료했다고 넣어주는 게 보인다. }
     *
     * 출처: https://jeong-pro.tistory.com/205 [기본기를 쌓는 정아마추어 코딩블로그]
     *
     */
    @Override
    public boolean supports(Class<?> aClass) {
        return UsernamePasswordAuthenticationToken.class.isAssignableFrom(aClass);
    }
}
