import React from "react";
import {Link} from "react-router-dom";

const EmptyPage = () => {

  return (
    <>
      <h3>해당 페이지를 찾지 못했습니다!</h3>
      <p>주소가 잘못되었거나 더 이상 제공되지 않는 페이지입니다.</p>
      <Link to="/">메인페이지로 이동</Link>
    </>
  )
};

export default EmptyPage