package com.frankly.restapi.service;

import com.frankly.restapi.domain.ConferenceBillLawDTO;

import java.util.List;

public interface ConferenceBillLawServiceInterface {

    List<ConferenceBillLawDTO> readConferenceBillLaw(int politicianID) throws Exception;

    void updateConferenceBillLaw(int billID) throws Exception;

    void deleteConferenceBillLaw(int billID) throws Exception;
}
