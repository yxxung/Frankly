package com.frankly.restapi.service;

import com.frankly.restapi.domain.BoardDTO;
import com.frankly.restapi.domain.ReplyDTO;
import com.frankly.restapi.mapper.BoardMapper;
import com.frankly.restapi.mapper.ReplyMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.TimeZone;

@Service
@Slf4j
@RequiredArgsConstructor
public class ReplyService implements ReplyServiceInterface {

    private final ReplyMapper replyMapper;

    @Override
    public void createReply(ReplyDTO replyDTO) throws Exception {
        replyMapper.createReply(replyDTO);
    }

    @Override
    public List<ReplyDTO> readReply(int boardID) throws Exception {
        log.info("getReplyList");
        return replyMapper.readReply(boardID);
    }

    @Override
    public void updateReply(ReplyDTO replyDTO) throws Exception {
        replyMapper.updateReply(replyDTO);
    }

    @Override
    public void deleteReply(ReplyDTO replyDTO) throws Exception {
        replyMapper.deleteReply(replyDTO);
    }


}
