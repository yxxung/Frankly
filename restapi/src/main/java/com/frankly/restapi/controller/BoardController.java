package com.frankly.restapi.controller;

import com.frankly.restapi.domain.BoardDTO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@Slf4j
@CrossOrigin
@RequestMapping("/api/boards")
public class BoardController {

    //지역마다 DB분리 필요할수도
//    @GetMapping("/{legion}/all")
//    public ResponseEntity<List<BoardDTO>>

}
