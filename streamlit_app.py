import streamlit as st
from myfuncs import *


### DECLARATIONS ###

MAX_DAYS=30
COMPLETED=daylist(MAX_DAYS)[:5]     # Update till completion
SPECIAL=set(['Day 3','Day 5'])      # Update till completion

### HEADER ###
st.title("30 Days of Streamlit")
st.write("Check my progress below!")
st.progress(calc_prog(len(COMPLETED), MAX_DAYS))

st.sidebar.header("Navigate through the journey!")
day = st.sidebar.selectbox("Which day do you wish to visit?", daylist(MAX_DAYS))


### CONTENT ###
if day in COMPLETED:
    intro(day, isDone=True)
    try:
        data = read_RM_data('./README.md', day)
    except Exception as exp:
        print(exp.args[0])
    
    if day in SPECIAL:
        call_special(day)
    
    st.markdown(data, unsafe_allow_html=True)       # Can break due to rogue HTML
else:
    intro()