package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.ConferenceBillLawDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface ConferenceBillLawMapper {

    public List<ConferenceBillLawDTO> readConferenceBillLaw(int politicianID) throws Exception;

    public void updateConferenceBillLaw(int billID) throws Exception;

    public void deleteConferenceBillLaw(int billID) throws Exception;

}