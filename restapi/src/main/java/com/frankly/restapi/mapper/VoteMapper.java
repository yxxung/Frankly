package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.VoteDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface VoteMapper {

    public List<VoteDTO> readVote(int politicianID) throws Exception;

    public List<VoteDTO> countVote(int politicianID) throws Exception;

    public void updateVote(VoteDTO voteDTO) throws Exception;

    public void deleteVote(int voteID) throws Exception;

}