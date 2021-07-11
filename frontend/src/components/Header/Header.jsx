import React, {useEffect, useState, memo} from "react";
import { useHistory } from "react-router-dom";

export const Header = memo((props) => {
  const [title, setTitle] = useState(props.title);
  // 뒤로가기 버튼
  const goBack = () => {
    props.history.goBack();
  }
  const goHome = () => {
    let history = useHistory();
    history.push("/");
  }

  return (
    <>
      <header className="header">
        <div className="header_container">
          {
            (() => {
              if (props.btn === "back") { // 뒤로가기
                return (
                  <>
                    <button className="leftBox" onClick={goBack}>
                      <span className="material-icons">arrow_back</span>
                    </button>
                    <div>
                      <h1>{title}</h1>
                    </div>
                  </>
                )
              } else if (props.btn === "home") { // 홈
                return (
                  <>
                    <button className="leftBox" onClick={goHome}>
                      <span className="material-icons">home</span>
                    </button>
                    <div>
                      <h1>{title}</h1>
                    </div>
                  </>
                )
              } else {
                return (
                  <h1 style={{marginLeft: "16px"}}>Frankly</h1>
                )
              }
            })()
          }
        </div>
      </header>
    </>
  )
});

// <Header btn="back" /> 일 경우 뒤로가기 버튼있는 Header
// <Header btn="home" /> 일 경우 홈 버튼있는 Header
// btn 값 추가 시 title 값도 추가해주어야 함
