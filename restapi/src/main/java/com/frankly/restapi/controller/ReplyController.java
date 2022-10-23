package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ReplyDTO;
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
@RequestMapping("/api/replys")
@RequiredArgsConstructor
public class ReplyController {

    private final ReplyService replyService;

    //댓글 달기
    @PostMapping(value = "/create")
    public ResponseEntity<ReplyDTO> createReply(@Validated @RequestBody ReplyDTO replyDTO) throws Exception {
        replyService.createReply(replyDTO);
        return new ResponseEntity<>(replyDTO, HttpStatus.OK);
    }

    //댓글 보기
    @GetMapping("/{boardID}/replyList")
    public ResponseEntity<List<ReplyDTO>> readReply(@PathVariable("boardID") int boardID) throws Exception{
        log.info("readReply");
        return new ResponseEntity<>(replyService.readReply(boardID), HttpStatus.OK);
    }

    //댓글 수
    /*
    @GetMapping("/{boardID}/replyCount")
    public ResponseEntity<?> countReply(@Validated @RequestBody ReplyDTO replyDTO)throws Exception{
        replyService.countReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }*/

    //댓글 수정
    @PutMapping("/{boardID}/update")
    public ResponseEntity<?> updateReply(@Validated @RequestBody ReplyDTO replyDTO)throws Exception{
        replyService.updateReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //댓글 삭제
    @DeleteMapping("/{boardID}/delete")
    public ResponseEntity<?> deleteReply(@Validated @RequestBody ReplyDTO replyDTO) throws Exception{

        replyService.deleteReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }



}