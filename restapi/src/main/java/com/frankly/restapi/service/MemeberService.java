package com.frankly.restapi.service;

import com.frankly.restapi.domain.MemberDTO;
import com.frankly.restapi.mapper.MemberMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor
@Service
@Slf4j
public class MemeberService implements MemberServiceInterface {

    private final MemberMapper mapper;

    @Override
    public List<MemberDTO> memberList() throws Exception{
        log.info("getList");
        return mapper.memberList();
    }

}
