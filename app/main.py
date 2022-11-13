import os.path as op
import sys

import streamlit as st

sys.path.append(op.abspath(op.join(op.dirname(__file__), "..")))

from app.contents import debt, home, labor


# Generate sidebar elements
def generate_sidebar_elements():
    pages = {"Home": home, "Labor": labor, "Debt": debt}

    # Sidebar -- Image/Title
    # st.sidebar.image(
    #     use_column_width=True,
    #     caption="",
    # )

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page.run()


def main():
    """Main function of the App"""
    generate_sidebar_elements()


if __name__ == "__main__":
    main()
