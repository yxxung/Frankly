package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.mapper.BoardMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.text.SimpleDateFormat;
import java.util.*;

@Service
@Slf4j
@RequiredArgsConstructor
public class BoardService implements BoardServiceInterface {

    private final BoardMapper boardMapper;

    @Override
    public void createBoard(BoardDTO boardDTO) throws Exception {

        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd kk:mm:ss");
        String strDate = dateFormat.format(Calendar.getInstance(TimeZone.getTimeZone("Asia/Seoul")).getTime());
        Date date = dateFormat.parse(strDate);
        boardDTO.setRegDate(date);
        boardDTO.setMarked(false);
        boardMapper.createBoard(boardDTO);
    }

    @Override
    public void updateBoard(BoardDTO boardDTO) throws Exception {



    }

    @Override
    public void deleteBoard(BoardDTO boardDTO) throws Exception {

    }

    @Override
    public BoardDTO readBoard(int region,Long id) throws Exception {
        return boardMapper.readBoard(region, id);
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
