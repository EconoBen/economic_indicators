import os.path as op
import sys

import streamlit as st

sys.path.append(op.abspath(op.join(op.dirname(__file__), "..")))

from st_pages import show_pages_from_config

show_pages_from_config()


def main():
    """Main function of the App"""


if __name__ == "__main__":
    main()
