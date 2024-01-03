import "./App.css";

import { useEffect, useState } from "react";
import Navbar from "./header/Navbar";
import Header from "./header/Header";
import NewsFeed from "./Main/NewsFeed/NewsFeed";


function App() {

  return (
    <>
    <Navbar/>
    <Header/>
    <NewsFeed/>
    </>
  );
}

export default App;
