package com.frankly.restapi.controller;

import com.frankly.restapi.domain.MemberDTO;
import com.frankly.restapi.service.MemeberService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RequiredArgsConstructor
@RestController
@RequestMapping("/infos")
public class MemberInfoController {

    private final MemeberService memeberService;

    @PostMapping("/all")
    public ResponseEntity<List<MemberDTO>>memberList()throws Exception{
    return new ResponseEntity<>(memeberService.memberList(), HttpStatus.OK);
    }

}
