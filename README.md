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
- **Pitch Velocity:** Logan Webb’s pitch velocity for each pitch type remained generally stable over time.
- **Pitch Spin Rate:** Webb’s pitch spin rate for each pitch type remained generally stable over time.
- **Pitch Type Frequency:** The change up and sinker had a strong upwards trend in frequency, while the four-seam fastball had a strong decline.
- **WHIP (Walks and Hits Per Inning Pitched):** Webb’s WHIP was above the population average until 2021, after which it remained below average.
- **ERA (Earned Run Average):** Webb’s ERA remained higher than the population mean throughout the analysis period, though it showed a noticeable decrease from 2020 to 2021.

### Odds Ratio Table
- The **sweeper** consistently had an odds ratio below 1, indicating it was Webb’s best performing pitch.
- The **change up** had an odds ratio greater than 1 for every season except 2020, indicating it performed poorly relative to other pitches.
- The **four-seam fastball** had an odds ratio below 1 from 2021 to 2024, suggesting it was effective, though its sample size was small.

### Heat Maps
- Webb’s pitch location by pitch type evolved very little over the seasons.
- Areas with higher pitch frequencies tended to coincide with higher hit frequencies, indicating consistent pitch placement.

## Discussion
### Strength of Analysis
- The analysis comprehensively examines various critical aspects of Webb’s pitching, including pitch velocity, pitch type frequency, WHIP, ERA, strike frequencies, pitch location densities, and hit location densities.
- Odds ratios provided insights into the effectiveness of Webb’s pitches.

### Limitations
- Disparity in pitch frequencies affects the reliability of performance metrics for less frequently used pitches.
- Webb’s unique pitching style may limit the generalizability of the findings.
- The focus on stable pitch location was appropriate for Webb but may not apply to other pitchers.

## Conclusion and Outlook
### Future Research Directions
- **Advanced Pitch Metrics:** Explore pitch movement, release point consistency, and spin axis.
- **Comparative Studies:** Compare Webb’s performance trends with other top-performing pitchers.
- **Impact of External Factors:** Investigate the influence of weather conditions, opposing team strategies, and game location.
- **Mental and Physical Conditioning:** Evaluate the impact of mental resilience training and physical conditioning.
- **Longitudinal Analysis:** Extend the analysis to include more seasons.
- **Player-Specific Adjustments:** Analyze Webb’s strategy adjustments against different batters and game situations.

### Conclusion
- **Strategic Pitch Selection:** Webb increased his use of the change up and sinker while reducing reliance on the four-seam fastball.
- **Improved WHIP:** Webb consistently maintained a WHIP below the population average from 2021 onwards.
- **Stable Pitch Velocity and Location:** Webb’s performance improvements were driven by strategic changes in pitch selection rather than changes in pitch speed or location.
- **Higher ERA:** Despite improvements in WHIP, Webb’s ERA remained higher than the population mean, indicating room for further strategic refinement.

## Appendix
Contains additional details, initial brainstorming, data requests, preprocessing steps, and code used for the analysis.

---

This README provides an overview of the project structure and key findings. For detailed analysis, methodologies, and visualizations, please refer to the full report.
