package com.frankly.restapi.domain;

import lombok.*;

import java.util.Date;

@Data
@Builder
@NoArgsConstructor
//@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class BoardDTO {

    private int boardID;

    private int userID;

    private Date regDate;

    private int marked;

    private String title;

    private String content;

    private int region;


    @Builder
    public BoardDTO(int boardID, int userID, Date regDate,
                    int marked, String title, String content
                    ,int region){
        this.boardID = boardID;
        this.userID = userID;
        this.regDate = regDate;
        this.marked = marked;
        this.title = title;
        this.content = content;
        this.region = region;
    }

    @Builder
    public BoardDTO(int boardID, int region){
        this.boardID = boardID;
        this.region = region;
    }

    public int getAuthor() { return userID;}
    
    //public void setRegion(int region) {}

    //public void setId(int boardID) {}

    //public void setRegDate(Date date) {}

    //public void setMarked(int marked) {}
}
