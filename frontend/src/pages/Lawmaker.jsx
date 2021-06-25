import React, {useState, useCallback, useEffect} from "react";
import { useParams } from "react-router-dom";
import Axios from "axios";

const Lawmaker = () => {
  const [loading, setLoading]  = useState(true);
  const [list, setList] = useState([]);

  useEffect(() => {
    Axios.get('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        setList(response.data);
        setLoading(false);
      })
  }, []);

  console.log(list);

  return (
    <>
      {loading ? ("loading...") : (
        <div>
          <h6>2020/06~2024/06</h6>
          <h2>대구 달서을</h2>
          <div>사진</div>
          <h3>{list[0].name}</h3>
          <h4>{list[0].id}</h4>
          <div>
            <p>{list[0].email}</p>
            <p>{list[0].phone}</p>
          </div>
        </div>
      )}
    </>
  )
};

export default Lawmaker