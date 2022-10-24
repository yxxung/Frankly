package com.frankly.restapi.controller;

import com.frankly.restapi.domain.ConferenceBillLawDTO;
import com.frankly.restapi.service.ConferenceBillLawService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/billLaw")
public class ConferenceBillLawController {

    private final ConferenceBillLawService conferenceBillLawService;

    @GetMapping("/{politicianID}")
    public ResponseEntity<List<ConferenceBillLawDTO>> readConferenceBillLaw(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readConferenceBillLaw - politicianID : " + politicianID);

        return new ResponseEntity<>(conferenceBillLawService.readConferenceBillLaw(politicianID), HttpStatus.OK);
    }

    @PutMapping("/update")
    public ResponseEntity<ConferenceBillLawDTO> updateConferenceBillLaw(@PathVariable("billID") int billID)
            throws Exception{
        log.info("updateConferenceBillLaw : " + billID);

        conferenceBillLawService.updateConferenceBillLaw(billID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteConferenceBillLaw(@PathVariable("billID") int billID)
            throws Exception{
        log.info("deleteConferenceBillLaw : " + billID);

        conferenceBillLawService.deleteConferenceBillLaw(billID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}

