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

    public List<BoardDTO> getBoardList() throws  Exception;

    //public List<BoardDTO> pageNumberBoardList(Long pageNumber) throws Exception;



}
