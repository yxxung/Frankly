package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.RegionNumberDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;


/**
 * 지역별 국회의원 출력 서비스를 위한 mapper
 */
@Mapper
public interface RegionNumberMapper {

    public List<RegionNumberDTO> getMemberListByRegionNumber(Integer regionNumber) throws Exception;
}
