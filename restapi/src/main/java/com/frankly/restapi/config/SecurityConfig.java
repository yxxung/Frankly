package com.frankly.restapi.config;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.CorsUtils;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

@Slf4j
//이 어노테이션은?
//@EnableWebSecurity(debug = true)
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {


    @Autowired
    private JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;

    @Autowired
    private UserDetailsService jwtUserDetailsService;

    @Autowired
    private JwtRequestFilter jwtRequestFilter;

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception{
        /**
         * Authenticationmanager가 어디서 load되는지 알 수 있도록 설정\
         * jwtUserDetailsService에서 사용하겠다!
         * .credentials 일치하는 유저
         * .BcryptPasswordEncoder 사용.(암호화)
         */

        auth.userDetailsService(jwtUserDetailsService).passwordEncoder(passwordEncoder());

    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    @Override
    public AuthenticationManager authenticationManagerBean() throws Exception{
        return super.authenticationManagerBean();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // 한 유저 테스트기 때문에 CSRF 미적용 추후 수정.
        http.csrf().disable() //security에서 기본으로 생성하는 login페이지 사용 안 함
                //특정 request에는 auth 필요없음.
                //배포용 설정
                .authorizeRequests().antMatchers("/api/auth/**", "/api/users/signup", "/api/users/login", "/api/infos/**", "/api/boards/**","/api/politician/**",
                        "/api/billLaw/**", "/api/schedule/**", "/api/attendance/**", "/api/vote/**", "/api/news/**", "/api/property/**", "/api/replys/**").permitAll()

                .antMatchers("/").hasRole("USER")
                .antMatchers("/admin").hasRole("ADMIN")

                //개발용 설정
                                .authorizeRequests().antMatchers("/api/**", "/api/users/user", "/api/auth/signin", "/**").permitAll()
                //cors 예외처리
                .requestMatchers(CorsUtils::isPreFlightRequest).permitAll()
                //다른 모든 request에는 auth작업 해주어야함.
                .anyRequest().authenticated().and()
                //restful api 는 stateless해야하므로, statless로 바꾸어줌. 유저 state 저장안함.
                .exceptionHandling().authenticationEntryPoint(jwtAuthenticationEntryPoint).and()
                .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS);

        //모든 request를 validate 하기위해 필터 추가.
        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource(){
        CorsConfiguration configuration = new CorsConfiguration();


        configuration.addAllowedOrigin("http:/frankly.kro.kr:8081");
//        configuration.addAllowedOrigin("http://220.122.5.95:3000");
        configuration.addAllowedMethod("*");
        configuration.addAllowedHeader("*");
        configuration.setAllowCredentials(true);
        configuration.setMaxAge(3600L);
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", configuration);
        return source;

    }
}
