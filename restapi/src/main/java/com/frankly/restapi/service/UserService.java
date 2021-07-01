package com.frankly.restapi.service;

import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.mapper.UserMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class UserService implements UserServiceInterface {

    private final UserMapper userMapper;

    @Override
    public void registerUser(UserDTO userDTO) throws Exception {
        userMapper.createUser(userDTO);
    }

    @Override
    public UserDTO getUser(Long userId) throws Exception {
        return userMapper.readUser(userId);
    }

    @Override
    public void updateUser(UserDTO userDTO) throws Exception {

    }

    @Override
    public void deleteUser(Long userId) throws Exception {

    }

    @Override
    public List<UserDTO> userList() throws Exception {
        return null;
    }
}
