package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.Date;

@Data
@NoArgsConstructor
public class ConferenceScheduleDTO {

    private int conferenceID;

    private int generation;

    //@DateTimeFormat(pattern = "yyyy-MM-dd")
    private Date conferenceDate;
    //private SimpleDateFormat conferenceDate = new SimpleDateFormat("yyyy-MM-dd");

    private String conferenceTitle;

    private int conferenceSession;


}
