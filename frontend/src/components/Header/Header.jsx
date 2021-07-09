import React, {useEffect, useState, memo} from "react";
import { Link } from "react-router-dom";

const Header = memo((props) => {
  const [title, setTitle] = useState(props.title);
  const [btn, setBtn] = useState("");
  // 뒤로가기 버튼
  const goBack = () => {
    props.history.goBack();
  }

  const backBtn = () => {
    if (props.btn === "back") {
      return (
        <button className="leftBox" onClick={goBack}>
          <svg xmlns="http://www.w3.org/2000/svg" width="14.6" height="14.23" viewBox="0 0 14.6 14.23">
            <path
              d="M8.389,15.925l-.723.723a.779.779,0,0,1-1.1,0L.226,10.316a.779.779,0,0,1,0-1.1L6.561,2.877a.779.779,0,0,1,1.1,0l.723.723a.783.783,0,0,1-.013,1.118L4.449,8.459h9.365a.78.78,0,0,1,.782.782v1.043a.78.78,0,0,1-.782.782H4.449l3.927,3.741A.777.777,0,0,1,8.389,15.925Z"
              transform="translate(0.004 -2.647)"/>
          </svg>
        </button>
      )
    } else {
      return (
        <div style={{marginLeft: "16px"}}></div>
      )
    }
  }

  useEffect(() => {
    setBtn(backBtn);
  }, []);

  return (
    <>
      <header className="header">
        <div className="header_container">
          {btn}
          <div>
            <h1>{title}</h1>
          </div>
        </div>
      </header>
    </>
  )
});

export default Header