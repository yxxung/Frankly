package com.frankly.restapi.service;

import com.frankly.restapi.domain.ConferenceScheduleDTO;
import com.frankly.restapi.mapper.ConferenceScheduleMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor

public class ConferenceScheduleService implements ConferenceScheduleServiceInterface {

    private final ConferenceScheduleMapper conferenceScheduleMapper;

    @Override
    public List<ConferenceScheduleDTO> readConferenceSchedule() throws Exception {
        return conferenceScheduleMapper.readConferenceSchedule();
    }

    @Override
    public void updateConferenceSchedule(int conferenceID) throws Exception {
        conferenceScheduleMapper.updateConferenceSchedule(conferenceID);
    }

    @Override
    public void deleteConferenceSchedule(int conferenceID) throws Exception {
        conferenceScheduleMapper.deleteConferenceSchedule(conferenceID);

    }
}
