package com.frankly.restapi.controller;

import com.frankly.restapi.domain.MemberDTO;
import com.frankly.restapi.service.MemeberService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.websocket.server.PathParam;
import java.util.List;

@CrossOrigin
@Slf4j
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/infos")
public class MemberInfoController {

    private final MemeberService memeberService;

    @GetMapping("/all")
    public ResponseEntity<List<MemberDTO>>memberList()throws Exception{

    return new ResponseEntity<>(memeberService.memberList(), HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<MemberDTO> getMemberById(@PathVariable("id")Long id) throws Exception{

        MemberDTO memberDTO = memeberService.getMemberById(id);

        return new ResponseEntity<>(memberDTO, HttpStatus.OK);

    }


}
