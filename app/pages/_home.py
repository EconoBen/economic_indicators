import streamlit as st
from st_pages import add_page_title

add_page_title()


def run():
    st.markdown("# Welcome to Indicators")

    st.markdown("##### There's a lot of economic data out there. This is the data I care about.")

    st.markdown("""
                ๐ก Home: Welcome Page \n
                ๐ Core Report: Most recent, impactful economic data at a glance \n
                ๐จโ๐ญ Labor: Labor Data \n
                ๐งพ Debt: Debt Data
    """)

st.sidebar.caption("""๐จโ๐ป [About](https://benjaminlabaschin.com/?page_id=10) \n 
๐พ [Repo](https://github.com/EconoBen/economic_indicators)"""
)

run()