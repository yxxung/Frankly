package com.frankly.restapi.service;

import com.frankly.restapi.domain.UserDTO;

import java.util.List;

public interface UserServiceInterface {

    public void registerUser(UserDTO userDTO) throws Exception;

    public UserDTO getUser(int userID) throws Exception;

    public void updateUser(UserDTO userDTO) throws Exception;

    public void deleteUser(int userID) throws Exception;


    public List<UserDTO> userList() throws Exception;
}
