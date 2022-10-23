package com.frankly.restapi.controller;


import com.frankly.restapi.domain.PropertyDTO;
import com.frankly.restapi.domain.PropertyListDTO;
import com.frankly.restapi.domain.PropertyChangeDTO;
import com.frankly.restapi.service.PropertyService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@Slf4j
@CrossOrigin
@RequestMapping("/api/property")
@RequiredArgsConstructor
public class PropertyController {

    private final PropertyService propertyService;

    @GetMapping("/create")
    public ResponseEntity<PropertyDTO> createProperty(@Validated @RequestBody PropertyDTO propertyDTO)
            throws Exception {
        log.info("createProperty");

        propertyService.createProperty(propertyDTO);

        return new ResponseEntity<>(propertyDTO, HttpStatus.OK);
    }

    @GetMapping("/{politicianID}")
    public ResponseEntity<List<PropertyDTO>> readProperty(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readProperty - politicianID : "+ politicianID);

        return new ResponseEntity<>(propertyService.readProperty(politicianID), HttpStatus.OK);
    }

    @GetMapping("/change/{politicianID}")
    public ResponseEntity<List<PropertyChangeDTO>> readPropertyChange(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readPropertyChange - politicianID : "+ politicianID);

        return new ResponseEntity<>(propertyService.readPropertyChange(politicianID), HttpStatus.OK);
    }

    //수정
    @PutMapping("/update")
    public ResponseEntity<PropertyDTO> updateProperty(@Validated @RequestBody PropertyDTO propertyDTO)
            throws Exception{
        log.info("update Property");

        propertyService.updateProperty(propertyDTO);

        return new ResponseEntity<>(propertyDTO, HttpStatus.OK);
    }

    //삭제
    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteProperty(@Validated @RequestBody PropertyDTO propertyDTO)
            throws Exception{
        log.info("deleteVote");

        propertyService.deleteProperty(propertyDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

}
