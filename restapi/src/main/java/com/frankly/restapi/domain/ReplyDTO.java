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

    private LocalDateTime replyRegDate;

    private int boardID;

    private int replyCount;


    @Builder
    public ReplyDTO(int replyID, String reply, int userID,
                    LocalDateTime replyRegDate, int boardID, int replyCount){
        this.replyID = replyID;
        this.reply = reply;
        this.replyRegDate = now();
        this.userID = userID;
        this.boardID = boardID;
        this.replyCount = replyCount;
    }

}
