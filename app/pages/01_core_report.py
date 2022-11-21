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

def get_consumer_price_index(cpi_col):
    
    data = bls.read_timeseries(value_status="Level",
                        series_id="CUSR0000SA0", 
                        series_choice="Consumer Price Index", 
                        freq="M",
                        start_year=start_year,
                        end_year=end_year,
                        )
    
    this_month_level = float(data[0][2])
    curr_month = data[0][1]

    last_month_level = float(data[1][2])
    next_to_last_month_level = float(data[2][2])

    curr_rate = round(((this_month_level-last_month_level)/last_month_level)*100,1)
    last_rate = round(((last_month_level-next_to_last_month_level)/next_to_last_month_level)*100, 1)

    cpi_col.metric(
        label=f"Consumer Price Index ({curr_month})",
        value=f"{curr_rate}%",
        delta=round((curr_rate - last_rate), 1),
    )


def run():   

    unemployment_rate, hiring_rate, job_openings = st.columns(3)

    get_unemployment_rate(unemployment_rate)
    get_hiring_rate(hiring_rate)
    get_job_openings(job_openings)

    cpi_rate, _, _ = st.columns(3)

    get_consumer_price_index(cpi_rate)

    st.caption("Source: Bureau of Labor Statistics. All stats seasonally adjusted")

st.sidebar.caption("""👨‍💻 [About](https://benjaminlabaschin.com) \n 
👾 [Repo](https://github.com/EconoBen/economic_indicators)"""
)
run()
