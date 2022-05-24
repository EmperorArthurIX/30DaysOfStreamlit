from random import seed
from numpy import size
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
    """
    Calculates the float value of challenge completion progress

    Parameters:
    
    * `finished`    :   The number of days for which tasks are completed
    * `total`       :   Total number of days in challenge

    Returns:

    * `float`   :   Value of progress, between `0` and `1`
    * `-1`      :   In case total number of days is passed as `0`
    """
    if total != 0:
        return finished/total
    return -1


def daylist(days):
    """
    Returns a list of enumerated days

    Parameters:

    * `days`    :   The number of days to be enlisted

    Returns:
    
    * `list`    :   ['Day 1', 'Day 2', ... , 'Day `days`']
    """
    return ["Day " + str(i) for i in range(1, days+1)]


def read_RM_data(filepath, day):
    """
    Reads content of README.md file and finds the section relevant to current day. This section is returned as a string.

    Parameters:
    
    * `filepath`    :   The path of the README.md file to be read
    * `day`         :   The day for which relevant section is to be found

    Returns:

    * str   :   Contents of section of file relevant to `day`. If no such section is found, then returns empty string.
    """
    with open(filepath, "r+") as f:
        srch_str = '<summary>'+day+'</summary>'       # Keep README consistent with this
        stop_str = '### Results'
        data = ""
        while srch_str not in data:
            data = f.readline()
            if not data:
                return ''
        data = ""
        while stop_str not in data:
            data += f.readline()
            if not data:
                return ''

        data = data[:-len(stop_str)]
    return data


def call_special(day):
    """
    Calls the special function defined for each day in the `SPECIAL` days set

    Parameters:

    * `day` :   The day for which the special function is to be called
    """
    globals()['day'+day[4:]+'_special']()       # globals() used since func call is elsewhere, not here. If main app was here, use locals()
    return


def day3_special():
    """
    Special function for Day 3
    """
    if st.button("Day 3 Special Button"):
        st.write("You've pressed the button! This is the Day 3 surprise ;)")
    else:
        st.write("Hmm...I wonder what's so special...")


def day5_special():
    """
    Special function for Day 3
    """
    st.write(
        "Day 5's special function is `st.write`",
        "In fact, this text has been written using this function!",
        "`st.write` supports Markdown, Functions Descriptions, DataFrames, Charts and Visualisations, Numbers and the list goes on.",
        "It also supports multiple arguments, just like all these different sentences each in a different string!"
        )


def day8_special():
    """
    Special function for Day 8
    """
    age = st.slider("What is your age?", min_value=1, max_value=150)
    if age < 10:
        st.write("It's great to see such a young person taking interest in Streamlit!")
    elif age < 50:
        st.write("Make the most of Streamlit and keep practicing!")
    elif age < 100:
        st.write("Streamlit makes our lives easier!")
    else:
        st.write("You've crossed a century, and that's amazing!")

    rng = st.slider("Plot numbers in range:", min_value=0, max_value=100, value=(10, 50))
    st.bar_chart(range(rng[0], rng[1]+1))


def day9_special():
    """
    Special function for Day 9
    """
    import numpy as np
    rng = st.slider("Choose a range",0, 100, value=(25, 75))
    arr = np.random.randint(low=rng[0], high=rng[1], size=100)
    st.caption("Plotting 100 random numbers from {} to {}, using `st.line_chart`".format(rng[0], rng[1]))
    st.line_chart(data=arr)


def day10_special():
    """
    Special function for Day 10
    """
    import numpy as np
    choice = st.selectbox("Select a chart type:", ["Line", "Bar", "Area"])
    arr = np.random.randint(low=0, high=100, size=(10, 2))
    if choice == "Line":
        st.line_chart(arr)
    elif choice == "Bar":
        st.bar_chart(arr)
    else:
        st.area_chart(arr)


def day11_special():
    """
    Special function for Day 11
    """
    from translate import Translator
    sentence = st.text_input("Enter a sentence in English", value="This is the default sentence!")
    langs = st.multiselect("Which languages do you speak?", ['English', "Spanish", "German"])
    for lang in langs:
        t = Translator(to_lang=lang)
        st.write(t.translate(sentence))


def day12_special():
    """
    Special function for Day 12
    """
    domains = ['Web Dev', 'Cloud', 'Data Science', 'Blockchain']
    arr = list()
    for i, domain in enumerate(domains):
        arr.append(st.checkbox(domain))
    
    for i, domain in enumerate(arr):
        if domain:
            st.write(domains[i])


def day14_special():
    """
    Special function for Day 14
    """
    import streamlit_folium as sf
    import folium

    world = folium.Map(
        location=(18.9316079, 73.1601956),
        zoom_start=4,
        tiles="Stamen Toner", width='100',)
    folium.Marker(
        location=(18.9316079, 73.1601956),
        popup="Amity University Mumbai",
        tooltip="This is where I study"
    ).add_to(world)

    sf.st_folium(world)


def day15_special():
    """
    Special function for Day 15
    """
    st.write("We can use `st.latex` to format LaTeX strings in Python!")
    st.write("Like writing equations in Python")
    st.latex(
        r"""
        x^2 + 4x + 4 = 0
        \\
        (x + 2) \cdot (x + 2) = 0
        \\
        \implies x = -2
        """)
    st.write("Or typing out identities")
    st.latex(
        r"""
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} 
        \\
        = \sum_{k=0}^{n-1} ar^k
        \\
        = a \left(\frac{1-r^{n}}{1-r}\right)
        """
    )
    st.write("One of the main uses of LaTeX in Python is while working with [SymPy](https://www.sympy.org/en/index.html)\n",
    "\nIt is especially beneficial while documenting code and explaining the math behind functions")