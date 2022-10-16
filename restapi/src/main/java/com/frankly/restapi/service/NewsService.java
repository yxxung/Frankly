package com.frankly.restapi.service;

import com.frankly.restapi.domain.NewsDTO;
import com.frankly.restapi.mapper.NewsMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class NewsService implements NewsServiceInterface{

    private final NewsMapper newsMapper;

    @Override
    public List<NewsDTO> readNews(int politicianID) throws Exception {
        return newsMapper.readNews(politicianID);
    }

    @Override
    public void updateNews(int newsID) throws Exception {
        newsMapper.updateNews(newsID);
    }

    @Override
    public void updateNewsKeyword(int newsKeywordID) throws Exception {
        newsMapper.updateNewsKeyword(newsKeywordID);
    }

    @Override
    public void deleteNews(int newsID) throws Exception {
        newsMapper.deleteNews(newsID);
    }

    @Override
    public void deleteNewsKeyword(int newsKeywordID) throws Exception {
        newsMapper.deleteNewsKeyword(newsKeywordID);
    }
}
