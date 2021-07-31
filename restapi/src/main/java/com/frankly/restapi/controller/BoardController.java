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
                                              @PathVariable("region") int region) throws Exception{
      log.info("게시물 생성" + boardDTO.getAuthor());
      boardDTO.setRegion(region);
      boardService.createBoard(boardDTO);
      log.info("time: " + boardDTO.getRegDate());

      return new ResponseEntity<>(boardDTO, HttpStatus.OK);
  }


  //본인이 쓴 글, 그리고 admin만 수정할 수 있음. 그걸 어떻게 판별할것인가?
  @PutMapping("/{region}/{id}")
    public ResponseEntity<?> updateBoard(@Validated @RequestBody BoardDTO boardDTO,
                                         @PathVariable("region") int region,
                                         @PathVariable("id")Long id)throws Exception{

      log.info("개시물 수정 수정자 :"  + boardDTO.getAuthor());
      boardService.updateBoard(boardDTO, region, id);
      return new ResponseEntity<>(HttpStatus.OK);
  }

  @GetMapping("/{region}/{id}")
    public ResponseEntity<BoardDTO> getBoardById(@PathVariable int region,
                                                 @PathVariable Long id) throws Exception{

      log.info("게시물 불러오기 : " + id);
      try{
          BoardDTO boardDTO = boardService.readBoard(region, id);
          return new ResponseEntity<>(boardDTO, HttpStatus.OK);
      }catch (Exception e){
          return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
      }


  }

  @GetMapping("/{region}/{start}")
    public ResponseEntity<BoardDTO> getBoardList(@PathVariable Long start) throws Exception{

      log.info("게시글 리스트 불러오기 +  "  + start);
//      BoardDTO boardDTO = boardService.pageNumberBoardList(start);

      return new ResponseEntity<>(HttpStatus.OK);
  }

  @DeleteMapping("/{region}/{id}")
    public ResponseEntity<?> deleteBoard(@PathVariable("region") int region,
                                         @PathVariable("id") Long id) throws Exception{

      BoardDTO boardDTO = new BoardDTO();
      boardDTO.setId(id);
      boardDTO.setRegion(region);

      log.info(id + "게시글 삭제");
      boardService.deleteBoard(boardDTO);

      return new ResponseEntity<>(HttpStatus.OK);

  }



}
