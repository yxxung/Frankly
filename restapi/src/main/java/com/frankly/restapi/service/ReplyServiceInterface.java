package com.frankly.restapi.service;

import com.frankly.restapi.domain.ReplyDTO;

import java.util.List;


public interface ReplyServiceInterface {



    public void createReply(ReplyDTO replyDTO) throws Exception;

    public List<ReplyDTO> readReply(int boardID) throws Exception;

    public List<ReplyDTO> countReply(int boardID) throws Exception;

    public void updateReply(ReplyDTO replyDTO) throws Exception;

    public void deleteReply(ReplyDTO replyDTO) throws Exception;


}
