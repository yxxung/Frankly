package com.frankly.restapi.domain;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

import static java.time.LocalDateTime.now;

@Data
@Builder
@NoArgsConstructor
//@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class BoardDTO {

    private int boardID;

    private int userID;

    private LocalDateTime boardRegDate;

    private int marked;

    private String title;

    private String content;

    private String region;


    private int replyID;

    private String reply;

    private LocalDateTime replyRegDate;
    //count(R.replyID)
    private int replyCount;


    @Builder
    public BoardDTO(int boardID, int userID, LocalDateTime boardRegDate,
                    int marked, String title, String content,
                    String region, int replyID, String reply, LocalDateTime replyRegDate, int replyCount){
        this.boardID = boardID;
        this.userID = userID;
        this.boardRegDate = now();
        this.marked = marked;
        this.title = title;
        this.content = content;
        this.region = region;

        this.replyID = replyID;
        this.reply = reply;
        this.replyRegDate = replyRegDate;
        this.replyCount = replyCount;

    }

    /*@Builder
    public BoardDTO(int boardID, String region){
        this.boardID = boardID;
        this.region = region;
    }*/

    public int getAuthor() { return userID;}

    //public void setRegion(int region) {}

    //public void setId(int boardID) {}

    //public void setRegDate(Date date) {}

    //public void setMarked(int marked) {}
}
