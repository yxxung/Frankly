package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ConferenceAttendanceDTO;
import com.frankly.restapi.domain.ConferenceBillLawDTO;
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
@RequestMapping("/api/attendance")
public class ConferenceAttendanceController {

    private final ConferenceAttendanceService conferenceAttendanceService;

    @GetMapping ("/{politicianID}")
    public ResponseEntity<List<ConferenceAttendanceDTO>> readConferenceAttendance(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readConferenceAttendance - politicianID : " + politicianID);

        return new ResponseEntity<>(conferenceAttendanceService.readConferenceAttendance(politicianID), HttpStatus.OK);
    }

    //updateConferenceAttendance
    @PutMapping("/update")
    public ResponseEntity<ConferenceBillLawDTO> updateConferenceAttendance(@PathVariable("attendanceID") int attendanceID, @PathVariable("politicianID") int politicianID)
            throws Exception{
        log.info("updateConferenceAttendance : " + attendanceID);

        conferenceAttendanceService.updateConferenceAttendance(attendanceID, politicianID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //deleteConferenceAttendance
    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteConferenceAttendance(@PathVariable("attendanceID") int attendanceID)
            throws Exception{
        log.info("deleteConferenceAttendance : " + attendanceID);

        conferenceAttendanceService.deleteConferenceAttendance(attendanceID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}
