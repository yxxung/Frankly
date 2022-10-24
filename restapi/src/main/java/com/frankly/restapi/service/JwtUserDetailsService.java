package com.frankly.restapi.service;

import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.mapper.UserMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;


//DB에서 UserDetail 받아오는 Service
//authenticationManager에서 사용.

//로직 처리 : @Service (서비스 레이어, 내부에서 자바 로직을 처리함)
@Service
@RequiredArgsConstructor
@Slf4j
public class JwtUserDetailsService implements UserDetailsService {

    private final UserMapper userMapper;

    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {

        try {
            UserDTO user = getUserByEmail(email);
            log.info("login User : " + email);
            if (user.getEmail().equals(email)) {

                return new User(user.getEmail(),
                            user.getPassword(),
                            user.getAuthorities());
            } else{
                throw new UsernameNotFoundException("유저 이름을 찾을 수 없습니다. 유저이름 : " + email);
            }
        } catch (Exception e){
            throw new UsernameNotFoundException("유저 이름을 찾을 수 없습니다. 유저이름 : " + email);
        }

    }

    public UserDTO getUserByEmail(String email) throws Exception {
        return userMapper.getUserByEmail(email);
    }
}
