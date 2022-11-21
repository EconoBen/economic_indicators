from datetime import datetime
from json import load
from os import system

import streamlit as st
from st_pages import add_page_title

from app.utils import BLS

add_page_title()


def run():
    """
    Run homepage.
    """

    st.title("Labor Indicators")

    with open("app/BLS_series_mapping.json") as json_file:
        bls_mapping = load(json_file)

    series_choice = st.selectbox("BLS Series ID", tuple(bls_mapping.keys()))
    series_id = bls_mapping[series_choice][0]
    freq_id = bls_mapping[series_choice][1]

    current_year = datetime.now().year

    start_year_options = [str(x) for x in range(1948, int(current_year) + 1)][::-1]
    start_year = st.selectbox("Start Year", start_year_options, index=1)

    end_year_options = [str(x) for x in range(int(start_year), int(current_year) + 1)][
        ::-1
    ]

    end_year = st.selectbox("End Year", end_year_options, index=0)

    value_type = ["Level", "Index from Start Year"]
    value_status = st.selectbox("Value Type", value_type, index=0)

    if int(end_year) - int(start_year) > 20:
        raise ValueError("Start and End Years must be a maximum of 20 years apart.")

    system("poetry run streamlit cache clear")

    bls = BLS()
    bls.read_timeseries(
        series_id=series_id,
        series_choice=series_choice,
        value_status=value_status,
        freq=freq_id,
        start_year=start_year,
        end_year=end_year,
        plot=True
    )
    st.caption("Source: US Dept. of Labor, Bureau of Labor Statistics")

st.sidebar.caption("""👨‍💻 [About](https://benjaminlabaschin.com/?page_id=10) \n 
👾 [Repo](https://github.com/EconoBen/economic_indicators)"""
)
run()
