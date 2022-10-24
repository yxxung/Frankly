package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class NewsKeywordDTO {

    private int newsKeywordID;

    private String newsKeyword;

    private int politicianID;

    private int newsID;




}
