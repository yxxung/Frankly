package com.frankly.restapi.controller;


import ch.qos.logback.core.encoder.EchoEncoder;
import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.tomcat.util.buf.UDecoder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;


@CrossOrigin
@Slf4j
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    @GetMapping("/user/{userId}")
    public ResponseEntity<UserDTO> getUser(@PathVariable("userId") Long userId)
            throws Exception{
        log.info("read" + userId);

        UserDTO userDTO = userService.getUser(userId);

        return new ResponseEntity<>(userDTO, HttpStatus.OK);
    }

    @PostMapping("/user")
    public ResponseEntity<UserDTO> registerUser(@Validated @RequestBody UserDTO userDTO)
            throws Exception{
        log.info("create User" + userDTO.getEmail());

        userService.registerUser(userDTO);

        return new ResponseEntity<>(userDTO, HttpStatus.OK);

    }

}
