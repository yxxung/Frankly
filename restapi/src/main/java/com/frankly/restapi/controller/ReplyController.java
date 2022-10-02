package com.frankly.restapi.controller;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.domain.ReplyDTO;
import com.frankly.restapi.service.BoardService;
import com.frankly.restapi.service.ReplyService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@RestController
@Slf4j
@CrossOrigin
@RequestMapping("/api/boards")
@RequiredArgsConstructor
public class ReplyController {

    private final ReplyService replyService;

    //댓글 달기
    @PostMapping("/{boardID}/create")
    public ResponseEntity<BoardDTO> createReply(@PathVariable int boardID) throws Exception {
        replyService.createReply(boardID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //댓글 보기
    @GetMapping("/{boardID}")
    public ResponseEntity<BoardDTO> readReply(@Validated @RequestBody ReplyDTO replyDTO) throws Exception{
        log.info("readReply");

        replyService.readReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //댓글 수정
    @PutMapping("/{boardID}")
    public ResponseEntity<?> updateReply(@Validated @RequestBody ReplyDTO replyDTO)throws Exception{
        replyService.updateReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //댓글 삭제
    @DeleteMapping("/{boardID}")
    public ResponseEntity<?> deleteReply(@Validated @RequestBody ReplyDTO replyDTO) throws Exception{

        replyService.deleteReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }



}

