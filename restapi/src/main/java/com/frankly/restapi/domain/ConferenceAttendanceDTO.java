package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class ConferenceAttendanceDTO {
    private int attendanceID;

    private int conferenceID;

    private int politicianID;

    private int attendance;

    private int petitionLeave;

    private int businessTrip;
}
