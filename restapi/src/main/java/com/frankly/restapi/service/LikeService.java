package com.frankly.restapi.service;

import com.frankly.restapi.domain.LikeDTO;
import com.frankly.restapi.mapper.LikeMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
@Slf4j
@RequiredArgsConstructor
public class LikeService implements LikeServiceInterface{

    private final LikeMapper likeMapper;

    @Override
    public void createLike(LikeDTO likeDTO) throws Exception {
        likeMapper.createLike(likeDTO);
    }

    @Override
    public List<LikeDTO> readLike(int userID) throws Exception {
        return likeMapper.readLike(userID);
    }

    @Override
    public void deleteLike(LikeDTO likeDTO) throws Exception {
        likeMapper.deleteLike(likeDTO);
    }

    @Override
    public void countLike(int boardID) throws Exception {
        likeMapper.countLike(boardID);
    }


}
