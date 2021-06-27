import React, {useState, useCallback, useEffect} from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import Nav from "../components/Nav";

const Lawmaker = (props) => {
  // APP 에서 데이터 받아와야함 props 로 데이터 내려주는 방식으로 / app 의 장점이 데이터를 처음에 다 받아오는건데 페이지 옮길때마다 로딩하면 안좋지않을까?
  console.log(props);

  return (
    <>
      <div>
        <h6>2020/06~2024/06</h6>
        <h2>대구 달서을</h2>
        <div>사진</div>
        <h3>{props.list[0].name}</h3>
        <h4>{props.list[0].id}</h4>
        <div>
          <p>{props.list[0].email}</p>
          <p>{props.list[0].phone}</p>
        </div>
      </div>

      <Nav />
    </>
  )
};

export default Lawmaker;