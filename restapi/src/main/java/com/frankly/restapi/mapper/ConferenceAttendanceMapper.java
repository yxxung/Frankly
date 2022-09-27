package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.ConferenceAttendanceDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface ConferenceAttendanceMapper {

    public List<ConferenceAttendanceDTO> readConferenceAttendance(int politicianID) throws Exception;

    public void updateConferenceAttendance(int attendanceID, int politicianID) throws Exception;

    public void deleteConferenceAttendance(int attendanceID) throws Exception;

}
