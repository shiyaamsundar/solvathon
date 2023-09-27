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
    <>
      <div>ResultComponent</div>
      <div className="result-main-component">
        <ProgressBar now={50} label={`50% completed`} />
        <br></br>
        <ProgressBar now={70} label={`70% completed`} animated />
        <br></br>
        <ProgressBar now={30} label={`30% completed`} variant="success" />
        <div className="circle-bar">
          <CircularProgressbar value={80} text={`${80}%`} />;
          <CircularProgressbarWithChildren value={66}>
            {/* Put any JSX content in here that you'd like. It'll be vertically and horizonally centered. */}
            <img
              style={{ width: 40, marginTop: -5 }}
              src="https://i.imgur.com/b9NyUGm.png"
              alt="doge"
            />

            <div style={{ fontSize: 12, marginTop: -5 }}>
              <strong>66%</strong> mate
            </div>
          </CircularProgressbarWithChildren>
        </div>
      </div>
    </>
  );
};

export default ResultComponent;
