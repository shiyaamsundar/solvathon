import React from "react";
import NewsCard from "./NewsCard";

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
  ];

  return (
    <div>
      {newsData.map((news, index) => (
        <NewsCard key={index} title={news.title} link={news.link} />
      ))}
    </div>
  );
};

export default NewsUpdate;
