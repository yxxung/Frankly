package com.frankly.restapi.service;

import com.frankly.restapi.domain.UserDTO;

import java.util.List;

public interface UserServiceInterface {

    public void registerUser(UserDTO userDTO) throws Exception;

    public UserDTO getUser(Long userId) throws Exception;

    public void updateUser(UserDTO userDTO) throws Exception;

    public void deleteUser(Long userId) throws Exception;


    public List<UserDTO> userList() throws Exception;
}
