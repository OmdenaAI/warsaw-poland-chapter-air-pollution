import streamlit as st
import streamlit.components.v1 as components
from utils.EDA import *

def dashboard_embed_code_joseph_antony():
    return st.write("Testing Testing")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

option="Map visualization"

option = st.selectbox(
        "Please select",
        ("Map visualization","eda_weather","Combined_air_quality_data_with_caqi","Normalization and dropping of redundant columns","Adding isUrban","Poland Air Pollution EDA & Imputation - Joseph Antony","Poland Weather Imputation - Joseph Antony","Merged Dataset EDA - Joseph Antony","Omdena air quality"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

def switch(option):
    if option == "Map visualization":
        return   dashboard_embed_code_joseph_antony()

    if option == "eda_weather":
        return dashboard_embed_code_joseph_antony()

    if option == "Combined_air_quality_data_with_caqi":
        return dashboard_embed_code_joseph_antony()

    if option == "Normalization and dropping of redundant columns":
        return dashboard_embed_code_joseph_antony()

    if option == "Adding isUrban":
        return dashboard_embed_code_joseph_antony()

    if option == "Poland Air Pollution EDA & Imputation - Joseph Antony":
        return dashboard_embed_code_joseph_antony()

    if option == "Poland Weather Imputation - Joseph Antony":
        return dashboard_embed_code_joseph_antony()

    if option == "Merged Dataset EDA - Joseph Antony":
        return dashboard_embed_code_joseph_antony(0)

    if option == "Omdena air quality":
        return dashboard_embed_code_joseph_antony()
    
components.html(switch(option), width=1130, height=650)

