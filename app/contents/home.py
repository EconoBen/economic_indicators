"""Home page shown when the user enters the application"""
import streamlit as st


def run():
    """
    Run homepage.
    """
    st.title("Economic Indicators")

    st.markdown(
        """
        There are many useful economic indicators out there. This dashboard contains those I tend to watch.
                
        All sources cited.
        """
    )
