import React, { useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { fetchLawmaker } from "../../redux";
import { Nav, Header } from "../../components";

const Lawmaker = () => {
  const items = useSelector(store => store.lawmaker.items);
  const loading = useSelector(store => store.lawmaker.loading);
  const dispatch = useDispatch();

  useEffect(() => {
    // 로그인 되어있으면 유저 정보에서 지역 값
    // 로그아웃이면 기본 값
    dispatch(fetchLawmaker(1));
  }, [])

  const changeLawmaker = () => {
    // 지역구 변경
  }

  const lawmakerList = loading ? (<div>is loading...</div>) : (
    <div key={1}>
      <h6>2020/06~2024/06</h6>
      <h1>{items.district}</h1>
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
    <div className="contents">
      {/*처음 로딩시 지역이름 안뜨는 문제*/}
      <Header />
      <Nav />
      <div className="lawmaker">
        {lawmakerList}
      </div>
    </div>
  )
};

export default Lawmaker;