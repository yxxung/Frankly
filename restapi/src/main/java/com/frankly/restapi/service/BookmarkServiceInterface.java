package com.frankly.restapi.service;

import com.frankly.restapi.domain.BookmarkDTO;

import java.util.List;

public interface BookmarkServiceInterface {

    public void createBookmark(BookmarkDTO bookmarkDTO) throws Exception;

    List<BookmarkDTO> readBookmark(int userID) throws Exception;

    public void deleteBookmark(BookmarkDTO bookmarkDTO) throws Exception;
}
