package com.frankly.restapi.domain;

import lombok.*;
import org.apache.tomcat.jni.Local;
import org.springframework.format.annotation.DateTimeFormat;

import java.time.LocalDateTime;
import java.util.Date;

@Data
@Builder
@NoArgsConstructor
//@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class BoardDTO {

    private int boardID;

    private int userID;

    private LocalDateTime regDate;

    private int marked;

    private String title;

    private String content;

    private String region;


    @Builder
    public BoardDTO(int boardID, int userID, LocalDateTime regDate,
                    int marked, String title, String content,
                    String region){
        this.boardID = boardID;
        this.userID = userID;
        this.regDate = regDate;
        this.marked = marked;
        this.title = title;
        this.content = content;
        this.region = region;
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
