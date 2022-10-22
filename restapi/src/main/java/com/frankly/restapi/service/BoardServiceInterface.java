package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;

import java.util.List;

public interface BoardServiceInterface {

    public void createBoard(BoardDTO boardDTO) throws Exception;

    public void updateBoard(BoardDTO boardDTO, int boardID) throws Exception;

    public void deleteBoard(BoardDTO boardDTO) throws Exception;

    public BoardDTO readBoard(int boardID) throws Exception;

    public List<BoardDTO> getBoardList(String region) throws  Exception;

    public List<BoardDTO> searchBoard(String region, String searchType, String keyword) throws Exception;

    // 게시물 총 갯수 + 검색 적용
    public int searchCount(String searchType, String keyword) throws Exception;
        //public List<BoardDTO> pageNumberBoardList(Long pageNumber) throws Exception;


}
