package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class BookmarkDTO {

    private int bookmarkID;

    private int politicianID;

    private int userID;
}
