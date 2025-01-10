# Analyzing My Spending Patterns at Coffee Shops at Sabancı University Using Akbank Transaction Data
## Abstract:
  This projects explores the relationship between coffee shop spendings of mine through Akbank transactions and academic deadlines and exam dates over a timeline between 2nd of March 2024 and 21th of December 2024 excluding the summer time. Focusing on coffee shops in my university campus, the purpose is to find patterns of my habits of coffee shop spendings and be in control of my behaviour to optimize my budget in periods of increased academic activity. In this project, data will be extracted and visualized using charts and visualisation mathods like EDA. I believe that this project will show me important information about my behaviour and help me to spend my money at coffee shops in a more conscious way. 
  
## Introduction:
  This project mainly focuses on coffee shop spendings of mine because I'm a student and I mostly spend my money to buy a cup of coffee or something to eat between my lectures other than a meal. While I mostly focus on lectures, friends and hobbies of mine -especially on busy weeks- I may not notice how much I've spent throughout the day on coffee or snacks. Therefore, I believe that this project can provide a visual summary of my spending behaviour at coffee shops and help me to optimize my budget. 
  
  In this project I aim to collect my transaction data of Starbucks, Coffy, Espressolab, Simit Sarayı and Fasshane in my university campus, visualize the patterns and analyze the patterns over time, also try to find a correlation with my important task deadlines, midterms and finals.

## Research Question:
  Does my coffee shop spendings change with respect to specific deadlines, midterms and finals, and which coffee shop I prefer the most during these time periods?

## Hypothesis:
  My visits to the coffee shops increase during exam weeks and deadlines. Also, I prefer Coffy mostly among all the coffee shops in my campus since it is closer to the Information Center. 

## Methodology, Scope and Intended Steps:
  I chose my data source as my Akbank transaction history as pdf files and my academic calendar -including midterms, finals and deadlines of projects, important homeworks and take home tasks- as an excel file. I will extract the related data -Starbucks, Coffy, Espressolab, Simit Sarayı and Fasshane- from the files. I will focus on the time period from 02.03.2024 to 21.12.2024 excluding the summer time that I don't stay in university. Also, as stated above this project will only focus on five coffee shops which are located in our campus. 
  
  After extracting the related raw data and putting it into a proper form, I will match the dates with the transaction history. I will visualize the data using the methods I learned in the lecture like EDA and use a proper chart system to combine all the data. After visualization, I will calculate averages, frequency and correlations using correlation coefficients. Based on my findings on data I will evaluate my hypothesis and write my conclusion. 
  
  **My outline for the steps I wrote:**
  - **Step1** - Gather all the raw data from Akbank. Form an excel sheet including midterms, finals and deadlines. 
  - **Step2** - Extract the related data from Akbank. Put all the data in a form and match the dates, so that I can work on it. 
  - **Step3** - Visualize the data using EDA, charts and python. 
  - **Step4** - Calculate related statistics and test hypothesis. 
  - **Step5** - Finalize the report. 
  - 
## Process
  To gather and prepare the data, I first downloaded the related transaction files. Then I used OCR (Optical Character Recognition) to extract transaction details from my Akbank PDF files. Also, I used some keywords to filter the data and categorize the coffee shops. I then organized the extracted data into a txt file by filtering out some unrelated columns, aligning it with dates. Later, I created an excel file for the academic calender data and I converted it into a txt file. Using this structured dataset, I visualized the data through a stacked bar chart to represent coffee shop spending patterns alongside academic deadlines, date by date. After visualizing, I applied statistical techniques such as linear regression, chi-square tests, and correlation analysis to explore and quantify the relationship between my spending habits and academic activity. This combination of data extraction, visualization, and statistical analysis helped me gain deeper insights into my behavior.

## Conclusion:
  In this project, I analyzed the relationship between my coffee shop spending and academic deadlines. The results showed mixed findings. The chi-square test suggested a weak but significant link (Chi-Square Statistic: 6.41, p-value: 0.0406), but the linear regression (R-squared: 0.00) and correlation coefficients (Pearson: -0.03, Spearman: -0.09) indicated almost no direct connection. Logistic regression provided moderate accuracy (weighted F1-score: 0.62), hinting that other factors might also play a role in my spending habits. Overall, while deadlines might have some influence, the relationship isn’t as strong as I expected. Also, from the analysis, it’s clear that I visit Coffy the most out of all the coffee shops in the dataset. This fits with my expectation since Coffy is the closest to the Information Center, making it the most convenient choice, especially during busy academic periods. In sum, even though I couldn't see a strong correlation between my spending habits at coffee shops and academic deadlines, I think that it would be a good idea to try to manage busy weeks with less visits to coffee shops. In this project I didn't examine the amount of money I spend, because I wanted to focus on pattern instead of the exact value. I saw that I visit Coffy more which is very sensible. This project aimed to figure out the patterns and I believe it succeeded. Additionally, I think further analysis is needed to figure out more.
  
  
  
