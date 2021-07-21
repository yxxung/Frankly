package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.mapper.BoardMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class BoardService implements BoardServiceInterface {

    private final BoardMapper boardMapper;

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
