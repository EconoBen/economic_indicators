"""Main module for the streamlit app"""
import os.path as op
import sys

import plotly.express as px
import streamlit as st

sys.path.append(op.abspath(op.join(op.dirname(__file__), "..")))

from st_pages import add_page_title

add_page_title()


from app.pages import household_debt_workbook

sheet_name = "Page 3 Data"
title = "Total Household Debt Balance and Its Composition"
x_axis = "Year:Quarter"
y_axis = "Trillions of $"
source = "Source: New York Fed Consumer Credit Panel/Equifax"
columns = [
    "Mortgage",
    "HE",
    "Revolving",
    "Auto Loan",
    "Credit Card",
    "Student Loan",
    "Other",
    "Total",
]


def total_debt_guarterly():
    total_debt = (
        household_debt_workbook.parse(sheet_name, header=3)
        .set_index("Unnamed: 0")
        .iloc[:, :-1]
    )
    total_debt.index.names = [x_axis]

    return total_debt


def bar_plot():
    total_debt = total_debt_guarterly().iloc[:, :-1]

    fig = px.bar(
        total_debt,
        x=total_debt.index,
        y=total_debt.columns,
        labels={"variable": "Debt Type"},
        title=title,
        width=800,
        height=400,
    )
    fig.update_xaxes(
        tickvals=total_debt.index[::4], tickangle=45, tickfont=dict(size=12)
    )
    fig.update_yaxes(
        title=y_axis, tickfont=dict(size=12), tickprefix="$", showgrid=False
    )

    fig.update_layout(width=1000, height=500)

    st.plotly_chart(fig, use_container_width=True)
    st.caption(source)


def run():
    bar_plot()

st.sidebar.caption("""👨‍💻 [About](https://benjaminlabaschin.com) \n 
👾 [Repo](https://github.com/EconoBen/economic_indicators)"""
)
run()
