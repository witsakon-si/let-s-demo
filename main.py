import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

def print_component(data):
    st.image(data['image_url'])

    tags = "";
    for tag in data['tags']:
        tags = tags + f"<span class='badge'>{tag}</span>"
    st.markdown(f"""
        <a class='image-url' href={data['url']}>{data['title']}</a>
        {tags}
    """, unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.title("Let's Demo")
st.text('Keep It Simple and Smart')
st.text('')


st.markdown("""
<style>
.image-url {
    font-size:16px !important;
    font-weight: bold;
    display: block; 
    text-align: center;
    text-decoration: none !important;
    padding-bottom: 8px;
}
.image-url:hover {
    color: #C73659;
}

.badge {
    background-color: #FFEFEF;
    border: none;
    color: black;
    font-size: small;
    padding: 3px 8px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 10px;
    cursor: default;
}
.badge:hover {
    background-color: #EED3D9;
}
</style>
""", unsafe_allow_html=True)
url = 'https://raw.githubusercontent.com/witsakon-si/let-s-demo/main/data.json'
resp = requests.get(url)
data = json.loads(resp.text)
print(data)

for idx, group in enumerate(data):
    st.subheader(group['group'], divider=True)
    demos = group['demo_list'];
    for i in range(0, len(demos), 4):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if i < len(demos):
                print_component(demos[i])
        with col2:
            if i+1 < len(demos):
                print_component(demos[i+1])
        with col3:
            if i+2 < len(demos):
                print_component(demos[i+2])
        with col4:
            if i+3 < len(demos):
                print_component(demos[i+3])


st.text('')
st.text('')
aboutMeCol1, aboutMeCol2 = st.columns(2)
with aboutMeCol1:
    st.subheader("About Me", divider=True)
    code = '''def aboutMe():
    print("Hello, World!")
    print("I'm Witsakon Siangwithan")
    print("I love coding and learning new tech stacks")
    print("Email: witsakon.si@gmail.com")
    '''
    st.code(code, language="python")
with aboutMeCol2:
    st.text('')