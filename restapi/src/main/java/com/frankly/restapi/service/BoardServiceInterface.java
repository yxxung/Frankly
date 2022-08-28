package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;

import java.util.List;

public interface BoardServiceInterface {

    public void createBoard(BoardDTO boardDTO) throws Exception;

    public void updateBoard(BoardDTO boardDTO, int region, int boardID) throws Exception;

    public void deleteBoard(BoardDTO boardDTO) throws Exception;

    public BoardDTO readBoard(int region, int boardID)throws Exception;

    public List<BoardDTO> allBoardList() throws  Exception;

    //public List<BoardDTO> pageNumberBoardList(Long pageNumber) throws Exception;


}
