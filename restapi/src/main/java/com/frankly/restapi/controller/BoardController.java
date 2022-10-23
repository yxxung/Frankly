package com.frankly.restapi.controller;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.domain.PageVO;
import com.frankly.restapi.service.BoardService;
import com.frankly.restapi.service.ReplyService;

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

    private final ReplyService replyService;

    //file 전송시 file과 dto를 나눠서 전송해야 함
    //requestpart로 나눠서 받기,,,나머지 수정 필요
//    @PostMapping(value = "/{region}/create", consumes = { MediaType.MULTIPART_FORM_DATA_VALUE, MediaType.APPLICATION_JSON_VALUE})
//    public ResponseEntity<BoardDTO> createBoard(@Validated @RequestPart BoardDTO boardDTO,
//                                                @RequestPart(required = false) MultipartFile file) throws Exception{
//        log.info("게시물 생성" + boardDTO.getAuthor());
//        boardService.createBoard(boardDTO);
//        log.info("time: " + boardDTO.getBoardRegDate());
//        log.info("dto: " + boardDTO);
//        log.info("file: " + file);
//
//        return new ResponseEntity<>(boardDTO, HttpStatus.OK);
//    }
    @PostMapping(value = "/create")
    public ResponseEntity<BoardDTO> createBoard(@Validated @RequestBody BoardDTO boardDTO) throws Exception{
        log.info("게시물 생성" + boardDTO.getAuthor());
        boardService.createBoard(boardDTO);
        log.info("time: " + boardDTO.getBoardRegDate());
        log.info("dto: " + boardDTO);


        return new ResponseEntity<>(boardDTO, HttpStatus.OK);
    }


    //본인이 쓴 글, 그리고 admin만 수정할 수 있음. 그걸 어떻게 판별할것인가?
    @PutMapping("/update/{boardID}")
    public ResponseEntity<?> updateBoard(@Validated @RequestBody BoardDTO boardDTO,
                                         @PathVariable("boardID")int boardID)throws Exception{

        log.info("게시물 수정 수정자 :"  + boardDTO.getAuthor());
        boardService.updateBoard(boardDTO, boardID);
        return new ResponseEntity<>(HttpStatus.OK);
    }


    @GetMapping("/{boardID}")
    public ResponseEntity<BoardDTO> readBoard(@PathVariable("boardID") int boardID) throws Exception{

        log.info("게시물 불러오기 : " + boardID);
        try{
            BoardDTO boardDTO = boardService.readBoard(boardID);
            replyService.readReply(boardID);
            replyService.countReply(boardID);

            return new ResponseEntity<>(boardDTO, HttpStatus.OK);
        }catch (Exception e){
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping("/boardlist/{region}")
    public ResponseEntity<List<BoardDTO>> getBoardList(@PathVariable("region") String region) throws Exception{

        return new ResponseEntity<>(boardService.getBoardList(region), HttpStatus.OK);
    }

    @DeleteMapping("/delete/{boardID}")
    public ResponseEntity<?> deleteBoard(@PathVariable("boardID") int boardID) throws Exception{

        BoardDTO boardDTO = new BoardDTO();
        boardDTO.setBoardID(boardID);

        log.info(boardID + " 게시글 삭제");
        boardService.deleteBoard(boardDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //게시물 검색
    @GetMapping("/boardlist/{region}/search")
    public ResponseEntity<List<BoardDTO>> searchBoard(@PathVariable("region") String region,
                                                      @RequestParam(value = "searchType", required = false, defaultValue = "title") String searchType,
                                                      @RequestParam(value = "keyword", required = false, defaultValue = "") String keyword) throws Exception{

        PageVO pageVO = new PageVO();

        //PageVO.setNum(num);
        //PageVO.setCount(boardService.searchCount(searchType, keyword));
        //pageVO.setSearchTypeKeyword(searchType, keyword);
        pageVO.setSearchType(searchType);
        pageVO.setKeyword(keyword);



        return new ResponseEntity<>(boardService.searchBoard(region, searchType, keyword), HttpStatus.OK);
    }


}
