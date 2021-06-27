package com.frankly.restapi.service;

import com.frankly.restapi.domain.MemberDTO;

import java.util.List;

public interface MemberServiceInterface {

    public List<MemberDTO> memberList() throws Exception;
}
