import streamlit as st

st.set_page_config(layout = "wide")
col1, col2 = st.columns(2)  # col1 and col2 are object instances

with col1:
    st.image("images/myphoto.jpg")
with col2:
    st.title("Anushri Kawade")
    st.subheader("WELCOME TO MY PROJECT SHOWCASE WEBSITE!")
    content = """ 
    
I’m Anushri!, an enthusiastic AI engineer in the making, currently pursuing a B.Tech in Artificial Intelligence and Data Science at SPPU. 
My passion lies in blending data science with innovation to develop intelligent solutions for real-world challenges. I thrive on creativity, continuous learning, and crafting impactful projects that push the boundaries of AI. 
Here, I share my journey, projects, and ideas that reflect my commitment to making a difference through technology.
    """
    st.info(content)
