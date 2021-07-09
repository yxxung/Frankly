import React, { memo } from "react";
import { NavLink } from "react-router-dom";
import styles from "./Nav.module.scss";

const Nav = memo(() => {

  return (
    <>
      <nav className={styles.bottom_nav}>
        <div className={styles.bottom_nav_area}>
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
});

export default Nav