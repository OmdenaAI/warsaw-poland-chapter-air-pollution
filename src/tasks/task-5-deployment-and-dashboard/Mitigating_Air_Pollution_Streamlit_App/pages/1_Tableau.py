import streamlit as st
import streamlit.components.v1 as components


# https://public.tableau.com/app/profile/catalin.vulcan/viz/AirqualitystationsinPolandInteractiveMap/Sheet1
# https://public.tableau.com/app/profile/joseph.antony/viz/AnnualStaticColsvsAnnualMeanCAQIbyPolishVoivodship/Sheet1?publish=yes
# https://public.tableau.com/app/profile/rukshar.alam/viz/PollutantStationAnalysis/StationDistributionbyPollutantType


dashboard_embed_code_catalin_vulcan = """
<div class="tableauPlaceholder" id="viz1679817609148" style="position: relative">
  <noscript>
    <a href="#">
      <img
        alt="Sheet 1 "
        src="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ai&#47;AirqualitystationsinPolandInteractiveMap&#47;Sheet1&#47;1_rss.png"
        style="border: none" />
    </a>
    </noscript>
  <object class="tableauViz" style="display: none">
    <param name="host_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />
    <param name="embed_code_version" value="3" />
    <param name="site_root" value="" />
    <param name="name" value="AirqualitystationsinPolandInteractiveMap&#47;Sheet1" />
    <param name="tabs" value="no" />
    <param name="toolbar" value="yes" />
    <param
      name="static_image"
      value="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ai&#47;AirqualitystationsinPolandInteractiveMap&#47;Sheet1&#47;1.png"
    />
    <param name="animate_transition" value="yes" />
    <param name="display_static_image" value="yes" />
    <param name="display_spinner" value="yes" />
    <param name="display_overlay" value="yes" />
    <param name="display_count" value="yes" />
    <param name="language" value="en-US" />
  </object>
</div>
<script type="text/javascript">
  var divElement = document.getElementById("viz1679817609148");
  var vizElement = divElement.getElementsByTagName("object")[0];
  if (divElement.offsetWidth > 800) {
    vizElement.style.width = '1130px';
    vizElement.style.height = '727px';
    } else if (divElement.offsetWidth > 500) {
    vizElement.style.width = '1130px';
    vizElement.style.height = '727px';
     } else {
    vizElement.style.width = '100%';
    vizElement.style.height = '1527px';
    }
  var scriptElement = document.createElement("script");
  scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""


# dashboard_embed_code_rukshar_alam = 
# <div class="tableauPlaceholder" id="viz1679818341686" style="position: relative">
#   <noscript>
#     <a href="#">
#         <img
#         alt=" "
#         src="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PollutantStationAnalysis&#47;StationDistributionbyPollutantType&#47;1_rss.png"
#         style="border: none" /></a></noscript>
#         <object class="tableauViz" style="display: none">
#     <param name="host_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />
#     <param name="embed_code_version" value="3" />
#     <param name="site_root" value="" />
#     <param
#       name="name"
#       value="PollutantStationAnalysis&#47;StationDistributionbyPollutantType"
#     />
#     <param name="tabs" value="yes" />
#     <param name="toolbar" value="yes" />
#     <param
#       name="static_image"
#       value="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PollutantStationAnalysis&#47;StationDistributionbyPollutantType&#47;1.png"
#     />
#     <param name="animate_transition" value="yes" />
#     <param name="display_static_image" value="yes" />
#     <param name="display_spinner" value="yes" />
#     <param name="display_overlay" value="yes" />
#     <param name="display_count" value="yes" />
#     <param name="language" value="en-US" />
#   </object>
# </div>
# <script type="text/javascript">
#   var divElement = document.getElementById("viz1679818341686");
#   var vizElement = divElement.getElementsByTagName("object")[0];
#   if (divElement.offsetWidth > 800) {
#     vizElement.style.width = "1000px";
#     vizElement.style.height = "850px";
#   } else if (divElement.offsetWidth > 500) {
#     vizElement.style.width = "1000px";
#     vizElement.style.height = "850px";
#   } else {
#     vizElement.style.width = "100%";
#     vizElement.style.height = "1150px";
#   }
#   var scriptElement = document.createElement("script");
#   scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
#   vizElement.parentNode.insertBefore(scriptElement, vizElement);
# </script>



dashboard_embed_code_rukshar_alam = """
<div class="tableauPlaceholder" id="viz1679818341686" style="position: relative">
  <noscript>
    <a href="#">
        <img
        alt=" "
        src="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PollutantStationAnalysis&#47;StationDistributionbyPollutantType&#47;1_rss.png"
        style="border: none" /></a></noscript>
        <object class="tableauViz" style="display: none">
    <param name="host_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />
    <param name="embed_code_version" value="3" />
    <param name="site_root" value="" />
    <param
      name="name"
      value="PollutantStationAnalysis&#47;StationDistributionbyPollutantType"
    />
    <param name="tabs" value="yes" />
    <param name="toolbar" value="yes" />
    <param
      name="static_image"
      value="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PollutantStationAnalysis&#47;StationDistributionbyPollutantType&#47;1.png"
    />
    <param name="animate_transition" value="yes" />
    <param name="display_static_image" value="yes" />
    <param name="display_spinner" value="yes" />
    <param name="display_overlay" value="yes" />
    <param name="display_count" value="yes" />
    <param name="language" value="en-US" />
  </object>
