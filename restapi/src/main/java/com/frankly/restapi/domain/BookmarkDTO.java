package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data
@NoArgsConstructor
public class BookmarkDTO {

    private int bookmarkID;

    private int politicianID;

    private int userID;


    //politicianDTO
    //이름
    private String politicianName;
    //한자명
    private String hanName;
    //영문명칭
    private String engName;
    //음/양력
    private String lunar;
    //생년월일
    private Date birthday;
    //정당번호
    private int partyID;
    //정당명
    private String partyName;
    //선거구
    private int regionID;//district;
    //재선횟수
    private int selectNumber;
    //당선
    private String selectInfo;
    //성별
    private String sex;
    //전화번호
    private String contact;
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
    //사진 주소
    private String politicianImageURL;
    //선거구
    private String regionName;
}
