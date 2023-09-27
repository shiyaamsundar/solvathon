import React from "react";
import { Radar } from "react-chartjs-2";

const RadarChart = () => {
  const data = {
    labels: ["Category A", "Category B", "Category C"],
    datasets: [
      {
        data: [0.6, 0.8, 0.7], // Replace with your data
        backgroundColor: [
          "rgba(75, 192, 192, 0.6)",
          "rgba(255, 99, 132, 0.6)",
          "rgba(54, 162, 235, 0.6)",
        ],
        borderColor: [
          "rgba(75, 192, 192, 1)",
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
        ],
        borderWidth: 2,
      },
    ],
  };

  const options = {
    scale: {
      ticks: {
        beginAtZero: true,
        max: 1, // Set your max value as needed
      },
    },
  };

  return (
    <div className="radar-chart">
      <Radar data={data} options={options} />
    </div>
  );
};

export default RadarChart;
