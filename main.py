import requests
import json

def search(term: str):
    offset = 0
    limit = 50
    # count how many items
    itemsCount = None

    # this code is full of laziness
    git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q={term}&_limit=50&_offset={offset}&_sort=%2BstartTime').json()
    data = git.get("data")
    itemsCount = data.get("total")
    items = data.get("materials")

    for item in items:
        global_id = item.get('global_id')
        title = item.get("title")
        print(f'[-] downloading {title}')
        # download(global_id)
    
    # wtf
    if itemsCount < 50:
        return "done"

    # should complete
    offset += 50

    while offset != itemsCount:        
        print(offset)
        git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q={term}&_limit=50&_offset={offset}&_sort=%2BstartTime').json()
        
        for item in items:
            global_id = item.get('global_id')
            title = item.get("title")
            print(f'[-] downloading {title}')
            # download(global_id)

        if (itemsCount - offset) < 50:
            print((itemsCount - offset))
            offset += (itemsCount - offset)
        else: 
            offset += 50 


    return ":3"


def grab_metadata(url: str):
   important_part = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{important_part}').json()

   with open(f"{url}_metadata.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(git))

   return git



def download(url: str):
    metadata = grab_metadata(url)
    

if __name__ == '__main__':
    #search('%E3%81%A9%E3%81%93%E3%81%A7%E3%82%82%E3%81%84%E3%81%A3%E3%81%97%E3%82%87')
    download('nc15531')