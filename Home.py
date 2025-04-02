import streamlit as st
import pandas as pd


#make sure to change the data csv file and add your own code urls



st.set_page_config(layout = "wide")
col1, col2 = st.columns(2)  # col1 and col2 are object instances

with col1:
    st.image("images/myphoto.jpg")
with col2:
    st.title("Anushri Kawade")
    st.subheader("WELCOME TO MY PROJECT SHOWCASE WEBSITE!")
    content = """ 
    
I’m Anushri!, an enthusiastic AI engineer in the making, currently pursuing a B.Tech in Artificial Intelligence and Data Science at SPPU. \n 
My passion lies in blending data science with innovation to develop intelligent solutions for real-world challenges. I thrive on creativity, continuous learning, and crafting impactful projects that push the boundaries of AI.\n 
Here, I share my journey, projects, and ideas that reflect my commitment to making a difference through technology.
    """
    st.info(content)

contact = "Below you can find some of the apps I have built using Python. \n Feel free to contact me! "
st.info(contact)

col3,empty_col, col4 = st.columns([1.5 , 0.5 , 1.5])

df = pd.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:10].iterrows ():
        st.header( row["title"] )
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows ():
        st.header( row["title"] )
        st.write ( row['description'] )
        st.image ( "images/"+row["image"] )
        st.write ( f"[Source Code]({row['url']})" )


