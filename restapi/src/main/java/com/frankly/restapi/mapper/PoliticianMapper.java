package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.PoliticianDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

/**
 * @author 최제현
 * @date 2021/06/25
 * mybatis 프레임워크
 * Member mapper interface
 */

@Mapper
public interface PoliticianMapper {

    public PoliticianDTO createPolitician(PoliticianDTO politicianDTO) throws Exception;

    public PoliticianDTO readPolitician(int politicianID) throws Exception;

    public PoliticianDTO updatePolitician(int politicianID) throws Exception;

    public PoliticianDTO deletePolitician(int politicianID)throws Exception;

    public List<PoliticianDTO> politicianList() throws Exception;

}
