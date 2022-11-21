import os.path as op
import sys
from st_pages import show_pages_from_config

sys.path.append(op.abspath(op.join(op.dirname(__file__), "..")))

from app.pages._home import run

show_pages_from_config()


def main():
    """Main function of the App"""
    run()

if __name__ == "__main__":
    main()
