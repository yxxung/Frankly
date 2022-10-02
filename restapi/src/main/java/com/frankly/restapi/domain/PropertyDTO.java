package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data
@NoArgsConstructor
public class PropertyDTO {

    private int assetID;

    private int propertyListID;

    private int politicianID;

    private String presentPrice;

    private String propertyDetail;

}
