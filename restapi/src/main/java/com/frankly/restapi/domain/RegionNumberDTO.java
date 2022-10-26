package com.frankly.restapi.domain;

import lombok.Data;


/**
 * 지역번호 별 국회의원 DTO
 */

@Data
public class RegionNumberDTO {

    private Long regionID;

    private String regionName;


}
