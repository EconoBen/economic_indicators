import os.path as op
import sys
from st_pages import show_pages_from_config
import streamlit as st

sys.path.append(op.abspath(op.join(op.dirname(__file__), "..")))

show_pages_from_config()


def main():
    """Main function of the App"""
    st.sidebar.caption("""👨‍💻 [About](https://benjaminlabaschin.com/?page_id=10) \n 
👾 [Repo](https://github.com/EconoBen/economic_indicators)"""
)

if __name__ == "__main__":
    main()
