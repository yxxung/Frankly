import React, {useState, useCallback, useEffect} from "react";
import { connect } from 'react-redux'

// components
import Nav from "../components/Nav/Nav";

const Lawmaker = (props) => {

  console.log(props);

  return (
    <>
      <Nav />
      <div>
        <h6>2020/06~2024/06</h6>
        <h2>대구 달서을</h2>
        <div>사진</div>
        <h3>{props.list[0].name}</h3>
        <h4>{props.list[0].id}</h4>
        <div>
          <p>{props.list[0].email}</p>
          <p>{props.list[0].phone}</p>
        </div>
      </div>
    </>
  )
};

export default connect()(Lawmaker);