package com.frankly.restapi.controller;

import com.frankly.restapi.domain.NewsDTO;
import com.frankly.restapi.domain.NewsKeywordDTO;
import com.frankly.restapi.service.NewsService;
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
@RequestMapping("/api/news")
public class NewsController {

    private final NewsService newsService;

    //뉴스 키워드 보기
    @GetMapping("/{politicianID}")
    public ResponseEntity<List<NewsDTO>> readNews(@PathVariable("politicianID") int politicianID)
            throws Exception {
        log.info("readNews - politicianID : "+ politicianID);

        return new ResponseEntity<>(newsService.readNews(politicianID), HttpStatus.OK);
    }

    //뉴스 수정
    @PutMapping("/update")
    public ResponseEntity<NewsDTO> updateNews(@PathVariable("newsID") int newsID)
            throws Exception{
        log.info("update News");

        newsService.updateNews(newsID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //뉴스 키워드 수정
    @PutMapping("/update")
    public ResponseEntity<NewsKeywordDTO> updateNewsKeyword(@PathVariable("newsKeywordID") int newsKeywordID)
            throws Exception{
        log.info("update NewsKeyword");

        newsService.updateNewsKeyword(newsKeywordID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //뉴스 삭제
    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteNews(@PathVariable("newsID") int newsID)
            throws Exception{
        log.info("delete News : " + newsID);

        newsService.deleteNews(newsID);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //뉴스 키워드 삭제
    @DeleteMapping("/delete")
    public ResponseEntity<?>deleteNewsKeyword(@PathVariable("newsKeywordID") int newsKeywordID)
            throws Exception{
        log.info("delete NewsKeyword : " + newsKeywordID);

        newsService.deleteNewsKeyword(newsKeywordID);

        return new ResponseEntity<>(HttpStatus.OK);
    }
}

