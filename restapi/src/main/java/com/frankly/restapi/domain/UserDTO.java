package com.frankly.restapi.domain;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;
import java.util.HashSet;
import java.util.Set;


@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UserDTO implements UserDetails {

    //Id와, EMail 모두 unique
    private int userID;
    private String email;
    private String contact;

    private String name;
    private String password;
    private String district;
    private String sex;
    private String userAuth;
    private Set<GrantedAuthority> authorities;


    /**
     * 빌더 패턴 생성
     *
     * 예시 :
     * Member customer = Member.build()
     *    .name("홍길동")
     *     .age(30)
     *     .build()
     *
     */

    @Builder
    public UserDTO(String email, String name, String password,
                   String district, String sex, String userAuth, String contact){
        this.email = email;
        this.name = name;
        this.password = password;
        this.district = district;
        this.sex = sex;
        this.userAuth = userAuth;
        this.contact = contact;
    }

    // 해당 유저의 권한을 컬렉션 형태로 반환
    //GrantedAuthority 구현
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        Set<GrantedAuthority> userAuths = new HashSet<>();
        for(String auth : this.userAuth.split(",")){
            userAuths.add(new SimpleGrantedAuthority(auth));
        }
        return userAuths;
    }

    @Override
    public String getUsername() {
        return name;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword(){
        return password;
    }


    //계정이 만료되었는가?
    @Override
    public boolean isAccountNonExpired() {
        return true; // 만료되지 않음. (원래 false이나, 우리에게 맞게 변)
    }

    //계정이 잠겼냐?
    @Override
    public boolean isAccountNonLocked() {
        return true; // 잠기지 않음.
    }

    //패스워드가 만료되었는가?
    @Override
    public boolean isCredentialsNonExpired() {
        return true; // 만료되지 않음.
    }

    //계정 사용가능한가?
    @Override
    public boolean isEnabled() {
        return true; // 계정 사용가능
    }
}