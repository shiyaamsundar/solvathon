import React from "react";
import "./radioSelect.css";
import UserInputForm from "./UserInputForm";
import { useState } from "react";

const RadioSelect = () => {
  const [selectedInput, setselectedInput] = useState(null)


 


  return (
    
      <div className="container">
        <div>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Temporibus eveniet cupiditate debitis fugiat totam consequuntur corrupti, corporis commodi. Quo neque libero architecto atque impedit voluptatum ut quidem, facere voluptatibus corrupti!
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores ut eligendi, quod quaerat nemo quisquam. Sint ratione sapiente omnis? Est ullam reiciendis ea numquam deserunt non dolorem porro. Veritatis.
        </div>
        <div className="radio-select">
        <ul class="list">
          <li class="list__item" onClick={()=>setselectedInput("url")}>
            <input type="radio" class="radio-btn" name="choice" id="a-opt" />
            <label for="a-opt" class="label" >
              Provide NewsAtricles Url
            </label>
          </li>

          <li class="list__item" onClick={()=>setselectedInput("text")}>
            <input type="radio" class="radio-btn" name="choice" id="b-opt" />
            <label for="b-opt" class="label" >
              Provide the whole text
            </label>
          </li>


          <li class="list__item" onClick={()=>setselectedInput("ticker")}>
            <input type="radio" class="radio-btn" name="choice" id="c-opt" />
            <label for="c-opt" class="label">
              Just Select Company ticket
            </label>
          </li>

          <li class="list__item" onClick={()=>setselectedInput("pdf")}>
            <input type="radio" class="radio-btn" name="choice" id="d-opt" />
            <label for="d-opt" class="label">
             Upload Any File 
            </label>
          </li>
        </ul>
        <UserInputForm input={selectedInput}/>
        </div>
        
      </div>
  );
};

export default RadioSelect;