</div>
<script type="text/javascript">
  var divElement = document.getElementById("viz1679818341686");
  var vizElement = divElement.getElementsByTagName("object")[0];
  if (divElement.offsetWidth > 800) {
    vizElement.style.width = '1130px';
    vizElement.style.height = '727px';
    } else if (divElement.offsetWidth > 500) {
    vizElement.style.width = '1130px';
    vizElement.style.height = '727px';
     } else {
    vizElement.style.width = '100%';
    vizElement.style.height = '1527px';
    }
  var scriptElement = document.createElement("script");
  scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

dashboard_embed_code_joseph_antony = """<div class='tableauPlaceholder' id='viz1679194089354' style='position: relative'>
<noscript>
<a href='#'>
<img alt='(Air Pollution Reduction Systems) Cyclones, Equipment - Efficiency Low ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;An&#47;AnnualStaticColsvsAnnualMeanCAQIbyPolishVoivodship&#47;Sheet1&#47;1_rss.png' style='border: none' />
</a>
</noscript>
<object class='tableauViz'  style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
<param name='embed_code_version' value='3' /> 
<param name='site_root' value='' />
<param name='name' value='AnnualStaticColsvsAnnualMeanCAQIbyPolishVoivodship&#47;Sheet1' />
<param name='tabs' value='no' />
<param name='toolbar' value='yes' />
<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;An&#47;AnnualStaticColsvsAnnualMeanCAQIbyPolishVoivodship&#47;Sheet1&#47;1.png' /> 
<param name='animate_transition' value='yes' />
<param name='display_static_image' value='yes' />
<param name='display_spinner' value='yes' />
<param name='display_overlay' value='yes' />
<param name='display_count' value='yes' />
<param name='language' value='en-US' />
<param name='filter' value='publish=yes' />
</object>
</div>  
<script type='text/javascript'>                    
var divElement = document.getElementById('viz1679194089354');                    
var vizElement = divElement.getElementsByTagName('object')[0];                    
if (divElement.offsetWidth > 800) {
vizElement.style.width = '1130px';
vizElement.style.height = '727px';
} else if (divElement.offsetWidth > 500) {
vizElement.style.width = '1130px';
vizElement.style.height = '727px';
 } else {
vizElement.style.width = '100%';
vizElement.style.height = '1527px';
}
var scriptElement = document.createElement('script');                    
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>              
"""

max_width_str = f"max-width: 1030px;"
align_items_str = f"align-items: normal;"

st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}} 
.css-uf99v8{{{align_items_str}}}</style>""",unsafe_allow_html=True)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

option="Annual Static Cols vs Annual Mean CAQI by Polish Voivodship by Joseph Antony"

option = st.selectbox(
        "Please select",
        ("Annual Static Cols vs Annual Mean CAQI by Polish Voivodship by Joseph Antony", 
         "Air quality stations in Poland, Interactive Map by Catalin Vulcan",
          "Pollutant Station Analysis by Rukshar Alam"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

def switch(option): 
    if option == "Annual Static Cols vs Annual Mean CAQI by Polish Voivodship by Joseph Antony":
      return   dashboard_embed_code_joseph_antony

    if option ==  "Air quality stations in Poland, Interactive Map by Catalin Vulcan":
        return   dashboard_embed_code_catalin_vulcan

    if option ==  "Pollutant Station Analysis by Rukshar Alam":
        return   dashboard_embed_code_rukshar_alam
      
    
components.html(switch(option), width=1130, height=650)

