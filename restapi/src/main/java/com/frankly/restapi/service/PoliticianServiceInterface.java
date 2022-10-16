package com.frankly.restapi.service;

import com.frankly.restapi.domain.PoliticianDTO;

import java.util.List;

public interface PoliticianServiceInterface {

    public PoliticianDTO createPolitician(PoliticianDTO politicianDTO) throws Exception;

    public PoliticianDTO getPoliticianById(int politicianID) throws Exception;

    public List<PoliticianDTO> getPoliticianByName(String politicianName) throws Exception;

    public PoliticianDTO updatePolitician(int politicianID) throws Exception;

    public PoliticianDTO deletePolitician(int politicianID) throws Exception;

    public List<PoliticianDTO> politicianList() throws Exception;

    public List<PoliticianDTO> searchPolitician(String searchName) throws Exception;

}
