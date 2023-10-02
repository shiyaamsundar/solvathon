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
        <div>ResultComponent</div>
        <ProgressBar now={50} label={`50% completed`} />
        <br></br>

        {/* <br></br>
        <ProgressBar now={30} label={`30% completed`} variant="success" /> */}
        <p className="result-percent">90%</p>
        </div>
        <div className="img-container">
          <h4>Word Cloud Image</h4>
        </div>
        {/* <div className="circle-bar">
          <CircularProgressbar value={80} text={`${80}%`} />;
         
        </div> */}
      </div>
    </div>
  );
};

export default ResultComponent;
