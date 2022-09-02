package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.BoardDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface BoardMapper {

    public void createBoard(BoardDTO boardDTO) throws Exception;

    public void updateBoard(BoardDTO boardDTO) throws Exception;

    public void deleteBoard(BoardDTO boardDTO) throws Exception;

    public BoardDTO readBoard(int region, int boardID)throws Exception;

    public List<BoardDTO> allBoardList() throws  Exception;

    //public List<BoardDTO> pageNumberBoardList(Long pageNumber) throws Exception;



}
