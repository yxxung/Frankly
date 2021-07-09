import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addSubscriber, addView } from "../../redux";
import { Nav } from "../../components";

const Community = () => {
  const [number, setNumber] = useState(1)

  const count = useSelector(state => state.subscribers.count);
  const view = useSelector(state => state.subscribers.view);
  const dispatch = useDispatch();

  const viewChange = (e) => {
    setNumber(Number(e.target.value));
  }

  return (
    <>
      <Nav />
      <h1>게시판 화면</h1>
      <p>구독자 수 : {count}</p>
      <p>조회 수 : {view}</p>
      <button onClick={() => dispatch(addSubscriber())}>구독</button>
      <div>
        <input type="text" value={number} onChange={viewChange}/>
        <button onClick={() => dispatch(addView(number))}>조회</button>
      </div>
    </>
  )
};

export default Community;