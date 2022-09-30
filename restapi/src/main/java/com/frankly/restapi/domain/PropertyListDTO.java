package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class PropertyListDTO {

    private int propertyListID;

    private String relation;

    private String kind;

    private String section;

}
