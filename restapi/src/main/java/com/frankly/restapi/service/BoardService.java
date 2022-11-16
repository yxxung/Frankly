package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.mapper.BoardMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.sql.SQLException;
import java.util.List;

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
    public void updateBoard(BoardDTO boardDTO, int boardID) throws Exception {

        BoardDTO targetBoard = boardMapper.readBoard(boardID);
        //if(targetBoard.getAuthor() == (boardDTO.getAuthor())){
            try{
                boardDTO.setBoardID(boardID);
                boardMapper.updateBoard(boardDTO);
            }catch(SQLException e){
                System.out.println(e);
                e.printStackTrace();
            }

        //}else{
        //    throw new Exception("author is different - "+targetBoard.getAuthor()+" and "+boardDTO.getAuthor());
        //}

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
    public List<BoardDTO> getBoardList(String region) throws Exception {
        log.info("getList");
        return boardMapper.getBoardList(region);
    }

    @Override
    public List<BoardDTO> getBoardListAll() throws Exception {
        log.info("getAllList");
        return boardMapper.getBoardListAll();
    }

    // 게시물 총 갯수
    @Override
    public int searchCount(String searchType, String keyword) throws Exception {
        return boardMapper.searchCount(searchType, keyword);
    }

    @Override
    public List<BoardDTO> searchBoard(String region, String searchType, String keyword) throws Exception {
        log.info("getSearchList");
        return boardMapper.searchBoard(region, searchType, keyword);
    }
//    @Override
//    public List<BoardDTO> pageNumberBoardList(Long startPageNumber) throws Exception {
//        return null;
//    }
    @Override
    public List<BoardDTO> userBoard(int userID) throws Exception{
        return boardMapper.userBoard(userID);
    }

    @Override
    public List<BoardDTO> userReply(int userID) throws Exception {
        return boardMapper.userReply(userID);
    }

}
