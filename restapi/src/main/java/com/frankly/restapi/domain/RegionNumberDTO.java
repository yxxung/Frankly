package com.frankly.restapi.domain;

import lombok.Data;


/**
 * 지역번호 별 국회의원 DTO
 */

@Data
public class RegionNumberDTO {

    private int regionID;

    private String regionName;

}
