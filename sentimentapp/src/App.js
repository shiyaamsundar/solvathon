import "./App.css";
import CsvUploader from "./Csvuploader";
import FileUpload from "./FileUpload";
import NewsUpdate from "./NewsUpdate";
import UserInputForm from "./UserInputForm";
import RadioSelect from "./RadioSelect";
import Marquee from "./Marquee";
import RadarChart from "./chart";
import ResultComponent from "./ResultComponent";
import FeedbackForm from "./FeedBack";
import Testimonials from "./Testmoni";
import Writeform from "./WriteForm";

function App() {
  return (
    <>
      <Marquee />

      <div className="main-div">
        <div>
          <RadioSelect />
          <UserInputForm />
          {/* <FileUpload /> */}
          <Testimonials />
          <FeedbackForm />
          <Writeform />
        </div>
        <div className="news">
          <NewsUpdate />
        </div>
      </div>
    </>
    // <div className="container">
    //   <div>
    //     <UserInputForm />
    //   </div>
    //   <div className="news">
    //     <NewsUpdate />
    //   </div>

    //   {/* <Marquee />
    //   <h1>Hello World</h1>
    //   <ResultComponent /> */}
    //   {/* <CsvUploader /> */}
    //   {/* <RadioSelect /> */}

    //   {/* <FileUpload /> */}
    // </div>
  );
}

export default App;
