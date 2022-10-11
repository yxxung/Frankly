package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ConferenceAttendanceDTO;
import com.frankly.restapi.service.ConferenceAttendanceService;
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
@RequestMapping("/api/infos")
public class ConferenceAttendanceController {

    private final ConferenceAttendanceService conferenceAttendanceService;

    @GetMapping ("/{politicianID}/attend")
    public ResponseEntity<List<ConferenceAttendanceDTO>> readConferenceAttendance(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readConferenceAttendance - politicianID : " + politicianID);

        return new ResponseEntity<>(conferenceAttendanceService.readConferenceAttendance(politicianID), HttpStatus.OK);
    }

    //updateConferenceAttendance

    //deleteConferenceAttendance
    @DeleteMapping("/attend/{attendanceID}")
    public ResponseEntity<?>deleteConferenceAttendance(@PathVariable("attendanceID") int attendanceID)
            throws Exception{
        log.info("deleteConferenceAttendance : " + attendanceID);

        conferenceAttendanceService.deleteConferenceAttendance(attendanceID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}
