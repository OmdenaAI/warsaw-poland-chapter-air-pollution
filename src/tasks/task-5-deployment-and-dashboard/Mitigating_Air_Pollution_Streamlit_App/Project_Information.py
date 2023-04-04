import streamlit as st

st.set_page_config(
    page_title="Mitigating Air Pollution in Poland Through Machine Learning",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

JumbotronImgAltText="Mitigating Air Pollution in Poland Through Machine Learning"
#JumbotronImgUrl="https://omdena.com/wp-content/uploads/2023/01/Mitigating-Air-Pollution-in-Poland-Through-Machine-Learning-1080x720.jpg" 
#JumbotronImgUrl=https://omdena.com/wp-content/uploads/2023/01/Mitigating-Air-Pollution-in-Poland-Through-Machine-Learning-980x653.jpg
JumbotronImgUrl="https://omdena.com/wp-content/uploads/2023/01/Mitigating-Air-Pollution-in-Poland-Through-Machine-Learning-480x320.jpg"

#LogoImg = 'place-holder.png'
LogoImg = 'https://omdena.com/wp-content/uploads/2022/07/place-holder.png'
#ProfileImg = 'Omdena-Logo.png'
#LogoImg = Image.open(r'place-holder.png')
#ProfileImg = Image.open(r'Omdena-Logo.png')
HomePage_Title='Omdena Warsaw Poland Chapter Project'

HomePage_Content='''
#####  This Omdena Local Chapter Challenge runs for 4 weeks.  This project is initiated by the Warsaw, Poland Chapter to solve Real World Problems.

### The Problem
 Air pollution is a major problem in Poland which has the worst air quality among the countries in Europe.
 The annual EEA reports on air quality show that Poland is among the countries with the worst air quality in Europe. 
 Bad air quality affects people’s lives and constitutes a considerable health risk.
 Mitigating air pollution could improve quality of life and lead to an overall healthier society
 At the same time, this would reduce costs for the Polish health care system.
 
 An important step towards mitigation is the identification of the main factors and causes of air pollution specific to Poland. 
 By using local time-series data on air pollutants together with other relevant country-specific data, an AI-assisted approach could yield valuable insights in this matter. 
 In particular, a machine-learning model for air quality prediction could give policy makers a simple but powerful tool to help tackle the issue of air pollution in Poland.

### How could AI help?
+ A statistical model based on machine learning could yield valuable insights into main factors and causes of air pollution specific to Poland
    → important step towards mitigation of air pollution
+ A machine-learning model for air quality prediction can give policy makers a simple but powerful tool to help tackle the issue of air pollution in Poland.
+ We will focus on the Common Air Quality Index (CAQI):
<div class="items">
    <figure>
        <img src="https://airly.org/en/static/1413837ba3160a440de01529eaf1f428/caqi1.png" >
        <figcaption align='right'>Common Air Quality Index (CAQI) source from: (<a href="https://airly.org" target="_blank">https://airly.org</a>).</figcaption>
    </figure>
  </div>

### The Goals
The goals of this project are: 
+ Identification of main factors contributing to air pollution in Poland.
+ Prototype a simple machine-learning model to predict air quality:
    - Classification or Regression model
    - Conventional or Deep learning model).
+ Open source GitHub repository.

### Datasets used for this Project

| Chief Inspectorate for Environmental Protection | European Climate Assessment and Dataset (ECAD) project | Central Statistics Office of Poland (GUS) |
|--|--|--|
| Daily averages of **pollutants** for measurement stations across the country | Daily averages of **weather** data for measurement stations across the county | Yearly data on **other** potentially relevant factors |
| Pollutants: <br> ‣ PM2.5 <br> ‣ PM10 <br> ‣ O3 <br> ‣ NO2 | Cloud cover, radiation, humidity, temperature, precipitation, pressure, snow, sunshine, wind speed | Poviat level (county) or Voivodship level (region) <br> E.g. population density, green areas, urbanized areas, registered vehicles, animal stock, … |
| From 2015-2021 | From 1979-2021 | From 2010-2021 |
| Dataset in Polish | Dataset in English | Dataset in English | 
''' 

HomePage_ChapterLead='''
| Chapter Name | Lead Name |
|--|--|
| Warsaw, Poland Chapter Leads | Alexander Lau |
'''

HomePage_ProjectLeads='''

| Process Name | Lead Name | 
|--|--|
| Data Cleaning | Kojo Kesse, Vidushi Khanna |  
| Data-Preprocessing | Catalina, Chidansh M |  
| Exploratory Data Analysis (EDA) | Joseph Antony |  
| Modeling | Shubhankar Sharma, Sagar |  
| Deployment | Vinod | 
'''

HomePage_Content_Header=f"""

"""


with st.container():
  with open("style.css") as cssfile:
    st.markdown(f"<style>{cssfile.read()}</style>", unsafe_allow_html=True)

  st.markdown(f"""
    <div id="profile-upper">
    <div id="profile-banner-image">
      <img src="{JumbotronImgUrl}" alt="Banner image">
    </div>
    <div id="profile-d">
      <div id="profile-pic">
        <img src="{LogoImg}" alt={JumbotronImgAltText}>
      </div>
      <div id="u-name"><h2>{JumbotronImgAltText}</h2></div>
    </div>
   """, unsafe_allow_html=True)
  st.markdown("<br>", unsafe_allow_html=True)
# st.image(image=JumbotronImgUrl, caption=JumbotronImgAltText,use_column_width ='auto')
# st.image(LogoImg, width=130)

#st.image(ProfileImg, width=700)
#st.title(HomePage_Title)
st.markdown(HomePage_Content, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(HomePage_ChapterLead, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(HomePage_ProjectLeads, unsafe_allow_html=True)
