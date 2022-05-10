import streamlit as st
from myfuncs import *


### DECLARATIONS ###

DAYS=1
MAX_DAYS=30
COMPLETED=daylist(MAX_DAYS)[:2]


### HEADER ###
st.title("30 Days of Streamlit")
st.write("Check my progress below!")
st.progress(calc_prog(DAYS, MAX_DAYS))

st.sidebar.header("Navigate through the journey!")
day = st.sidebar.selectbox("Which day do you wish to visit?", daylist(MAX_DAYS))


### CONTENT ###
if day in COMPLETED:
    intro(day, isDone=True)
    try:
        data = read_RM_data('./README.md', day)
    except Exception as exp:
        print(exp.args[0])
    
    st.markdown(data, unsafe_allow_html=True)       # Can break due to rogue HTML
else:
    intro()