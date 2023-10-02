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
import Header from "./Header";

function App() {
  return (
    <>
    <Header/>
      <Marquee />

      <div className="main-div">
        <div>
          <RadioSelect />
       
          {/* <FileUpload /> */}
          <ResultComponent/>
        
        
        </div>
        <div className="news">
    <h1>Code</h1>
          <NewsUpdate />
        </div>
        
      </div>
      <div className="tertimonial">
      <Testimonials />
      <FeedbackForm />
          <Writeform />
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
