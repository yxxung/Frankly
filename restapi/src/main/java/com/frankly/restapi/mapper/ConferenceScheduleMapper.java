package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.ConferenceScheduleDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.Date;
import java.util.List;

@Mapper
public interface ConferenceScheduleMapper {

    public List<ConferenceScheduleDTO> readConferenceSchedule() throws Exception;

    public void updateConferenceSchedule(ConferenceScheduleDTO conferenceScheduleDTO) throws Exception;

    public void deleteConferenceSchedule(int conferenceID) throws Exception;

}