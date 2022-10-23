package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
public class NewsDTO {

    private int newsID;

    private int politicianID;

    private String newsTitle;

    private String newsURL;

    private String newsKeyword;

    private String newsAbstract;

    private LocalDateTime newsDate;

    private String newsContents;

    private int newsKeywordID;
}
