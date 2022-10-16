package com.frankly.restapi.controller;

import com.frankly.restapi.domain.PoliticianDTO;
import com.frankly.restapi.service.PoliticianService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@Slf4j
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/politician")
public class PoliticianController {

    private final PoliticianService politicianService;


    @GetMapping("/{politicianID}")
    public ResponseEntity<PoliticianDTO> getPoliticianById(@PathVariable("politicianID")int politicianID) throws Exception{

        PoliticianDTO politicianDTO = politicianService.getPoliticianById(politicianID);

        return new ResponseEntity<>(politicianDTO, HttpStatus.OK);


    }

    @GetMapping("/search")
    public ResponseEntity<List<PoliticianDTO>> getPoliticianByName(@PathVariable("politicianName")String politicianName) throws Exception{

        return new ResponseEntity<>(politicianService.getPoliticianByName(politicianName), HttpStatus.OK);

    }

    @GetMapping("/all")
    public ResponseEntity<List<PoliticianDTO>>politicianList()throws Exception{

        return new ResponseEntity<>(politicianService.politicianList(), HttpStatus.OK);
    }
}
