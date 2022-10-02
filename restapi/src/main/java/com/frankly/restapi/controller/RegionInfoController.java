package com.frankly.restapi.controller;

import com.frankly.restapi.domain.RegionNumberDTO;
import com.frankly.restapi.service.RegionNumberService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/regions")
@RequiredArgsConstructor
public class RegionInfoController {

    private final RegionNumberService regionNumberService;

    @GetMapping("/{regionNumber}")
    public ResponseEntity<List<RegionNumberDTO>> getMemberListByRegionNumber(
            @PathVariable("regionID")Integer regionID) throws Exception {

        return new ResponseEntity<>(
                regionNumberService.getMemeberListByRegion(regionID)
                , HttpStatus.OK);

    }
}
