import React, { useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { fetchLawmaker } from "../../redux";
import { Nav, Header } from "../../components";

const Lawmaker = () => {
  const items = useSelector(store => store.lawmaker.items);
  const loading = useSelector(store => store.lawmaker.loading);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchLawmaker(1));
  }, [])

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