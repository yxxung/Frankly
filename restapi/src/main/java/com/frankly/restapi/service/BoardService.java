package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.mapper.BoardMapper;

import java.util.List;

public class BoardService implements BoardServiceInterface {

    BoardMapper boardMapper;

    @Override
    public void createBoard(BoardDTO boardDTO) throws Exception {
        boardMapper.createBoard(boardDTO);
    }

    @Override
    public void updateBoard(BoardDTO boardDTO) throws Exception {
    }

    @Override
    public void deleteBoard(BoardDTO boardDTO) throws Exception {

    }

    @Override
    public BoardDTO readBoard(Long id) throws Exception {
        return null;
    }

    @Override
    public List<BoardDTO> allBoardList() throws Exception {
        return null;
    }

    @Override
    public List<BoardDTO> pageNumberBoardList(Long pageNumber) throws Exception {
        return null;
    }
}
