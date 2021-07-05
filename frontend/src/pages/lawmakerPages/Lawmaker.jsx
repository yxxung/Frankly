import React, { useEffect } from "react";
import { connect } from 'react-redux';
import { fetchLawmaker } from "../../redux";
import { Nav, Header } from "../../components";

const Lawmaker = ({items, fetchLawmaker, loading}) => {

  useEffect(() => {
    fetchLawmaker(1)
  }, [])

  const lawmakerList = loading ? (<div>is loading...</div>) : (
    <div key={1}>
      <h6>2020/06~2024/06</h6>
      <h2>{items.district}</h2>
      <div>사진</div>
      <h3>{items.name}</h3>
      <p>{items.hanName}</p>
      <p>{items.engName}</p>
      <p>{items.birthday}</p>
      <p>{items.selectNumber}</p>
      <p>{items.contact}</p>
      <p>{items.email}</p>
      <p>사무실 : {items.office}</p>
    </div>
  )

  return (
    <>
      <Header />
      <Nav />
      <div>
        {lawmakerList}
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