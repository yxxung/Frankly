import React, { useState } from "react";
import { connect } from "react-redux";
import { addSubscriber, addView } from "../../redux";
import { Nav } from "../../components";

const Community = ({ count, view, addSubscriber, addView }) => {
  const [number, setNumber] = useState(1)

  const viewChange = (e) => {
    setNumber(e.target.value);
  }

  return (
    <>
      <Nav />
      <h1>게시판 화면</h1>
      <p>구독자 수 : {count}</p>
      <p>조회 수 : {view}</p>
      <button onClick={() => addSubscriber()}>구독</button>
      <div>
        <input type="text" value={number} onChange={viewChange}/>
        <button onClick={() => addView(number)}>조회</button>
      </div>
    </>
  )
};
// state 값 불러오기
const mapStateToProps = ({ subscribers }) => {
  return {
    count: subscribers.count,
    view: subscribers.view,
  }
}
// dispatch
const mapDispatchToProps = {
  addSubscriber,
  addView: (number) => addView(number)
}

export default connect(mapStateToProps, mapDispatchToProps)(Community);