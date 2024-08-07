# Analyzing the Time Trends of Logan Webb’s Performance

## Authors
- Jackson Sousa
- Samuel Glick
- Yinkun Tang
- Cameron Zaidi

## Date
June 11, 2024

## Abstract
This project investigates the MLB pitcher Logan Webb from 2019-2024 to understand his overall improved pitching performance. Key metrics such as velocity and pitch location over time remained relatively constant, while individual pitch type frequency significantly evolved. We conclude that much of the cause for his improved performance comes from an overall change in strategy rather than speed, location, or other variables.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Description and Processing](#data-description-and-processing)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
4. [Methodology](#methodology)
5. [Main Results](#main-results)
6. [Discussion](#discussion)
7. [Conclusion and Outlook](#conclusion-and-outlook)
8. [Appendix](#appendix)

## Introduction
Major League Baseball (MLB) features some of the world's best players. A team’s defense relies heavily on a strong starting pitcher. Logan Webb of the San Francisco Giants has significantly improved his pitching performance since the start of his career. This paper explores the underlying changes or trends that affected his performance, positively or negatively, from 2019 to 2024.

## Data Description and Processing
### Data Description
The data used for this analysis comes from Statcast, a tracking technology developed by MLB. We specifically used Statcast data on variables relating to Logan Webb over a five-year period. The key variables include:

- **Pitch Type:** The type of pitch thrown by the pitcher.
- **Pitch Velocity:** The speed of the pitch thrown.
- **Pitch Spin Rate:** The rate at which a pitched ball spins.
- **Pitch Location:** The location in which the ball crosses the plate.
- **Strike or Ball:** Whether a pitched ball was a strike, swing and miss, or ball.
- **Earned Run Average (ERA):** Measures the average number of earned runs a pitcher allows per nine innings pitched.
- **Walks and Hits Per Inning Pitched (WHIP):** Measurement of the number of base runners a pitcher has allowed per inning pitched.
- **Types of Hit:** Describes the type of hit ball (single, double, triple, home run, ground out, pop up, or fly ball).

## Exploratory Data Analysis
We summarize the main characteristics of Logan Webb’s pitching data to gain a general understanding of the data structure and patterns. This includes visualizations such as aggregate bar graphs for pitch type proportions and average pitch velocity by pitch type.

## Methodology
### Line Graphs
Used to depict trends over time for variables such as pitch type proportions, pitch velocity, and spin rate.

### Odds Ratios
Calculated to quantify the relationship between two binary variables (e.g., odds of a hit given a pitch type vs. all other pitch types).

### Heat Maps
Used to represent the distribution and intensity of data across two variables, such as pitch location and where in the strike zone balls tend to get hit.

## Main Results
### Line Graphs
Analyzed trends in pitch velocity, spin rate, pitch type frequency, and WHIP over time. 

### Odds Ratio Table
Calculated the odds ratio of a hit given each pitch type over each season.

### Heat Maps
Visualized pitch placement and hit events by season and pitch type.

## Discussion
### Strength of Analysis
The analysis comprehensively examines various critical aspects of pitching, providing nuanced evaluations of Webb’s performance.

### Limitations
Acknowledges limitations such as the disparity in pitch frequencies and the unique pitching style of Logan Webb, which may limit generalizability.

## Conclusion and Outlook
### Future Research Directions
Proposes areas for further exploration, such as advanced pitch metrics, comparative studies, and the impact of external factors.

### Conclusion
Summarizes key findings, including strategic pitch selection and stable pitch velocity and location, while suggesting potential areas for Webb’s performance improvement.

## Appendix
Contains additional details, initial brainstorming, data requests, preprocessing steps, and code used for the analysis.

---

This README provides an overview of the project structure and key findings. For detailed analysis, methodologies, and visualizations, please refer to the full report.
