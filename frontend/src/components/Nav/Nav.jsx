import React from "react";
import { Link } from "react-router-dom";

const Nav = () => {

  return (
    <>
      <nav className="bottom_nav">
        <div className="bottom_nav_area">
          <Link to="/">
            <p>홈</p>
          </Link>
          <Link to="/community">
            <p>게시판</p>
          </Link>
          <Link to="/profile">
            <p>내 정보</p>
          </Link>
        </div>
      </nav>
    </>
  )
};

export default Nav