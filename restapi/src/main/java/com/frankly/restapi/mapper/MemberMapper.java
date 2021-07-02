package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.MemberDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

/**
 * @author 최제현
 * @date 2021/06/25
 * mybatis 프레임워크
 * Member mapper interface
 */

@Mapper
public interface MemberMapper {

    public void createMember(MemberDTO member) throws Exception;

    public MemberDTO readMember(Long id) throws Exception;

    public void updateMember(MemberDTO member) throws Exception;

    public void deleteMember(MemberDTO member) throws Exception;

    public List<MemberDTO> memberList() throws Exception;
}
