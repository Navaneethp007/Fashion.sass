import React, { useEffect } from 'react';
import { Container,Row,Col } from 'react-bootstrap';
import './home.css';

import { Link } from 'react-router-dom';
import { useState } from 'react';
 
//var cloths = require('./black.json')
import cloths from './black.json'



function Home(props) {
    const [data,setData] = useState([])
    const [selected,setSelected] = useState([])
    const [sub,setSub] = useState([])
    // retrive values from json file
  
    useEffect(() => {
      (async()=>{
          

        const arr=  Array.from({length:4},()=>Math.floor(Math.random()*cloths.length))
        setData(arr)
          
      })();

      return(()=>{

      })
      
    },
    []);

    const handleInput1=async(e)=>{
      await setSelected(dat=>[...dat,e.target.value])
    }

    const handleInput2=async(e)=>{
      await setSub(dat=>[...dat,e.target.value]);
    }

    const handlesubmit=async(e)=>{
      //e.preventDefault()
     //await setSelected(dat=>[...dat,e.target.value])
      //await  setSub(dat=>[...dat,e.target.value])
      await console.log(selected)

      await console.log(sub)
      alert("heloo")
    }



    
 

    
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
          <button type="submit" onClick={(e) => handlesubmit(e)}>
            Submit
          </button>
        </form>
      </div>
    );
}

export default Home;