# 30 Days of Streamlit

I have always loved working with Streamlit, ever since I first discovered it.

The **30 Days of Streamlit** Challenge by [The Data Professor](https://youtube.com/dataprofessor) is one of the most exciting experiences I have had, and I would recommend everyone reading this to have a go at it as well!


## The Challenge

The **30 Days of Streamlit** Challenge is a campaign by Streamlit, in collaboration with Mr. Chanin Nantasenamat, also known as *The Data Professor*, to help interested people get involved in creating applications using the powerful and flexible Streamlit API and deploy them on Streamlit Cloud!

> Read more on the official [Blog Page](https://blog.streamlit.io/30-days-of-streamlit/)


## My take on the challenge

I fell in love with the idea of a consistency challenge related to the Python module I use extensively; thus, I am going to document each of the 30 days of the challenge in this repository, summarising key moments of learning from the day's work.


## My Goals

By taking up the challenge, I wish to accomplish the following goals:

- Become proficient in using the various attributes and features offered by Streamlit
- Increase speed and efficiency while using Python, especially when working with Streamlit and related modules from my domain of interest
- Develop and maintain consistency, not just through the challenge but also after the challenge is over
- Learn about the best practices for application deployment on Streamlit Cloud


## Timeline

<details open>
<summary>Day 1</summary>
<h3> Task Summary </h3>

- Set up a virtual environment
    
    Open Command Prompt where you want to create the environment and set up a virtual environment called `.env` in local machine (Windows)
    ```
    python -m venv .env
    ```
- Activate the environment
    
    In the same folder, activate the environment using the following command:
    ```
    .env\Scripts\activate
    ```
- Install Streamlit
    
    Once the environment is activated, the name of the environment will appear before the root directory of the folder on Command Prompt. Install Streamlit here
    ```
    pip install streamlit
    ```
- Launch the Streamlit Demo App

    Run the following command to launch the `Streamlit Hello` Demo application
    ```
    streamlit hello
    ```

<h3> Results </h3>

![Day 1](./images/Day1.png)

</details>

<details>
<summary>Day 2</summary>
<h3> Task Summary </h3>

- Create a Python File

    Using the file name `streamlit_app.py` enables deployment directly under the GitHub repository name instead of the specific file name

- Write some code

    Import Streamlit and write some code for your streamlit application!

    ```
    import streamlit as st

    st.title('30 Days of Streamlit')
    st.header('Welcome to my application!')
    ```

- Launch the app from your terminal

    Using the command line interface, run the streamlit application on localhost

    If you have a virtual environment, activate it from the command line (Windows)
    ```
    .env\Scripts\activate
    ```
    Launch the application from the command line
    ```
    streamlit run streamlit_app.py
    ```

<h3> Results </h3>

![Day 2](./images/Day2.png)

![Day 2](./images/Day2_2.png)

</details>