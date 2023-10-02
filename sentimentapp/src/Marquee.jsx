import React from "react";
import "./marquee.css";
import Marquee from "react-fast-marquee";

const MarqueeComponent = () => {
  return (
    <div className="marquee-container">
      <Marquee>
        <ul class="marquee__inner">
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
          <li class="marquee__part">CSS Only Marquee •</li>
        </ul>
      </Marquee>
    </div>
    //   </div>
    //   <div class="marquee red">
    //     <ul class="marquee__inner">
    //       <li class="marquee__part">Another one •</li>
    //       <li class="marquee__part">Another one •</li>
    //       <li class="marquee__part">Another one •</li>
    //       <li class="marquee__part">Another one •</li>
    //       <li class="marquee__part">Another one •</li>
    //     </ul>
    //   </div>
    //   <div class="marquee green">
    //     <ul class="marquee__inner">
    //       <li class="marquee__part">Life is Roblox •</li>
    //       <li class="marquee__part">Life is Roblox •</li>
    //       <li class="marquee__part">Life is Roblox •</li>
    //       <li class="marquee__part">Life is Roblox •</li>
    //       <li class="marquee__part">Life is Roblox •</li>
    //     </ul>
    //   </div>
    // </div>
  );
};

export default MarqueeComponent;
