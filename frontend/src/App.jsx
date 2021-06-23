import React, {useState, useCallback, useEffect} from "react";
import Axios from "axios";

const App = () => {
  const [district, setDistrict]  = useState('대구 달서을');
  const [name, setName] = useState('');
  const [party, setParty] = useState('');
  const [email, setEmail] = useState('');
  const [birth, setBirth] = useState('');
  const [phone, setPhone] = useState('');

  useEffect(() => {
    Axios.get('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        setName(response.data[0].name)
        setParty(response.data[0].username)
        setEmail(response.data[0].email)
        setBirth(response.data[0].address.street)
        setPhone(response.data[0].address.zipcode)
      })
  })
  // 로그인 여부 체크
  // if 로그인 -> 지역 체크 -> 지역 번호 데이터 요청 -> 받고 화면 뿌려주기(?)
  // else 로그아웃 -> 기본값 (서울 송파구을 배현진ㅋ) 요청 -> 받고 화면 뿌려주기

  return (
    <>

      <div>
        <h6>2020/06~2024/06</h6>
        <h2>{district}</h2>
        <div>사진</div>
        <h3>{name}</h3>
        <h4>{party}</h4>
        <div>
          <p>{email}</p>
          <p>{birth}</p>
          <p>{phone}</p>
        </div>
      </div>

      <div>
        <a href="#">홈</a>
        <a href="#">게시판</a>
        <a href="#">내정보</a>
      </div>

    </>
  )
};

export default App