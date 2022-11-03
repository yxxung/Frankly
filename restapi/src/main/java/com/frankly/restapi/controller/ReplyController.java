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
    @PatchMapping("/{replyID}/update")
    public ResponseEntity<?> updateReply(@Validated @RequestBody ReplyDTO replyDTO,
                                        @PathVariable("replyID") int replyID)throws Exception{
        //replyDTO.setBoardID(boardID);
        replyDTO.setReplyID(replyID);
        //replyDTO.setReply(reply);

        log.info(replyID +"번째 댓글 수정");
        replyService.updateReply(replyDTO, replyID);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    //댓글 삭제
    @DeleteMapping("/{boardID}/{replyID}/delete")
    public ResponseEntity<?> deleteReply(@PathVariable("boardID") int boardID,
                                         @PathVariable("replyID") int replyID) throws Exception{
        ReplyDTO replyDTO = new ReplyDTO();
        replyDTO.setBoardID(boardID);
        replyDTO.setReplyID(replyID);

        log.info(boardID + "번째 게시글 " + replyID +"번째 댓글 삭제");

        replyService.deleteReply(replyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }



}