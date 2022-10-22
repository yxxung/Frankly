package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.NewsDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface NewsMapper {

    public List<NewsDTO> readNews(int politicianID) throws Exception;

    public void updateNews(int newsID) throws Exception;

    public void updateNewsKeyword(int newsKeywordID) throws Exception;

    public void deleteNews(int newsID) throws Exception;

    public void deleteNewsKeyword(int newsKeywordID) throws Exception;


}