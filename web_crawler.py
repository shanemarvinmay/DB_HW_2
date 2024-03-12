# TODO include a rediculous amout of screenshots of EVERYTHING.
'''
wikicfg web crawler
params topic

steps
get html
parse html
write output
'''
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
# from selenium import webdriver
import requests


def get_wikicfg_html(search_term, url):
    x = requests.get(url)
    return x.text

def parse_date_to_year(date):
    try:
        return int(date[-4:])
    except:
        return 0

def clean_string(string):
    string = string.encode("utf-8")
    string = string.decode("utf-8")
    string = string.replace("\n", "")
    string = string.replace("\t", " ")
    return string

def parse_row_to_list(row):
    data = []
    cells = row.find_all("td")
    for cell in cells:
        link = cell.find("a")
        if link:
            data.append(clean_string(link.text))
        elif cell.text:
            data.append(clean_string(cell.text))
    return data

def parse_html_to_dataframe(html):
    data = {
        'acronym': [],
        'name': [],
        'when': [],
        'where': []
    }
    html_parser = BeautifulSoup(html, features="html.parser")

    table = html_parser.find("table", {"cellpadding": "3", "cellspacing": "1"})
    table_rows = table.find_all("tr")
    for i in range(1, len(table_rows), 2):
        try:
            acronym, name = parse_row_to_list(table_rows[i])
            when, where, _ = parse_row_to_list(table_rows[i+1])
        except:
            continue
        data['acronym'].append(acronym)
        data['name'].append(name)
        data['when'].append(parse_date_to_year(when))
        data['where'].append(where)

    return pd.DataFrame(data=data)

if __name__ == "__main__":
    search_terms_to_urls = {
        "Big Data": "http://www.wikicfp.com/cfp/call?conference=Big%20Data", 
        "Machine Learning": "http://www.wikicfp.com/cfp/call?conference=machine%20learning",
        "Artificial Intelligence": "http://www.wikicfp.com/cfp/call?conference=Artificial%20Intelligence"
        }

    frames = []
    for search_term in search_terms_to_urls:  
        print(f'Getting results for {search_term}')
        for page in range(1, 21):
            print(f'Processing page {page} of 20')
            url = f"{search_terms_to_urls[search_term]}&page={page}"
            html = get_wikicfg_html(search_term, url)
            try:
                frames.append(parse_html_to_dataframe(html))
            except:
                pass
            # TODO write about the query delimeter in your report.
            # Query limiter
            sleep(7)
    
    df = pd.concat(frames)
    print('Datframe of scraped html data.')
    print(f'rows:{df.shape[0]}\tcolumns:{list(df.columns)}')
    df.to_csv('conference_html_data.csv', sep='\t', encoding='utf-8', index=False)
    df[['acronym', 'name', 'where']].to_csv('MAY_EXERCISE_1_OUTPUT.csv', sep='\t', encoding='utf-8', index=False)
    print("Done")