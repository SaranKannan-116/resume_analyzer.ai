import streamlit as st

from analysis import analyze_resume

st.set_page_config('Resume Analyzer',page_icon='愛')

st.title('RESUME ANALYZER USING AI🤖🇦🇮֎✨')

st.header(':blue[AI powered Resume analyzer with given job description using AI𖡎]')

st.subheader('This page helps you to compare the resume and the iven job description and provide ats, probability and SWOT analysis')

st.sidebar.subheader('Drop your resume  here🌱')

pdf_doc=st.sidebar.file_uploader('Click here',type=['pdf'])

st.sidebar.markdown('Designed by Saran Kannan 🎓')
st.sidebar.markdown('Git hub:https://github.com/SaranKannan-116/resume_analyzer.ai')

job_des = st.text_area('copy and paste the JD here🕹️', max_chars=10000)

submit=st.button('Get Result🎯')

if submit:
    with st.spinner('Loading.....'):
        analyze_resume(pdf_doc,job_des)