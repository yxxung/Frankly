import React, { memo } from "react";
import { NavLink } from "react-router-dom";

export const Nav = memo(() => {

  return (
    <>
      <nav className="bottom_nav">
        <div className="bottom_nav_area">
          <NavLink exact to="/" activeClassName="selected">
            <span className="material-icons">home</span>
            <p>홈</p>
          </NavLink>
          <NavLink to="/community" activeClassName="selected">
            <span className="material-icons">format_list_bulleted</span>
            <p>커뮤니티</p>
          </NavLink>
          <NavLink to="/profile" activeClassName="selected">
            <span className="material-icons">account_circle</span>
            <p>내 정보</p>
          </NavLink>
        </div>
      </nav>
    </>
  )
});
