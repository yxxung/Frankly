package com.frankly.restapi.controller;

import com.frankly.restapi.domain.VoteDTO;
import com.frankly.restapi.service.VoteService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/vote")
public class VoteController {

    private final VoteService voteService;

    //법안투표결과보기
    @GetMapping("/{politicianID}")
    public ResponseEntity<List<VoteDTO>> readVote(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readVote - politicianID : "+ politicianID);

        return new ResponseEntity<>(voteService.readVote(politicianID), HttpStatus.OK);
    }

    //숫자로나타내기
    @GetMapping("/count/{politicianID}")
    public ResponseEntity<List<VoteDTO>> countVote(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("countVote - politicianID : "+ politicianID);

        return new ResponseEntity<>(voteService.countVote(politicianID), HttpStatus.OK);
    }

    //수정
    @PutMapping("/update")
    public ResponseEntity<VoteDTO> updateVote(@PathVariable("voteID") int voteID)
            throws Exception{
        log.info("update Vote");

        voteService.updateVote(voteID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //삭제
    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteVote(@PathVariable("voteID") int voteID)
            throws Exception{
        log.info("deleteVote : " + voteID);

        voteService.deleteVote(voteID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}

