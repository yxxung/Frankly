package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.BoardDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

//인터페이스를 마이바티스용 mapper로 만들어줌
//XML mapper에서 이름과 일치하는 SQL문을 찾아서 실행해준다
@Mapper
public interface BoardMapper {

    public void createBoard(BoardDTO boardDTO) throws Exception;

    public void updateBoard(BoardDTO boardDTO) throws Exception;

    public void deleteBoard(BoardDTO boardDTO) throws Exception;

    public BoardDTO readBoard(int boardID)throws Exception;

    public List<BoardDTO> getBoardList(String region) throws  Exception;

    public List<BoardDTO> getBoardListAll() throws  Exception;

    public List<BoardDTO> searchBoard(String region, String searchType, String keyword) throws Exception;

    // 게시물 총 갯수 + 검색 적용
    public int searchCount(String searchType, String keyword) throws Exception;
        //public List<BoardDTO> pageNumberBoardList(Long pageNumber) throws Exception;

    public List<BoardDTO> userBoard(int userID) throws Exception;

}
