from urllib import request
import requests, bs4

def main():
    tpage = 'https://automatetheboringstuff.com/files/rj.text'
    res = requests.get(tpage)
    try:
        res.raise_for_status()
        print(tpage + 'Page is OK')
    except Exception as exc:
        print(tpage + 'Broken')
    res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    try:
        res.raise_for_status()
        print('Page is OK')
    except Exception as exc:
        print('Broken')
    tpage1 = 'https://www.ensign.edu/quick-links'
    res = requests.get(tpage1)
    try:
        res.raise_for_status()
        print(tpage1 + 'Page is OK')
    except Exception as exc:
        print(tpage1 + 'Broken')
    res = requests.get('https://www.google.com/search?q=ertysdgfhgjhkj&rlz=1C5CHFA_enUS895US895&oq=ertysdgfhgjhkj&aqs=chrome..69i57.9192j1j7&sourceid=chrome&ie=UTF-8')
    try:
        res.raise_for_status()
        print('Page is OK')
    except Exception as exc:
        print('Broken')