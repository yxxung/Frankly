package com.frankly.restapi.controller;

import com.frankly.restapi.domain.BookmarkDTO;
import com.frankly.restapi.domain.LikeDTO;
import com.frankly.restapi.service.BookmarkService;
import com.frankly.restapi.service.LikeService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@Slf4j
@CrossOrigin
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/likeBookmark")

public class LikeBookmarkController {

    private final LikeService likeService;

    private final BookmarkService bookmarkService;

    //좋아요 한 게시물 목록
    @GetMapping("/like/{userID}")
    public ResponseEntity<List<LikeDTO>> readLike(@PathVariable("userID") int userID)
            throws Exception {
        log.info("readLike - userID : "+ userID);

        return new ResponseEntity<>(likeService.readLike(userID), HttpStatus.OK);
    }

    //북마크 한 국회의원 목록
    @GetMapping("/bookmark/{userID}")
    public ResponseEntity<List<BookmarkDTO>> readBookmark(@PathVariable("userID") int userID)
            throws Exception {
        log.info("readBookmark - userID : "+ userID);

        return new ResponseEntity<>(bookmarkService.readBookmark(userID), HttpStatus.OK);
    }

}

