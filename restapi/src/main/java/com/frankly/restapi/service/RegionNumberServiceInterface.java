package com.frankly.restapi.service;

import com.frankly.restapi.domain.RegionNumberDTO;

import java.util.List;

public interface RegionNumberServiceInterface {

    public List<RegionNumberDTO> getMemeberListByRegion(Integer regionID) throws Exception;

}
