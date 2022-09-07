package com.frankly.restapi.service;

import com.frankly.restapi.domain.PoliticianDTO;
import com.frankly.restapi.mapper.PoliticianMapper;
import lombok.RequiredArgsConstructor;
import lombok.ToString;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor
@Service
@Slf4j
@ToString
public class PoliticianService implements PoliticianServiceInterface {

    private final PoliticianMapper politicianMapper;

    @Override
    public PoliticianDTO createPolitician(PoliticianDTO politicianDTO) throws Exception {
        return politicianMapper.createPolitician(politicianDTO);
    }

    @Override
    public PoliticianDTO getPoliticianById(int politicianID) throws Exception {
        log.info("get PoliticianID:" + politicianID);
        return politicianMapper.readPolitician(politicianID);
    }

    @Override
    public PoliticianDTO updatePolitician(int politicianID) throws Exception {
        return politicianMapper.updatePolitician(politicianID);
    }

    @Override
    public PoliticianDTO deletePolitician(int politicianID) throws Exception {
        return politicianMapper.deletePolitician(politicianID);
    }

    @Override
    public List<PoliticianDTO> politicianList() throws Exception{
        log.info("getList");
        return politicianMapper.politicianList();
    }
}
