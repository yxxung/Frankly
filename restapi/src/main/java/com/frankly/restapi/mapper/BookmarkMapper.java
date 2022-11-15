package com.frankly.restapi.mapper;

import com.frankly.restapi.domain.BookmarkDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface BookmarkMapper {

    public void createBookmark(BookmarkDTO bookmarkDTO) throws Exception;

    List<BookmarkDTO> readBookmark(int userID) throws Exception;

    public void deleteBookmark(BookmarkDTO bookmarkDTO) throws Exception;

}
