package com.frankly.restapi.domain;

/**
 * 쿼리에 들어갈 파라미터를 넣을 클래스.
 */
public class CriteriaVO {
    private long page;
    private int pageNum;

    public long getPageStart(){
        return (this.page-1)*pageNum;
    }

    public CriteriaVO(){
        this.page = 1;
        this.pageNum = 10;
    }

    public void setPage(long page){
        if(page <= 0){
            this.page = 1;
        }else{
            this.page = page;
        }
    }

    public int getPageNum(){
        return pageNum;
    }

    public void setPageNum(int pageCount){
        int count = this.pageNum;
        if(pageCount != count){
            this.pageNum = count;
        }else{
            this.pageNum = pageCount;
        }
    }
}
