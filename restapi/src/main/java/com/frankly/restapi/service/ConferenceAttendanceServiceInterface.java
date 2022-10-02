package com.frankly.restapi.service;

import com.frankly.restapi.domain.ConferenceAttendanceDTO;

import java.util.List;

public interface ConferenceAttendanceServiceInterface {

    List<ConferenceAttendanceDTO> readConferenceAttendance(int politicianID) throws Exception;

    void updateConferenceAttendance(int attendanceID, int politicianID) throws Exception;

    void deleteConferenceAttendance(int attendanceID) throws Exception;
}
