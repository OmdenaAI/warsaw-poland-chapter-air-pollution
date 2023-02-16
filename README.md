# Mitigating Air Pollution in Poland Through Machine Learning

## Problem Statement

### Background

According to the Air Quality in Europe 2022 report by the European Environment Agency (EEA), air pollution is the largest environmental health risk in Europe and significantly impacts the health of the European population. There are several types of compounds considered as air pollutants. On the one hand, there is particulate matter (PM) of different sizes (PM2.5, PM10) consisting of solid and liquid particles suspended in air. On the other hand, also common gases, such as nitrogen dioxide (NO2), carbon dioxide (CO2), or ozone (O3), contribute to air pollution. The different pollutant quantities can further be combined into a single air quality index, such as the common air quality index (CAQI) used in the European Union.

### Problem

Air pollution is a particular problem in Poland. The annual EEA reports on air quality show that Poland is among the countries with the worst air quality in Europe. Bad air quality affects people’s lives and constitutes a considerable health risk. Therefore, mitigating air pollution could improve quality of life and lead to an overall healthier society. At the same time, this would reduce costs for the Polish health care system.

An important step towards mitigation is the identification of main factors and causes of air pollution specific to Poland. By using local time-series data on air pollutants together with other relevant country-specific data, an AI assisted approach could yield valuable insights in this matter. In particular, a machine-learning model for air quality prediction could give policy makers a simple but powerful tool to help tackle the issue of air pollution in Poland.

### Project Goals

* Identification of main factors contributing to air pollution in Poland
* Prototype a simple machine-learning model to predict air quality (classification or regression model, conventional or deep learning model)
* Open source GitHub repository

## Task overview

* **Task 1 - Data Cleaning:**
    * Clean and combine data files from the provided sources
    * obtain three tabular datasets for (i) pollutant data, (ii) weather data, and (iii) general regional data


* **Task 2 - Data Preprocessing:**
    * Merge locations of measurement stations for pollutants and weather appropriately
    * Combine them with the general regional data
    * Obtain a single tabular data file that can be used for EDA and modelling
    

* **Task 3 - EDA:**
    * Data visualization and time-series analysis
    * pin down main causes and possible hotspots of air pollution


* **Task 4 - Modelling:**
    * Develop a machine-learning model (conventional or deep learning) to predict air quality based on the given features
    * Can be either a classification model (good or bad air quality) or a regression model
    * Use the trained model to analyze feature importance to identify main factors contributing to air pollution in Poland


## Contribution Guidelines
- Have a Look at the [project structure](#project-structure) and [folder overview](#folder-overview) below to understand where to store/upload your contribution
- If you're creating a task, go to the task folder and create a new folder with the below naming convention and add a README.md with task details and goals to help other contributors understand
    - Task Folder Naming Convention : _task-n-taskname.(n is the task number)_  ex: task-1-data-analysis, task-2-model-deployment etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relavant location and update the README.md information table with your contribution details.
- Make sure your File names(jupyter notebooks, python files, data sheet file names etc) has proper naming to help others in easily identifing them.
- Please restrict yourself from creating unnessesary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion. 

## Project Structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers/collaborators using this project.
    ├── original           <- Original Source Code of the challenge hosted by omdena. Can be used as a reference code for the current project goal.
    │ 
    │
    ├── reports            <- Folder containing the final reports/results of this project
    │   └── README.md      <- Details about final reports and analysis
    │ 
    │   
    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        ├── visualizations <- Code and Visualization dashboards generated for the project
        │
        └── results        <- Folder to store Final analysis and modelling results and code.
--------

## Folder Overview

- Original          - Folder Containing old/completed Omdena challenge code.
- Reports           - Folder to store all Final Reports of this project
- Data              - Folder to Store all the data collected and used for this project 
- Docs              - Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referneced code/research papers and other useful documents used for this project
- Tasks             - Master folder for all tasks
  - All Task Folder names should follow specific naming convention
  - All Task folder names should be in chronologial order (from 1 to n)
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information
  - Update the [task-table](./src/tasks/README.md#task-table) whenever a task is created and explain the purpose and goals of the task to others.
- Visualization     - Folder to store dashboards, analysis and visualization reports
- Results           - Folder to store final analysis modelling results for the project.


