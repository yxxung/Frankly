package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
public class LikeDTO {

    private int likeID;

    private int boardID;

    private int userID;

    private int likeCount;

    //boardDTO
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

    private int replyID;

    private String reply;

    private int userID;

    private LocalDateTime replyRegDate;

    private int boardID;

    private int replyCount;
}
