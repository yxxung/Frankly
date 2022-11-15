package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.LikeDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface LikeMapper {

    public void createLike(LikeDTO likeDTO) throws Exception;

    List<LikeDTO> readLike(int userID) throws Exception;

    public void deleteLike(LikeDTO likeDTO) throws Exception;

    public void countLike(int boardID) throws Exception ;

}
