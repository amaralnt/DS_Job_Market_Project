![data](https://user-images.githubusercontent.com/69180967/207455818-277624f8-0893-4ee5-a8ac-f8eb2de70b65.jpg)

# Data Science Job Market Project

## Objective

Data Science is a fast-growing field, with more than 2.7 million new data jobs predicted to be created. This project aims to explore all the features of a dataset covering various aspects of the Data Science Job Market. Here, I clean, filter, format, analyze, and visualize the data. 

## Tools

The tools I used here are: 
- Excel: PivotTables and PivotCharts
- Python: wordcloud and matplotlib

## The Dataset

The entire ds_salaries dataset has 12 columns:
- __work_year:__ The year the salary was paid.
- __experience_level:__ The experience level in the job during the year.
- __employment_type:__ The type of employment for the role.
- __job_title:__ The role worked in during the year.
- __salary:__ The total gross salary amount paid.
- __salary_currency:__ The currency of the salary paid as an ISO 4217 currency code.
- __salary_in_usd:__ The salary in USD.
- __employee_residence:__ The employee’s primary country of residence during the work year as an ISO 3166 country code.
- __remote_ratio:__ The overall amount of work done remotely.
- __company_location:__ The country of the employer’s main office or contracting branch.
- __company_size:__ The median number of people that worked for the company during the year.
- __serial:__ The unnamed column holds serial values and is intended to be used as a Primary Key.

## Dimensions and Measures

Dimensions are the qualitative, categorical fields that are considered an independent variable. Measures are the quantitative, numerical fields considered a dependent variable; that is, its value depends on one or more dimensions.

Namely:
- __7 Dimensions Columns:__ Work Year, Job Title, Experience Level, Employment Type, Employee Residence, Company Location, Company Size.
- __2 Measures Columns:__ Salary USD, Remote Ratio

## Method

To perform a thorough analysis of every aspect of the dataset I decided to divide it into two parts: Univariate Analysis and Multivariate Analysis. 

### Univariate Analysis

It is the analysis of an isolated variable. The purpose of this type of analysis is to understand the distribution of values for a single variable. It goes through every single Dimension and Measure.  

### Multivariate Analysis

It takes into account two or more variables at the same time. The aim is to find patterns and correlations between several variables simultaneously.

Some of the approaches are:

- __Work Year Analysis__, relating it to Salary, and Remote Ratio;
- __Experience Level Analysis__, relating it to Employment Type, Job Title, and Company Size;
- __Company Location Analysis__, relating it to Experience Level;
- __Salary Analysis__, relating it to Work Year, Experience Level, Company Size, Job Title, and Remote Ratio.

## Source

Link to the full article: https://natan4tech.com/2022/10/04/eda-data-science-job-market/
