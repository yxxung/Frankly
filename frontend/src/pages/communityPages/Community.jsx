import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addSubscriber, addView } from "../../redux";
import {Header, Nav} from "../../components";

const Community = () => {
  const [number, setNumber] = useState(1)

  const count = useSelector(state => state.community.count);
  const view = useSelector(state => state.community.view);
  const dispatch = useDispatch();

  const viewChange = (e) => {
    setNumber(Number(e.target.value));
  }

  return (
    <div className="contents">
      <Header />
      <Nav />
      <h1>게시판 화면</h1>
      <p>구독자 수 : {count}</p>
      <p>조회 수 : {view}</p>
      <button onClick={() => dispatch(addSubscriber())}>구독</button>
      <div>
        <input type="text" value={number} onChange={viewChange}/>
        <button onClick={() => dispatch(addView(number))}>조회</button>
      </div>
    </div>
  )
};

export default Community;