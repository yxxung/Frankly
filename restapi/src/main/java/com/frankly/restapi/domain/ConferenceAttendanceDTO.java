package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data
@NoArgsConstructor
public class ConferenceAttendanceDTO {
    private int attendanceID;

    private int conferenceID;

    private int politicianID;

    private int attendance;

    private int petitionLeave;

    private int businessTrip;


    private int generation;

    private Date conferenceDate;

    private String conferenceTitle;

    private int conferenceSession;
}
