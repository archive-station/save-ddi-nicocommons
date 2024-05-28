import requests
import pyperclip

def search(term: str):
    offset = 0
    limit = 50
    # count how many items
    itemsCount = None

    git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q={term}&_limit=50&_offset=0&_sort=%2BstartTime').json()
    data = git.get("data")
    itemsCount = data.get("total")
    items = data.get("materials")
    # print(items)
    for item in items:
        global_id = item.get('global_id')
        title = item.get("title")
        print(f'[-] downloading {title}')
        download(global_id)
    
    return ":3"


def grab_metadata(url: str):
   url = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{url}').json()
   # return
   return git



def download(url: str):
    metadata = grab_metadata(url)
    

if __name__ == '__main__':
    search('%E3%81%A9%E3%81%93%E3%81%A7%E3%82%82%E3%81%84%E3%81%A3%E3%81%97%E3%82%87')
    download('nc15531')