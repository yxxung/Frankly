package com.frankly.restapi.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("http://220.122.5.95:3000" , "http://localhost:3000", "http://localhost:8081")
//                .allowedOrigins("*")
                .allowedMethods("PUT", "DELETE", "OPTION")
                .allowedHeaders("Authorization")
                .exposedHeaders("Authorization")
                .allowCredentials(false).maxAge(3600);
    }
}
