import React, { useRef } from "react";
import "./userInput.css";
import FileUpload from "./FileUpload";

const UserInputForm = ({input}) => {
  const form = useRef();

  console.log(input)

  return (
    <div className="select-wrapper">
      <form ref={form}>

        {input=='url' && (<input
          type="text"
          className="select-dropdown"
          placeholder="Paste your url here"
        />)}


        
          {input && (
 <select name="format" id="format" className="select-dropdown">
 <option selected disabled>
   Choose a book format
 </option>
 <li role="option">...</li>
 <li role="option">...</li>
 <option value="pdf">PDF</option>
 <option value="txt">txt</option>
 <option value="epub">ePub</option>
 <option value="fb2">fb2</option>
 <option value="mobi">mobi</option>
</select>
          )}

          {input=='text' && (
 <textarea
 type="text"
 className="select-dropdown"
 placeholder="Paste your content here"
 rows="4"
 cols="50"
/>
          )}


            {input=='pdf' && (
              <div className="pdf-upload">

              <FileUpload/>
              </div>
            )}

          <div className="submit-btn">
       
       {input && (
          <button className="user-sumbit-btn">submit</button>
       )}
       </div>



        <div>

        </div>
      </form>
    </div>
  );
};

export default UserInputForm;
