import React, { useEffect } from "react";
import { connect } from 'react-redux';
import { fetchLawmaker } from "../../redux";
import { Nav } from "../../components";

const Lawmaker = ({items, fetchLawmaker, loading}) => {
  useEffect(() => {
    fetchLawmaker()
  }, [])

  const lawmakerList = loading ? (<div>is loading...</div>) : (
    items.map(item => (
      <div key={item.id}>
        <h3>{item.name}</h3>
        <p>{item.email}</p>
        <p>{item.body}</p>
      </div>
    ))
  )

  return (
    <>
      <Nav />
      <div>
        <h1>국회의원 화면</h1>
        <h6>2020/06~2024/06</h6>
        <h2>대구 달서을</h2>
        <div>사진</div>
        <div>
          {lawmakerList}
        </div>
      </div>
    </>
  )
};
// state 값 불러오기
const mapStateToProps = (state) => {
  return {
    items: state.lawmaker.items
  }
}
// dispatch
const mapDispatchToProps = {
  fetchLawmaker
}

export default connect(mapStateToProps, mapDispatchToProps)(Lawmaker);