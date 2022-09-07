package com.frankly.restapi.service;

import com.frankly.restapi.domain.UserDTO;
import com.frankly.restapi.mapper.UserMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCrypt;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class UserService implements UserServiceInterface {

    private final UserMapper userMapper;

    private final PasswordEncoder passwordEncoder;

    @Override
    public void registerUser(UserDTO userDTO) throws Exception {

        String password = userDTO.getPassword();
        String encryptedpassword = passwordEncoder.encode(password);
        userDTO.setPassword(encryptedpassword);

        userMapper.createUser(userDTO);
    }

    @Override
    public UserDTO getUser(int userID) throws Exception {
        return userMapper.readUser(userID);
    }

    @Override
    public void updateUser(UserDTO userDTO) throws Exception {
        userMapper.updateUser(userDTO);
    }

    @Override
    public void deleteUser(int userID) throws Exception {
        userMapper.deleteUser(userID);

    }

    @Override
    public List<UserDTO> userList() throws Exception {
        return null;
    }
}
