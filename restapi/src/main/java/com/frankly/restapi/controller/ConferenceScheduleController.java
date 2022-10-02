package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ConferenceScheduleDTO;
import com.frankly.restapi.service.ConferenceScheduleService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.Date;
import java.util.List;

import static com.sun.org.apache.xalan.internal.lib.ExsltDatetime.date;
import static java.time.LocalTime.now;

@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/infos")
public class ConferenceScheduleController {

    private final ConferenceScheduleService conferenceScheduleService;

    //오늘의 국회 일정
    @GetMapping("/schedule")
    public ResponseEntity<List<ConferenceScheduleDTO>> readConferenceSchedule()
            throws Exception {
        log.info("readConferenceSchedule - "+date());

        return new ResponseEntity<>(conferenceScheduleService.readConferenceSchedule(), HttpStatus.OK);
    }

    @DeleteMapping("/schedule/{conferenceID}")
    public ResponseEntity<?>deleteConferenceSchedule(@PathVariable("conferenceID") int conferenceID)
            throws Exception{
        log.info("deleteConferenceSchedule : " + conferenceID);

        conferenceScheduleService.deleteConferenceSchedule(conferenceID);

        return new ResponseEntity<>(HttpStatus.OK);
    }


}