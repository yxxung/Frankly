package com.frankly.restapi.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

@Data
@NoArgsConstructor
public class ConferenceBillLawDTO {
    private int billID;

    private int generation;

    private String billTitle;

    private String proposer;

    private String billResult;

    private Date effectiveDate;

    private Date proposalDate;

    private String competentCommittee;

    private int billNumber;

    private String billLawAPIID;

}
