# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrapper(user_input):
    # Create an URL object
    url = f'https://www.marketwatch.com/investing/stock/{user_input}?mod=mw_quote_switch'  # Create object page
    page = requests.get(url)

    # parser-lxml = Change html to Python friendly format
    # Obtain page's information
    soup = BeautifulSoup(page.text, 'lxml')

    # Obtain information from tag <table>
    table1 = soup.find('ul', {"class": "list list--kv list--col50"})

    # Obtain every title of columns with tag <th>
    headers = []
    for x in table1.find_all('li'):
        for i in x.find_all('small'):
            title = i.text
            headers.append(title)

    # Create a dataframe
    mydata = pd.DataFrame(columns=headers)

    data = []
    # Create a for loop to fill mydata
    for x in table1.find_all('li'):
        for i in x.find_all('span', {"class": "primary"}):
            title = i.text
            data.append(title)
    length = len(mydata)
    mydata.loc[length] = data

    my_dict = {header: row[header] for header in headers for (index, row) in mydata.iterrows()}

    return my_dict

