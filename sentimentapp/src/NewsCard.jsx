import React from "react";
import "./newsCard.css"; // Import your CSS file for styling
import { ProgressBar } from "react-bootstrap";

const NewsCard = ({ data }) => {
  return (
  
    <div className="news-card">
      <span className="topic">{data.ArticleName}</span>
      <div className="news-title">{data?.Title}</div>
      <div className="news-title2">
      {data?.Description}
        <div className="news-sentiment">
          <div className="img-svg neu flex1">
            {data.Sentiment=='positive' && (
 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
 <path d="M12 1a11 11 0 1 0 11 11A11.013 11.013 0 0 0 12 1zm0 20a9 9 0 1 1 9-9 9.011 9.011 0 0 1-9 9zm6-8a6 6 0 0 1-12 0 1 1 0 0 1 2 0 4 4 0 0 0 8 0 1 1 0 0 1 2 0zM8 10V9a1 1 0 0 1 2 0v1a1 1 0 0 1-2 0zm6 0V9a1 1 0 0 1 2 0v1a1 1 0 0 1-2 0z" />
</svg>
            )}

{data.Sentiment=='negative' && (
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M10 9v2a1 1 0 0 1-2 0V9a1 1 0 0 1 2 0zm5-1a1 1 0 0 0-1 1v2a1 1 0 0 0 2 0V9a1 1 0 0 0-1-1zm8 4A11 11 0 1 1 12 1a11.013 11.013 0 0 1 11 11zm-2 0a9 9 0 1 0-9 9 9.01 9.01 0 0 0 9-9z" />
            </svg>
)}
{data.Sentiment=='neutral' &&(
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M8 11V9a1 1 0 0 1 2 0v2a1 1 0 0 1-2 0zm7 1a1 1 0 0 0 1-1V9a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1zm8 0A11 11 0 1 1 12 1a11.013 11.013 0 0 1 11 11zm-2 0a9 9 0 1 0-9 9 9.01 9.01 0 0 0 9-9zm-4 5a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1 4 4 0 0 1 4-4h2a4 4 0 0 1 4 4zm-2.269-1A2 2 0 0 0 13 15h-2a2 2 0 0 0-1.731 1z" />
          </svg>)}
         
        
          </div>
          <div className="flex2">
            <ProgressBar now={50} label={`50% completed`} variant="#5a6b60" />
          </div>
        </div>
      </div>


      <a href={data.Link} className="read-more-link" target="_blank">
        Read More
      </a>
    </div>
    
  );
};

export default NewsCard;
