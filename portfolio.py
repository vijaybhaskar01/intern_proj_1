import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image

st.title(":red[Rimmalapudi Vijay Bhaskar]")

st.header(":blue[Data Scientist]")

tab1, tab2, tab3,tab4 = st.tabs(["About Me","Projects","Skills","Contact"])
with tab1:
    st.markdown("Data Science Intern at Innomatics Research Labs")
    st.markdown("I am always energetic and eager to learn new skills")

with tab2:
    st.markdown("Web scrapping")
    st.markdown("Machine learning")
    st.markdown("Natural Language Processing-NLP")
    st.markdown("Flask")

with tab3:
    st.markdown("Python")
    st.markdown("Data Analysis")
    st.markdown("Machine Learning")
    st.markdown("PGDCA")
    st.markdown("SQL")

with tab4:
    st.caption("Linkedin--https://www.linkedin.com/in/rimmalapudi-vijay-bhaskar-a49882266/")
    st.caption("Github--https://github.com/vijaybhaskar01")

