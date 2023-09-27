import React from "react";
import "./radioSelect.css";

const RadioSelect = () => {
  return (
    <>
      <div class="container">
        <ul class="list">
          <li class="list__item">
            <input type="radio" class="radio-btn" name="choice" id="a-opt" />
            <label for="a-opt" class="label">
              pick me!
            </label>
          </li>

          <li class="list__item">
            <input type="radio" class="radio-btn" name="choice" id="b-opt" />
            <label for="b-opt" class="label">
              pick me i'm better!
            </label>
          </li>

          <li class="list__item">
            <input type="radio" class="radio-btn" name="choice" id="c-opt" />
            <label for="c-opt" class="label">
              pick me i'm the best!
            </label>
          </li>

          <li class="list__item">
            <input type="radio" class="radio-btn" name="choice" id="d-opt" />
            <label for="d-opt" class="label">
              pick me i'm fabulous!
            </label>
          </li>
        </ul>
      </div>
    </>
  );
};

export default RadioSelect;
