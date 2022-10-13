package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.format.annotation.DateTimeFormat;

@Data
@NoArgsConstructor
public class NewsDTO {

    private int newsID;

    private int politicianID;

    private String newsTitle;

    private String newsURL;

    private String newsKeyword;

    private String newsAbstract;

    private DateTimeFormat newsDate;

    private String newsContents;


}
