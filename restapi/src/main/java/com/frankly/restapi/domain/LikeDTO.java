package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class LikeDTO {

    private int likeID;

    private int boardID;

    private int userID;

    private int likeCount;

}
