package com.frankly.restapi.service;

import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

//DDB에서 UserDetail 받아오는 Service

//로직 처리 : @Service (서비스 레이어, 내부에서 자바 로직을 처리함)
@Service
@RequiredArgsConstructor
public class JwtUserDetailsService implements UserDetailsService {

    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
        /**
         * password는
         * https://www.javainuse.com/onlineBcrypt 에서 user_pw를 Bcrypt화할 수 있습니다.
         * 우선 임시조치
         */
        if ("user_id".equals(userName)) {
            return new User("user_id", "$2a$10$jCvWm3NXDRFs/EfuI4h4.u0ZxNocv.ZkgEy6qbjVXrfQ5.KzLfhAe",
                    new ArrayList<>());
        }else{
                throw new UsernameNotFoundException("유저 이름을 찾을 수 없습니다. 유저이름 : " + userName);
        }


    }
}
