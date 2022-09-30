package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class PropertyChangeDTO {

    private int changeID;

    private int politicianID;

    private int propertyID;

    private String period;

    private String price;

    private String reason;


}
