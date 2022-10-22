package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
public class ReplyDTO {

    private int replyID;

    private String reply;

    private int userID;

    private LocalDateTime replyRegDate;

    private int boardID;


}
