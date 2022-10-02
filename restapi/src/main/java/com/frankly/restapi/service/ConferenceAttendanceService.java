package com.frankly.restapi.service;

import com.frankly.restapi.domain.ConferenceAttendanceDTO;
import com.frankly.restapi.mapper.ConferenceAttendanceMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class ConferenceAttendanceService implements ConferenceAttendanceServiceInterface {

    private final ConferenceAttendanceMapper conferenceAttendanceMapper;

    @Override
    public List<ConferenceAttendanceDTO> readConferenceAttendance(int politicianID) throws Exception {
        return conferenceAttendanceMapper.readConferenceAttendance(politicianID);

    }

    @Override
    public void updateConferenceAttendance(int attendanceID, int politicianID) throws Exception {
        conferenceAttendanceMapper.updateConferenceAttendance(attendanceID, politicianID);

    }

    @Override
    public void deleteConferenceAttendance(int attendanceID) throws Exception {
        conferenceAttendanceMapper.deleteConferenceAttendance(attendanceID);

    }

}