import React from "react";
import { Link } from "react-router-dom";

const Nav = () => {

  return (
    <>
      <Link to="/">홈</Link>
      <Link to="/community">게시판</Link>npm
      <Link to="/profile">내정보</Link>
    </>
  )
};

export default Nav
