package com.frankly.restapi.domain;

import lombok.*;

import java.util.Date;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class BoardDTO {

    private Long id;

    private String author;

    private Date regDate;

    private Boolean marked;

    private String title;

    private String content;

    private int region;



//
//    @Builder
//    public BoardDTO(Long id, String author, Date regDate,
//                    Boolean marked, String title, String content
//                    ,int region){
//        this.id = id;
//        this.author = author;
//        this.regDate = regDate;
//        this.marked = marked;
//        this.title = title;
//        this.content = content;
//        this.region = region;
//    }
//
//
//    @Builder
//    public BoardDTO(Long id, int region){
//        this.id = id;
//        this.region = region;
//    }


}
