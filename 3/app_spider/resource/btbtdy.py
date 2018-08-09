from bs4 import BeautifulSoup
import requests


def processing_list():
    result = []
    r = requests.get('http://www.btbtdy.net/new/dianying/')
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "html.parser")
    li_list = soup.find_all('li', class_="li")
    for li in li_list:
        div_list = li.find_all('div')
        if 'name' in div_list[0]['class']:
            data = {
                'href': "http://www.btbtdy.net" + div_list[0].a['href'],
                'title': div_list[0].a.text,
                'source_type': div_list[4].text,
            }
            result.append(data)
    return result


if __name__ == '__main__':
    print(processing_list())
