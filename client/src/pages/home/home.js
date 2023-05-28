import React, { useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./home.css";

import { Link } from "react-router-dom";
import { useState } from "react";

//var cloths = require('./black.json')
import cloths from "./black.json";
import axios from "axios";

function Home(props) {
  const [data, setData] = useState([]);
  const [selected, setSelected] = useState([]);
  const [sub, setSub] = useState([]);
  const [Arr, setArr] = useState([]);
  const [reload, setReload] = useState(false);
  const [res, setres] = useState();
  // retrive values from json file

  useEffect(() => {
    (async () => {
      if (data.length == 0) {
        const arr = Array.from({ length: 4 }, () =>
          Math.floor(Math.random() * cloths.length)
        );
        setData(arr);
      } else {
        setData(Arr);
        const arr = Array.from({ length: 4 - data.length }, () =>
          Math.floor(Math.random() * cloths.length)
        );
        setData((dat) => [...dat, ...arr]);
      }
    })();

    return () => {};
  }, [reload]);

  const handleInput1 = async (e) => {
    await setSelected((dat) => [...dat, e.target.value]);

    await setArr((dat) => [...dat, e.target.value - 1]);
  };

  const handleInput2 = async (e) => {
    await setSub((dat) => [...dat, e.target.value]);
  };

  const handlesubmit = async (e) => {
    //e.preventDefault()
    //await setSelected(dat=>[...dat,e.target.value])
    //await  setSub(dat=>[...dat,e.target.value])
    await console.log(selected);

    await console.log(sub);
    setReload((prev) => !prev);
    //alert("heloo")
  alert(dress:JSON.stringify(selected));
  };

  axios
    .post("/api/", {
      dress:JSON.stringify(selected),
    })
    .then(function (response) {
      console.log(response);
      setres(response);
    })
    .catch(function (error) {
      console.log(error);
    });

  return (
    <div>
      <form>
        <Container>
          <Row>
            {data.map((item) => {
              return (
                <Col>
                  <img src={cloths[item].path} className="image" />
                  <br />
                  <input
                    type="radio"
                    name={cloths[item].id}
                    value={cloths[item].id}
                    onChange={(e) => handleInput1(e)}
                  />
                </Col>
              );
            })}
          </Row>
          {/* dropdown button
           */}
          <Row>
            <Col>
              <input
                type="radio"
                name="cat"
                value="0"
                onSubmit={(e) => handlesubmit(e)}
              />
              <label for="cat">Casual</label>

              <input
                type="radio"
                name="cat"
                value="1"
                onSubmit={(e) => handlesubmit(e)}
              />
              <label for="cat">Formal</label>
            </Col>
          </Row>
        </Container>
        <button onClick={(e) => handlesubmit(e)}>Submit</button>
      </form>
      <Container>
        {res.map((item) => {
          return (
            <Row>
              <Col>
                <img src={item.path} className="image" />
              </Col>
            </Row>
          );
        })}
      </Container>
    </div>
  );
}

export default Home;
