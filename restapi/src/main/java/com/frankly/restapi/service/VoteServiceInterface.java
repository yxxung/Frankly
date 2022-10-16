package com.frankly.restapi.service;

import com.frankly.restapi.domain.VoteDTO;

import java.util.List;

public interface VoteServiceInterface {

    List<VoteDTO> readVote(int politicianID) throws Exception;

    List<VoteDTO> countVote(int politicianID) throws Exception;

    void updateVote(int voteID) throws Exception;

    void deleteVote(int voteID) throws Exception;
}
