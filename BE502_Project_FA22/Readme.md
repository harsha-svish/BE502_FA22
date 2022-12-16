# BAT 502 Project
______________________________

Group members:
1) Kamil Abdulrazzaq Khalaf - kamilk@arizona.edu
2) Nicolle Angela Viloria - nviloria@arizona.edu
3) Sri Harsha Vishwanath - shv@arizona.edu

_____________________________

## Project Prompt

The project aims to synthesize different parts of the knowledge acquired in this course. It is a group project with a team size of 2 to 4. Each group needs to raise a question (or form a hypothesis) about the raining data but should download additional data than the existing Tucson and Weather data in 2018-2021. You will analyze the downloaded data and conclude from the new data. Each group submits one copy of the report, which includes your research question, workflow, results, and conclusion. It ends with the contribution of each team member. Please attach separate files for the program coded for the project with respective suffix names (.r, .sh, or .py).


## Research question

Is a higher amount of rain associated with an increase in car accidents in Tucson, AZ?

## Data & Code:
1) Tucson car accidents - tucson_car_accidents.csv
2) Tucson Rain - File was larger than 25 MB, github did not accomodate this file
3) Analysis file - bat502_project.ipynb
4) Analysis file as raw python file -  bat502_project.py

## Results and Conclusions

This folder contains images of the results from the analysis file

1) Table with Number of collisions and rain amount - BATtable.png
2) Rain amount vs month and year - rainAmount.png
3) Number of accidents - accidents.png
4) Collisions and Rain Amount - collisionsRain.png

Our experiment wanted to solve whether or not there is a correlation between rain amount and car accidents in Tucson, AZ. To answer this question, we looked at the average rain amount for June, July, and August in 2018, 2019, 2020, and 2021 and compared it to the sum of collisions that occurred during those years. These months were chosen because it is the time in which there is the most rain in Tucson, AZ, because it is the monsoon season. This would give enough rain data compared to dry months in which there is little rain data to analyze. Plot 1 summarizes the average amount of rain during these months for 2018, 2019, 2020, and 2021. Most of the data points show an average rain amount of about 0.01 - 0.10 mm. There are two months in 2021 that are outliers, August and July, with an average rain amount of 0.20 mm and 0.34 mm, respectively.

Plot 1:
![RainAmount](https://github.com/harsha-svish/BE502_FA22/blob/main/BE502_Project_FA22/rainAmount.png?raw=true)

The number of car accidents for our specific months and years were plotted in Plot 2. For August, July, and June, there is a decrease in car accidents for the year 2020. For August, the car collisions were higher overall. This could potentially be due to the fact that the University of Arizona starts their fall semester during that month, resulting in an increase in the amount of drivers in Tucson, AZ. College students are younger drivers with less experience and are more likely to underestimate dangerous situations, which can cause car crashes. Teen drivers from ages 16-19 are also three times more likely to get into a fatal crash compared to drivers that are age 20 and older ([1]). On the other hand, the number of car collisions are shown to decrease in June 2018, 2019, 2020, and very slightly in 2021. This can be due to the fact that the academic year ends at the University of Arizona in June and there are less young, college students on the road.

Plot 2:
![Accidents](https://github.com/harsha-svish/BE502_FA22/blob/main/BE502_Project_FA22/accidents.PNG?raw=true)

The mean rain amount was plotted against the number of collisions during this time period in Plot 3. The scatter plot shows that a higher number of car collisions is not associated with an increase in rain amount. The largest number of collisions was 560, which occurred when the average rain amount was around 0.09 mm, but this may be an outlier. However, 0.09 mm is not the largest average rain amount recorded. The largest average rain amount recorded was 0.33, which was associated with 478 collisions, which was around the middle of the data spread for car collisions. Meanwhile, for the lowest number of collisions plotted at 408, the average rain amount was 0.07 mm, which was not the mean lowest rain amount recorded, but around the middle of the spread of most of the mean rain amounts recorded, factoring in that 0.33 mm and 0.21 mm are potential outliers. 

Based on these findings, we can conclude that there is insufficient data to draw conclusions about whether mean rain amount is correlated with an increase in car collisions in Tucson, AZ. If this study were to be repeated in the future, more months and years should be looked at in order to have more data points to draw conclusions from. This can also help mitigate the effects of the COVID-19 pandemic data points from 2020, in which the car collisions were noticeably lower for that year.

Plot 3:
![New Accidents vs Rain Amount](https://github.com/harsha-svish/BE502_FA22/blob/main/BE502_Project_FA22/rainVScollision.PNG?raw=true)

Works Cited

[1]	“Teen Drivers and Passengers: Get the Facts | Transportation Safety | Injury Center | CDC,” Nov. 22, 2022. https://www.cdc.gov/transportationsafety/teen_drivers/teendrivers_factsheet.html (accessed Dec. 14, 2022).
