package com.frankly.restapi.controller;

import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.domain.VoteDTO;
import com.frankly.restapi.service.VoteService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/infos")
public class VoteController {

    private final VoteService voteService;

    //법안투표결과보기
    @GetMapping("/{politicianID}/vote")
    public ResponseEntity<List<VoteDTO>> readVote(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readVote - politicianID : "+ politicianID);

        return new ResponseEntity<>(voteService.readVote(politicianID), HttpStatus.OK);
    }

    //숫자로나타내기
    @GetMapping("/{politicianID}/voteCount")
    public ResponseEntity<List<VoteDTO>> countVote(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("countVote - politicianID : "+ politicianID);

        return new ResponseEntity<>(voteService.countVote(politicianID), HttpStatus.OK);
    }

    //수정
    @PutMapping("/vote/{voteID}")
    public ResponseEntity<VoteDTO> updateVote(@Validated @RequestBody VoteDTO voteDTO)
            throws Exception{
        log.info("update Vote");

        voteService.updateVote(voteDTO);

        return new ResponseEntity<>(voteDTO, HttpStatus.OK);
    }

    //삭제
    @DeleteMapping("/vote/{voteID}")
    public ResponseEntity<?>deleteVote(@PathVariable("voteID") int voteID)
            throws Exception{
        log.info("deleteVote : " + voteID);

        voteService.deleteVote(voteID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}

