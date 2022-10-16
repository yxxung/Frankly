package com.frankly.restapi.service;

import com.frankly.restapi.domain.ConferenceScheduleDTO;

import java.util.List;

public interface ConferenceScheduleServiceInterface {


    public List<ConferenceScheduleDTO> readConferenceSchedule() throws Exception;

    public void updateConferenceSchedule(int conferenceID) throws Exception;

    public void deleteConferenceSchedule(int conferenceID) throws Exception;
}
