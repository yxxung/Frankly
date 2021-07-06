import React from "react";
import { NavLink, useParams } from "react-router-dom";

const Nav = () => {

  return (
    <>
      <nav className="bottom_nav">
        <div className="bottom_nav_area">
          <NavLink exact to="/" activeClassName="selected">
            <p>홈</p>
          </NavLink>
          <NavLink to="/community" activeClassName="selected">
            <p>게시판</p>
          </NavLink>
          <NavLink to="/profile" activeClassName="selected">
            <p>내 정보</p>
          </NavLink>
        </div>
      </nav>
    </>
  )
};

export default Nav