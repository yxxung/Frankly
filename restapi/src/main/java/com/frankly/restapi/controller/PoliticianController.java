package com.frankly.restapi.controller;

import com.frankly.restapi.domain.BookmarkDTO;
import com.frankly.restapi.domain.PageVO;
import com.frankly.restapi.domain.PoliticianDTO;
import com.frankly.restapi.service.BookmarkService;
import com.frankly.restapi.service.PoliticianService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@Slf4j
@RequiredArgsConstructor
@RestController
@RequestMapping("/api/politician")
public class PoliticianController {

    private final PoliticianService politicianService;

    private final BookmarkService bookmarkService;

    //국회의원 상세페이지 + 조회수증가
    @GetMapping("/{politicianID}")
    public ResponseEntity<PoliticianDTO> getPoliticianById(@PathVariable("politicianID")int politicianID) throws Exception{

        politicianService.countView(politicianID);

        return new ResponseEntity<>(politicianService.getPoliticianById(politicianID), HttpStatus.OK);

    }

    //정당 내 국회의원
    @GetMapping("/party/{partyID}")
    public ResponseEntity<List<PoliticianDTO>> readParty(@PathVariable("partyID")int partyID) throws Exception{

        return new ResponseEntity<>(politicianService.readParty(partyID), HttpStatus.OK);
    }

    //전체 국회의원
    @GetMapping("/all")
    public ResponseEntity<List<PoliticianDTO>>politicianList()throws Exception{

        return new ResponseEntity<>(politicianService.politicianList(), HttpStatus.OK);
    }

    //국회의원 검색
    @GetMapping("/search")
    public ResponseEntity<List<PoliticianDTO>>searchPolitician(@RequestParam(value = "searchName", required = true, defaultValue = "") String searchName)throws Exception{
        PageVO pageVO = new PageVO();

        pageVO.setSearchName(searchName);
        return new ResponseEntity<>(politicianService.searchPolitician(searchName), HttpStatus.OK);
    }

    //국회의원 상세 페이지 클릭순
    @GetMapping("/rank")
    public ResponseEntity<List<PoliticianDTO>>viewRank()throws Exception{

        return new ResponseEntity<>(politicianService.viewRank(), HttpStatus.OK);
    }

    //북마크 누르기
    @PostMapping("/create/bookmark")
    public ResponseEntity<BookmarkDTO> createBookmark(@Validated @RequestBody BookmarkDTO bookmarkDTO) throws Exception {

        bookmarkService.createBookmark(bookmarkDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

    //북마크 취소
    @DeleteMapping("/delete/bookmark")
    public ResponseEntity<BookmarkDTO> deleteBookmark(@Validated @RequestBody BookmarkDTO bookmarkDTO) throws Exception {

        bookmarkService.deleteBookmark(bookmarkDTO);

        return new ResponseEntity<>(HttpStatus.OK);
    }

}
