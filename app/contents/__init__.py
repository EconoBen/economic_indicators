import requests
from bs4 import BeautifulSoup
from pandas import ExcelFile


def check_response(response):
    if response.status_code != 200:
        print("Error fetching page")
        raise ValueError("Response Non 200")
    else:
        return response.content


def get_content(url: str):
    """Provide a url, get beautifulsoup conten"""
    base_response = requests.get(url)
    base_content = check_response(response=base_response)
    return BeautifulSoup(base_content, "html.parser")


base_url = "https://www.newyorkfed.org/"

### Get Base Page to get iFrame ###  noqa: E266
origin_url = base_url + "microeconomics/hhdc"
base_page = get_content(origin_url)
iframe = base_page.find(id="HHDCIframe")

### Use Base Page to get excel url ###
iframe_url = base_url + iframe.attrs["src"]
iframe_page = get_content(iframe_url)
xl_url = [
    base_url[:-1] + xl.get("href") + ".xlsx"
    for xl in iframe_page.find_all(class_="glossary-download")
    if "data/xls" in xl.get("href")
][0]

household_debt_workbook = ExcelFile(xl_url)
