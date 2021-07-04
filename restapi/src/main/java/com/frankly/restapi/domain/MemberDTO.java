package com.frankly.restapi.domain;

import lombok.Data;


/**
 * @author 최제현
 * @date 2021/06/24
 * 국회의원 DTO
 * 추후 나눌 필요가 있어보임.
 */
@Data
public class MemberDTO {

    //id
    private Long id;
    //이름
    private String name;
    //한자명
    private String hanName;
    //영문명칭
    private String engName;
    //음/양력
    private String lunar;
    //생년월일
    private String birthday;
    //정당명
    private String party;
    //선서구
    private String district;
    //재선횟수
    private String selectNumber;
    //당선
    private String selectInfo;
    //성별
    private String sex;
    //전화번호
    private String contact;
    //사무실 호실
    private String office;
    //이메일
    private String email;
    //홈페이지
    private String homepage;
    //보자관
    private String aide;
    //비서관
    private String secretary;
    //비서
    private String personalAssistant;


    //나머지 Lombok으로 자동생성.

}
