import React from "react";
import { ProgressBar } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "./resultComponent.css";
import {
  CircularProgressbar,
  CircularProgressbarWithChildren,
} from "react-circular-progressbar";

import "react-circular-progressbar/dist/styles.css";

const ResultComponent = () => {
  return (
    <div className="result-wrapper">

      <div className="result-main-component">
        <div>
        <div className="result-heading">Result And Confidence Scores </div>
        <br></br>
        <div className="result-sub-container"> 
        <h4>model result</h4>
        <div>
          
        <p className="result-percent">Positive <span> 90%</span></p>
        <p className="result-percent">Negative <span>90%</span></p>
        </div>
       </div>
       
        </div>
        <div className="img-container">
        
          {/* <img src="../../reviewWordCloud.png" alt="" /> */}
        </div>
        {/* <div className="circle-bar">
          <CircularProgressbar value={80} text={`${80}%`} />;
         
        </div> */}
      </div>
    </div>
  );
};

export default ResultComponent;
