package com.frankly.restapi.service;

import com.frankly.restapi.domain.ReplyDTO;
import com.frankly.restapi.mapper.ReplyMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.sql.SQLException;
import java.util.List;

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
    public ReplyDTO getReply(int replyID) throws Exception {
        return replyMapper.getReply(replyID);
    }

    @Override
    public List<ReplyDTO> countReply(int boardID) throws Exception {
        return replyMapper.countReply(boardID);
    }

    @Override
    public void updateReply(ReplyDTO replyDTO, int replyID) throws Exception {

        ReplyDTO targetReply = replyMapper.getReply(replyID);
        if(targetReply.getUserID() == (replyDTO.getUserID())){
            try{
                replyDTO.setReplyID(replyID);
                replyMapper.updateReply(replyDTO);
            }catch(SQLException e){
                System.out.println(e);
                e.printStackTrace();
            }

        }else{
            throw new Exception("author is different - "+targetReply.getUserID()+" and "+replyDTO.getUserID());
        }
    }

    @Override
    public void deleteReply(ReplyDTO replyDTO) throws Exception {
        replyMapper.deleteReply(replyDTO);
    }

}
