package com.frankly.restapi.service;

import com.frankly.restapi.domain.VoteDTO;
import com.frankly.restapi.mapper.VoteMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class VoteService implements VoteServiceInterface{

    private final VoteMapper voteMapper;

    @Override
    public List<VoteDTO> readVote(int politicianID) throws Exception {
        return voteMapper.readVote(politicianID);
    }

    @Override
    public List<VoteDTO> countVote(int politicianID) throws Exception {
        return voteMapper.countVote(politicianID);
    }

    @Override
    public void updateVote(int voteID) throws Exception {
        voteMapper.updateVote(voteID);
    }

    @Override
    public void deleteVote(int voteID) throws Exception {
        voteMapper.deleteVote(voteID);
    }
}
