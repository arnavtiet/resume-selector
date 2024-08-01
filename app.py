import os
import pickle 
import streamlit as st
import pandas as pd 
from streamlit_option_menu import option_menu
if 'keyword' not in st.session_state:
    st.session_state.keyword = []

st.set_page_config(
    page_title="Resume sorter",
    layout="wide",
    page_icon="📃"
)

working_dir = os.path.dirname(os.path.abspath(__file__))

with st.sidebar:
    selected=option_menu(
        'Select sort option'
        , ['Sort by keywords', 'Sort by tech skills','Sort by soft skills'],
       menu_icon='file-earmark-person',
        icons=['text-wrap','file-earmark-code-fill','person-video2'],
        default_index=0
    
    )

if selected=='Sort by keywords':
    st.title('Sort by keywords')
    uploaded_file = st.file_uploader("Choose a file", type="csv")
    col1, col2, col3 = st.columns(3)
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        num_entries=len(df)
        with col1:
            participants = st.slider('Please enter the  number of resume to be sorted', 
                    min_value=0, max_value=num_entries, value=1)
    # keyword=[]
    new_keyword = st.text_input('Enter a keyword:', '')
    if st.button('Add Keyword'):
        if new_keyword:
            st.session_state.keyword.append(new_keyword)
            st.success(f'Keyword "{new_keyword}" added!')
    if len(st.session_state.keyword)  is not 0:
        st.write('Keywords:', st.session_state.keyword  )

if selected=='Sort by tech skills':
    st.title('Sort by tech skills')
    uploaded_file = st.file_uploader("Choose a file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        num_entries=len(df)
        with col1:
            participants = st.slider('Please enter the  number of resume to be sorted', 
                    min_value=0, max_value=num_entries, value=1)
    col1, col2, col3 = st.columns(3)
    lang=st.radio(
        "Select coding language",('C','C++', 'Java','Python','Other'))
    if lang=='C':
        st.write('C selected')
    elif lang=='C++':
        st.write('C++ selected')
    elif lang=='Java':
        st.write('Java selected')
    elif lang=='Python':
        st.write('Python selected')
    
    tech_st=st.radio(
        "Select tech stack ",('Web-developer','App-developer', 'Cyber-security','Network Engineer'))
    if tech_st=='Web-developer':
        level=st.radio("",("Full-stack developer","Front-end developer","Back-end developer"))
    elif tech_st=='App-developer':
        level=st.radio("",("Android","iOS","Flutter"))
        
    elif tech_st=='Cyber-security':
        st.write('Cyber-security selected')
    elif tech_st=='Network Engineer':
        st.write('Network Engineer selected')

    # projects=st.slider('Please enter the  number of minimum projects required', 
    #                 min_value=0, max_value=1000, value=1) 
    expyr=st.slider('Please enter the   minimum working experince year required', 
                    min_value=0, max_value=1000, value=1)



