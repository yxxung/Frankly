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

    //count(R.replyID)
    private int replyCount;

}