import streamlit as st
from st_pages import add_page_title
from app.utils import BLS
from datetime import datetime

add_page_title()

today = datetime.today()
start_year = today.year

if today.month == 1:
    end_year = today.year - 1
else:
    end_year = today.year

bls = BLS()


def get_unemployment_rate(unemployment_col):
    
    data = bls.read_timeseries(value_status="Level",
                        series_id="LNS14000000", 
                        series_choice="Unemployment Rate", 
                        freq="M",
                        start_year=start_year,
                        end_year=end_year,
                        )

    new_rate = float(data[0][2])
    month = data[0][1]
    old_rate = float(data[1][2])
    

    unemployment_col.metric(
        label=f"Unemployment Rate ({month})",
        value=f"{new_rate}%",
        delta=round((new_rate - old_rate), 2),
    )


def get_hiring_rate(hiring_col):
    
    data = bls.read_timeseries(value_status="Level",
                        series_id="JTS000000000000000HIR", 
                        series_choice="Hiring Rate", 
                        freq="M",
                        start_year=start_year,
                        end_year=end_year,
                        )
    
    new_rate = float(data[0][2])
    month = data[0][1]

    old_rate = float(data[1][2])
    

    hiring_col.metric(
        label=f"Hiring Rate ({month})",
        value=f"{new_rate}%",
        delta=round((new_rate - old_rate), 2),
    )

def get_job_openings(openings_col):
    
    data = bls.read_timeseries(value_status="Level",
                        series_id="JTS000000000000000JOL", 
                        series_choice="Hiring Rate", 
                        freq="M",
                        start_year=start_year,
                        end_year=end_year,
                        )
    
    new_rate = float(data[0][2])
    month = data[0][1]

    old_rate = float(data[1][2])
    

    openings_col.metric(
        label=f"Job Openings ({month})",
        value=f"{int(new_rate*1000):,}",
        delta=f"{int((new_rate - old_rate)*1000):,}"
    )

def run():   

    unemployment_rate, hiring_rate, job_openings = st.columns(3)

    get_unemployment_rate(unemployment_rate)
    get_hiring_rate(hiring_rate)
    get_job_openings(job_openings)

    st.caption("Source: Bureau of Labor Statistics. All stats seasonally adjusted")


run()
