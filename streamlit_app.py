import streamlit as st
from myfuncs import *


### DECLARATIONS ###

MAX_DAYS=30
COMPLETED=daylist(MAX_DAYS)[:15]     # Update till completion
SPECIAL=set(['Day 3', 'Day 5', 'Day 8', 'Day 9', 'Day 10', 'Day 11', 'Day 12', 'Day 14', 'Day 15'])      # Update till completion

print(globals())

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
    
    st.markdown(data)       # Can display rogue HTML tags
    
    if day in SPECIAL:
        call_special(day)
else:
    intro()