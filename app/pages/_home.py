import streamlit as st
from st_pages import add_page_title

add_page_title()


def run():
    st.markdown("# Welcome to Indicators")

    st.markdown("##### There's a lot of economic data out there. This is the data I care about.")

    st.markdown("""
                🏡 Home: Welcome Page \n
                📊 Core Report: Most recent, impactful economic data at a glance \n
                👨‍🏭 Labor: Labor Data \n
                🧾 Debt: Debt Data
    """)

st.sidebar.caption("""👨‍💻 [About](https://benjaminlabaschin.com/?page_id=10) \n 
👾 [Repo](https://github.com/EconoBen/economic_indicators)"""
)

run()