package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ConferenceBillLawDTO;
import com.frankly.restapi.domain.ConferenceScheduleDTO;
import com.frankly.restapi.service.ConferenceScheduleService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static java.time.LocalTime.now;

@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/schedule")
public class ConferenceScheduleController {

    private final ConferenceScheduleService conferenceScheduleService;

    //오늘의 국회 일정
    @GetMapping("")
    public ResponseEntity<List<ConferenceScheduleDTO>> readConferenceSchedule()
            throws Exception {
        log.info("readConferenceSchedule - "+now());

        return new ResponseEntity<>(conferenceScheduleService.readConferenceSchedule(), HttpStatus.OK);
    }

    @PutMapping("/update")
    public ResponseEntity<ConferenceBillLawDTO> updateConferenceSchedule(@Validated @RequestBody ConferenceScheduleDTO conferenceScheduleDTO)
            throws Exception{
        log.info("updateConferenceSchedule");

        conferenceScheduleService.updateConferenceSchedule(conferenceScheduleDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteConferenceSchedule(@PathVariable("conferenceID") int conferenceID)
            throws Exception{
        log.info("deleteConferenceSchedule : " + conferenceID);

        conferenceScheduleService.deleteConferenceSchedule(conferenceID);

        return new ResponseEntity<>(HttpStatus.OK);
    }


}