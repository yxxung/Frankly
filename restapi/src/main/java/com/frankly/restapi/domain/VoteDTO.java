package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data
@NoArgsConstructor
public class VoteDTO {
    private int voteID;

    private int politicianID;

    private int billNumber;

    private Date voteDate;

    private String voteResult;

    private String voteURL;

    //count(voteResult)
    private int voteCount;

}
