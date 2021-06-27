package com.frankly.restapi.service;

import com.frankly.restapi.domain.MemberDTO;
import com.frankly.restapi.mapper.MemberMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor
@Service
public class MemeberService implements MemberServiceInterface {

    private final MemberMapper mapper;

    @Override
    public List<MemberDTO> memberList() throws Exception{
        return mapper.memberList();
    }

}
