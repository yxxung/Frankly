package com.frankly.restapi.controller;

import com.frankly.restapi.config.JwtTokenUtil;
import com.frankly.restapi.domain.JwtRequest;
import com.frankly.restapi.domain.JwtResponse;
import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.service.JwtUserDetailsService;
import com.frankly.restapi.service.UserAuthProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.DisabledException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin
@RequestMapping("/api/auth")
public class JwtAuthenticationController {


    @Autowired
    private UserAuthProvider userAuthProvider;

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Autowired
    private JwtUserDetailsService userDetailsService;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @PostMapping("/signin")
    public ResponseEntity<?> createAuthenticationToken(@RequestBody JwtRequest authenticationRequest) throws Exception {

        try {
            userAuthProvider.authenticate(new UsernamePasswordAuthenticationToken(
                    authenticationRequest.getEmail(), authenticationRequest.getPassword()));

            UserDetails userDetails = userDetailsService
                    .loadUserByUsername(authenticationRequest.getEmail());
            String token = jwtTokenUtil.generateToken(userDetails);
            UserDTO user = userDetailsService.getUserByEmail(authenticationRequest.getEmail());

            return ResponseEntity.ok(new JwtResponse(token, user.getEmail(), user.getUserAuth(), user.getUserID()));

        } catch (DisabledException e) {
            throw new Exception("USER_DISABLED", e);
        } catch (BadCredentialsException e) {
            throw new Exception("INVALID_CREDENTIALS", e);
        }


    }


}
