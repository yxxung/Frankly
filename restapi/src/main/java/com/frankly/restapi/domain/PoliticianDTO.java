package com.frankly.restapi.domain;

import lombok.Builder;
import lombok.Data;

import java.util.Date;


/**
 * @author 최제현
 * @date 2021/06/24
 * 국회의원 DTO
 * 추후 나눌 필요가 있어보임.
 */
@Data
@Builder
public class PoliticianDTO {
    //id
    private int politicianID;
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

    @Builder
    public PoliticianDTO(int politicianID, String politicianName, String hanName, String engName, String lunar, Date birthday, int partyID,
                         String partyName, int regionID, int selectNumber, String selectInfo, String sex, String contact, String office,
                         String email, String homepage, String aide, String secretary, String personalAssistant) {
        this.politicianID = politicianID;
        this.politicianName = politicianName;
        this.hanName = hanName;
        this.engName = engName;
        this.lunar = lunar;
        this.birthday = birthday;
        this.partyID = partyID;
        this.partyName = partyName;
        this.regionID = regionID;
        this.selectNumber = selectNumber;
        this.selectInfo = selectInfo;
        this.sex = sex;
        this.contact = contact;
        this.office = office;
        this.email = email;
        this.homepage = homepage;
        this.aide = aide;
        this.secretary = secretary;
        this.personalAssistant = personalAssistant;
    }
    //나머지 Lombok으로 자동생성.

}
