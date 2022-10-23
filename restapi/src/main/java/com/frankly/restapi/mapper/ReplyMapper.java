package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.ReplyDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface ReplyMapper {


    public void createReply(ReplyDTO replyDTO) throws Exception;

    public List<ReplyDTO> readReply(int boardID) throws Exception;

    public List<ReplyDTO> countReply(int boardID) throws Exception;

    public void updateReply(ReplyDTO replyDTO) throws Exception;

    public void deleteReply(ReplyDTO replyDTO)throws Exception;


}
