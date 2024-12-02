# Influencer Performance Analysis
This repository contains my solution to build a data-driven system for influencer selection based on video performance data. This system identifies unique influencers, calculates their average performance across multiple videos, and provides insights into which influencers consistently drive higher engagement.

Additionally, this project includes visualizations, regression analysis to predict future engagement, and an interactive dashboard to explore influencer data effectively.

## Task Breakdown:
Identify unique influencers appearing across ~200 videos.     
Calculate average performance for each influencer.      
Determine which influencers consistently drive better engagement based on their performance.

## Solution
This solution processes video data to:     
Detect unique influencers using facial recognition.     
Calculate their average performance based on performance scores across videos.      
Generate a report showing each influencer’s average performance and a representative image of them.

## Components
### Jupyter Notebook:

Contains the entire analysis workflow, including:    
Video data processing and unique influencer identification.    
Visualization of influencer engagement metrics.     
Regression analysis to predict future engagement based on historical performance data.     
The notebook is self-contained and offers detailed, step-by-step insights into the entire problem-solving approach.      

### Python Script for Dashboard:

Builds an interactive dashboard showcasing:     
The average performance of each uniquely identified influencer.     
Their representative face images extracted from the videos.      
The dashboard provides an intuitive way to explore influencer data and make informed decisions.     


## Features
__Face Recognition__: Detects and identifies influencers in videos using the face_recognition library.    
__Performance Calculation__: Calculates the average performance of each influencer across all videos.     
__Video Processing__: Downloads and processes videos to extract faces and performance metrics.      
__Report Generation__: Outputs a CSV report with the following:     
Influencer's average performance.     
Representative image of the influencer.     
Total number of videos the influencer appeared in.    
__Regression Analysis__: Models influencer engagement to help predict future performance.      
__Interactive Dashboard__: Enables dynamic exploration of influencer data, including representative images and average engagement metrics.     
__Performance Metrics__: Calculates and displays the average performance of influencers across all videos.    


## Conclusion
This solution provides a comprehensive analysis of influencer performance and an intuitive dashboard for decision-making. By combining visualizations, regression analysis, and interactivity, this project demonstrates a robust, end-to-end approach to solving the given problem statement.

