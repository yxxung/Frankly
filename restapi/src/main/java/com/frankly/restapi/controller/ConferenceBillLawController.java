package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ConferenceBillLawDTO;
import com.frankly.restapi.domain.VoteDTO;
import com.frankly.restapi.service.ConferenceBillLawService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/infos")
public class ConferenceBillLawController {

    private final ConferenceBillLawService conferenceBillLawService;

    @GetMapping("/{politicianID}/billLaw")
    public ResponseEntity<List<ConferenceBillLawDTO>> readConferenceBillLaw(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readConferenceBillLaw - politicianID : " + politicianID);

        return new ResponseEntity<>(conferenceBillLawService.readConferenceBillLaw(politicianID), HttpStatus.OK);
    }

    @PutMapping("/billLaw/{billID}")
    public ResponseEntity<ConferenceBillLawDTO> updateConferenceBillLaw(@PathVariable("billID") int billID)
            throws Exception{
        log.info("update Vote : " + billID);

        conferenceBillLawService.updateConferenceBillLaw(billID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    @DeleteMapping("/billLaw/{billID}")
    public ResponseEntity<?>deleteConferenceBillLaw(@PathVariable("billID") int billID)
            throws Exception{
        log.info("deleteConferenceBillLaw : " + billID);

        conferenceBillLawService.deleteConferenceBillLaw(billID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}

