import React, { useState } from "react";
import NewsCard from "./NewsCard";
import { useEffect } from "react";
import axios from "axios";

const NewsUpdate = () => {
  const newsData = [
    {
      title:
        "News Headline 1 Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, quam.  ",
      link: "https://example.com/news1",
    },
    {
      title:
        "News Headline 2   Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ad unde fuga praesentium illum excepturi alias officiis sed facere voluptas eaque.",
      link: "https://example.com/news2",
    },
    {
      title:
        "News Headline 3    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione voluptates fugit ab rerum cupiditate necessitatibus minima magnam, blanditiis temporibus, tempora ea voluptas, nihil illo nesciunt.",
      link: "https://example.com/news3",
    },
    {
      title:
        "News Headline 1 Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, quam.  ",
      link: "https://example.com/news1",
    },
    {
      title:
        "News Headline 2   Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ad unde fuga praesentium illum excepturi alias officiis sed facere voluptas eaque.",
      link: "https://example.com/news2",
    },
    {
      title:
        "News Headline 3    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione voluptates fugit ab rerum cupiditate necessitatibus minima magnam, blanditiis temporibus, tempora ea voluptas, nihil illo nesciunt.",
      link: "https://example.com/news3",
    },
  ];

  const [recentNews, setrecentNews] = useState([])

  useEffect(async() => {
    const res=await axios.get('http://127.0.0.1:8000/api/recentnews')
    setrecentNews(res?.data)
  }, [])
  


  return (
    <div>
      {recentNews?.map((data) => (
        <NewsCard key={data.Link} data={data} />
      ))}
    </div>
  );
};

export default NewsUpdate;
