package com.frankly.restapi.service;

import com.frankly.restapi.domain.RegionNumberDTO;
import com.frankly.restapi.mapper.RegionNumberMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class RegionNumberService implements RegionNumberServiceInterface {

    private final RegionNumberMapper mapper;

    @Override
    public List<RegionNumberDTO> getMemeberListByRegion(Integer regionNumber) throws Exception {
        log.info("getMemeberListByRegion : " + regionNumber);
        return mapper.getMemberListByRegionNumber(regionNumber);
    }

}
