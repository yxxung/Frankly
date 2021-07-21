package com.frankly.restapi.controller;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.service.BoardService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@Slf4j
@CrossOrigin
@RequestMapping("/api/boards")
@RequiredArgsConstructor
public class BoardController {


    private final BoardService boardService;

    //지역마다 DB분리 필요할수도
    //create board이름 변경
    //DB 분리 고려..
  @PostMapping("/{region}/create")
  public ResponseEntity<BoardDTO> createBoard(@Validated @RequestBody BoardDTO boardDTO,
                                              @PathVariable("region") String region) throws Exception{
      log.info("게시물 생성" + boardDTO.getAuthor());
      boardDTO.setRegion(region);
      boardService.createBoard(boardDTO);
      log.info("time: " + boardDTO.getRegDate());

      return new ResponseEntity<>(boardDTO, HttpStatus.OK);
  }


}
