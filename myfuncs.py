import streamlit as st

def intro(day=None, isDone=False):
    """
    Adds streamlit header elements based on day and status of completion

    Parameters:
    
    * `day`     :   The day selected through sidebar selectbox
    * `isDone`  :   Have the tasks for this day been completed?
    """
    if isDone:
        st.balloons()
        st.subheader(day + " Tasks")
    else:
        st.subheader("I've not reached there yet!")
    return


def calc_prog(finished, total):
    return finished/total


def daylist():
    return ["Day " + str(i) for i in range(1, 31)]


def read_RM_data(filepath, day):
    with open(filepath, "r+") as f:
        srch_str = '<summary>'+day+'</summary>'       # Keep README consistent with this
        stop_str = '</details>'
        data = f.readline()
        while srch_str not in data:
            data = f.readline()
        data = ""
        while stop_str not in data:
            data += f.readline()
    
    return data