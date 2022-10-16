package com.frankly.restapi.domain;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

import static java.time.LocalDateTime.now;

@Data
@Builder
@NoArgsConstructor
public class ReplyDTO {

    private int replyID;

    private String reply;

    private int userID;

    private LocalDateTime regDate;

    private int boardID;


    @Builder
    public ReplyDTO(int replyID, String reply, int userID,
                    LocalDateTime regDate, int boardID){
        this.replyID = replyID;
        this.reply = reply;
        this.regDate = now();
        this.userID = userID;
        this.boardID = boardID;
    }

}
