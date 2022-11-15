package com.frankly.restapi.service;

import com.frankly.restapi.domain.BookmarkDTO;
import com.frankly.restapi.mapper.BookmarkMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
@Slf4j
@RequiredArgsConstructor
public class BookmarkService implements BookmarkServiceInterface{

    private final BookmarkMapper bookmarkMapper;

    @Override
    public void createBookmark(BookmarkDTO bookmarkDTO) throws Exception{
        bookmarkMapper.createBookmark(bookmarkDTO);
    }

    @Override
    public List<BookmarkDTO> readBookmark(int userID) throws Exception {
        return bookmarkMapper.readBookmark(userID);
    }
    @Override
    public void deleteBookmark(BookmarkDTO bookmarkDTO) throws Exception{
        bookmarkMapper.deleteBookmark(bookmarkDTO);

    }

}
