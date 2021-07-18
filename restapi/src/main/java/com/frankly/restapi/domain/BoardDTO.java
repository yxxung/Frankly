package com.frankly.restapi.domain;

import lombok.*;

import java.util.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class BoardDTO {

    private Long id;

    private String author;

    private Date regDate;

    private Boolean marked;

    private String title;

    private String content;


}
