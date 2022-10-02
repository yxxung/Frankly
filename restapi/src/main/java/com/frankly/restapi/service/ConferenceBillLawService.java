package com.frankly.restapi.service;

import com.frankly.restapi.domain.ConferenceBillLawDTO;
import com.frankly.restapi.mapper.ConferenceBillLawMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class ConferenceBillLawService implements ConferenceBillLawServiceInterface{

    private final ConferenceBillLawMapper conferenceBillLawMapper;

    @Override
    public List<ConferenceBillLawDTO> readConferenceBillLaw(int politicianID) throws Exception {
        return conferenceBillLawMapper.readConferenceBillLaw(politicianID);
    }

    @Override
    public void updateConferenceBillLaw(int billID) throws Exception {
        conferenceBillLawMapper.updateConferenceBillLaw(billID);
    }

    @Override
    public void deleteConferenceBillLaw(int billID) throws Exception {
        conferenceBillLawMapper.deleteConferenceBillLaw(billID);
    }

}
