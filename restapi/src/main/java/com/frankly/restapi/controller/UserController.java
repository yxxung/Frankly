package com.frankly.restapi.controller;


import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
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

    @GetMapping("/{userID}")
    public ResponseEntity<UserDTO> getUser(@PathVariable("userID") int userID)
            throws Exception{
        log.info("read" + userID);

        UserDTO userDTO = userService.getUser(userID);

        return new ResponseEntity<>(userDTO, HttpStatus.OK);
    }

    @PostMapping("/signup")
    public ResponseEntity<UserDTO> registerUser(@Validated @RequestBody UserDTO userDTO)
            throws Exception{
        log.info("create User " + userDTO.getEmail());

        userService.registerUser(userDTO);

        return new ResponseEntity<>(userDTO, HttpStatus.OK);

    }
    @PutMapping("/{userID}")
    public ResponseEntity<UserDTO> updateUser(@Validated @RequestBody UserDTO userDTO)
            throws Exception{
        log.info("update User " + userDTO.getName());

        userService.updateUser(userDTO);

        return new ResponseEntity<>(userDTO, HttpStatus.OK);

    }

    @DeleteMapping("/{userID}")
    public ResponseEntity<?> deleteUser(@PathVariable("userID")int userID)
            throws Exception{
        log.info("delete user : " + userID);

        userService.deleteUser(userID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

}
