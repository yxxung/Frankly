package com.frankly.restapi.service;

import com.frankly.restapi.domain.NewsDTO;

import java.util.List;

public interface NewsServiceInterface {

    public List<NewsDTO> readNews(int politicianID) throws Exception;

    public void updateNews(int newsID) throws Exception;

    public void updateNewsKeyword(int newsKeywordID) throws Exception;

    public void deleteNews(int newsID) throws Exception;

    public void deleteNewsKeyword(int newsKeywordID) throws Exception;
}
