package com.frankly.restapi.config;

import lombok.Builder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@Configuration
@EnableSwagger2
public class SwaggerConfig extends WebMvcConfigurerAdapter {

//

    private ApiInfo apiInfo(){
        return new ApiInfoBuilder()
                .title("Frankly Api doc")
                .description("병호찡을 위한 API 문서입니다. postman 대체")
                .build();

    }

    private ApiInfo regionApiInfo(){
        return new ApiInfoBuilder()
                .title("지역별 국회의원")
                .description("지역번호는 전화번호 기준\n\n" +
                        "서울" +
                        " 02" +
                        " 부산" +
                        " 51" +
                        " 대구" +
                        " 53" +
                        " 인천" +
                        " 32" +
                        " 광주" +
                        " 62\n" +
                        " 대전" +
                        " 42" +
                        " 울산" +
                        " 52" +
                        " 세종" +
                        " 44" +
                        " 경기" +
                        " 31" +
                        " 강원" +
                        " 33\n" +
                        " 충북" +
                        " 43" +
                        " 충남" +
                        " 41" +
                        " 전북" +
                        " 63" +
                        " 전남" +
                        " 61" +
                        " 경북" +
                        " 54\n" +
                        " 경남" +
                        " 55" +
                        " 제주" +
                        " 64" )
                .build();
    }

    @Bean
    public Docket memberApi(){
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("국회의원")
                .apiInfo(this.apiInfo())
                .select()
                .apis(RequestHandlerSelectors.
                        basePackage("com.frankly.restapi.controller"))
                .paths(PathSelectors.ant("/api/infos/**")).build();

    }

    @Bean
    public Docket regionApi(){
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("지역별 국회의원")
                .apiInfo(this.regionApiInfo())
                .select()
                .apis(RequestHandlerSelectors.
                        basePackage("com.frankly.restapi.controller"))
                .paths(PathSelectors.ant("/api/regions/**")).build();

    }

    @Bean
    public Docket userApi(){
        return new Docket(DocumentationType.SWAGGER_2)
                .groupName("유저")
                .apiInfo(this.apiInfo())
                .select()
                .apis(RequestHandlerSelectors.
                        basePackage("com.frankly.restapi.controller"))
                .paths(PathSelectors.ant("/api/users/**")).build();

    }

}
