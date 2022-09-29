package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.mapper.BoardMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.stereotype.Service;

import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.*;

@Service
@Slf4j
@RequiredArgsConstructor
public class BoardService implements BoardServiceInterface {

    private final BoardMapper boardMapper;

    @Override
    public void createBoard(BoardDTO boardDTO) throws Exception {

        boardDTO.setMarked(0);
        boardMapper.createBoard(boardDTO);
    }

    @Override
    public void updateBoard(BoardDTO boardDTO, String region, int boardID) throws Exception {

        BoardDTO targetBoard = boardMapper.readBoard(boardID);
        if(targetBoard.getAuthor() == (boardDTO.getAuthor())){
            try{
                boardDTO.setBoardID(boardID);
                boardDTO.setRegion(region);
                boardMapper.updateBoard(boardDTO);
            }catch(SQLException e){
                System.out.println(e);
                e.printStackTrace();
            }

        }else{
            throw new Exception("author is different");
        }

    }
    @Override
    public void deleteBoard(BoardDTO boardDTO) throws Exception {
        boardMapper.deleteBoard(boardDTO);
    }

    @Override
    public BoardDTO readBoard(int boardID) throws Exception {
        return boardMapper.readBoard(boardID);
    }

    @Override
<<<<<<< HEAD
    public List<BoardDTO> allBoardList() throws Exception {
        return boardMapper.allBoardList();
=======
    public List<BoardDTO> getBoardList() throws Exception {
        return null;
>>>>>>> aa0d70e (boardDetail 넘어가기, backend api 수정)
    }

//    @Override
//    public List<BoardDTO> pageNumberBoardList(Long startPageNumber) throws Exception {
//        return null;
//    }
}
