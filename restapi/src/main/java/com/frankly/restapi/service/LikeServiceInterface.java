package com.frankly.restapi.service;

import com.frankly.restapi.domain.LikeDTO;

import java.util.List;

public interface LikeServiceInterface {

    public void createLike(LikeDTO likeDTO) throws Exception;

    List<LikeDTO> readLike(int userID) throws Exception;

    public void deleteLike(LikeDTO likeDTO) throws Exception ;

    public void countLike(int boardID) throws Exception ;

}
