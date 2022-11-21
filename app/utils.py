import json
from os import environ
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from dotenv import load_dotenv
import requests_cache
from os import environ


def get_api_key():
    """Get BLS API Key"""
    if Path("app/.env").exists():
        load_dotenv()

    assert isinstance(environ["APIKEY"], str) , "API Key not loaded."
    assert isinstance(environ["FREDKEY"], str), "FRED API Key not loaded."

class BLS:
    def __init__(self):
        self.api_key = environ.get("APIKEY")
        self.session = requests_cache.CachedSession("BLS_Requests")

    def read_timeseries(self,
        series_id: str,
        series_choice: str,
        value_status: str,
        freq: str,
        start_year: str,
        end_year: str,
        plot: bool=False
    ):
        """
        Queries Bureau of Labor Statistics (BLS) API for economic data.

        :param value_status: Value denomination of economic indicator.
        :param freq: Frequency in which timeseries posts (e.g. Monthly, Quarterly)
        :param series_id: BLS economic metric indicator ID
        :param series_choice: Plain English BLS economic metric name
        :param start_year: Year to begin query.
        :param end_year: Year to end query
        :param apikey: BLS API registration ID for querying.
        :return: None
        """
        headers = {"Content-type": "application/json"}
        data = json.dumps(
            {
                "seriesid": [series_id],
                "startyear": start_year,
                "endyear": end_year,
                "registrationkey": self.api_key,
            }
        )
        p = self.session.post(
            "https://api.bls.gov/publicAPI/v2/timeseries/data/", data=data, headers=headers
        )
        json_data = json.loads(p.text)

        api_data = []

        if not json_data:
            raise ValueError("Response data not returned.")

        for item in json_data["Results"]["series"][0]["data"]:
            year = item["year"]
            period_name = item["periodName"]
            value = item["value"]
            api_data.append([year, period_name, value])
        
        if plot != True:
            return api_data
            
        else:
            if freq == "M":
                columns = ["Year", "Month", "Value"]
                results = pd.DataFrame(api_data, columns=columns)
                results["Date"] = pd.to_datetime(
                    results.Year.astype(str) + "/" + results.Month.astype(str) + "/01",
                    format="%Y/%B/%d",
                ).dt.date
                results = (
                    results[["Date", "Value"]].sort_values(by="Date").reset_index(drop=True)
                )
                if value_status == "Index from Start Year":
                    results["Value"] = [
                        f"{((float(x) - float(results['Value'][0]))/float(results['Value'][0]))*100}"
                        for x in results["Value"]
                    ]
            elif freq == "Q":
                columns = ["Year", "Quarter", "Value"]
                results = pd.DataFrame(api_data, columns=columns)
                results["Date"] = pd.to_datetime(
                    [
                        str(year) + f"Q{str(quarter)[0]}"
                        for year, quarter in zip(results["Year"], results["Quarter"])
                    ]
                )
                if value_status == "Index from Start Year":
                    results["Value"] = [
                        f"{((float(x) - float(results['Value'][0]))/float(results['Value'][0]))*100}"
                        for x in results["Value"]
                    ]
            elif freq == "A":
                columns = ["Date", "Freq", "Value"]
                results = pd.DataFrame(api_data, columns=columns)
                results = (
                    results[["Date", "Value"]].sort_values(by="Date").reset_index(drop=True)
                )
                if value_status == "Index from Start Year":
                    results["Value"] = [
                        f"{((float(x) - float(results['Value'][0]))/float(results['Value'][0]))*100}"
                        for x in results["Value"]
                    ]
            else:
                raise ValueError(f"Unexpected frequency {freq} received")
                
            self.plot_timeseries(results, series_choice)
            

        
    def plot_timeseries(self, data: pd.DataFrame, series_choice: str) -> None:
        """
        Plot BLS economics indicator timeseries data.

        :param data:
        :param series_choice:
        :return: None
        """

        # Create traces
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=data["Date"], y=data["Value"], line=dict(color="crimson"))
        )

        fig.update_traces(mode="markers+lines")
        fig.update_layout(
            title=series_choice, template="simple_white", autotypenumbers="convert types"
        )
        st.write(fig)

       
