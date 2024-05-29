import requests
import json
import pyrfc6266

def search_user(userId: str):
    offset = 0
    limit = 10
    itemsCount = None

    git = requests.get(f"https://public-api.commons.nicovideo.jp/v1/materials/search/tags?_limit=10&_offset={offset}&_sort=-startTime&filters[userId][0]={userId}").json()
    data = git.get("data")
    itemsCount = data.get("total")
    items = data.get("materials")

    for item in items:
        # print(item)
        global_id = item.get('global_id')
        title = item.get("title")
        print(f'[-] downloading {title}')
        download(global_id)

    if itemsCount < 10:
        return "done"
    offset += 10

    while offset != itemsCount:
        whypls = requests.get(f"https://public-api.commons.nicovideo.jp/v1/materials/search/tags?_limit=10&_offset={offset}&_sort=-startTime&filters[userId][0]={userId}").json()
        helpme = whypls["data"]["materials"]
        if helpme is None:
            break

        for i, v in enumerate(helpme):
            global_id = v.get('global_id')
            
            title = v.get("title")
            print(f'[-] downloading {title}, {i}')
            download(global_id)

        if (itemsCount - offset) < 10:
            offset += (itemsCount - offset)
        else: 
            offset += 10 


def search(term: str):
    offset = 0
    limit = 50
    itemsCount = None


    git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q={term}&_limit=50&_offset={offset}&_sort=%2BstartTime').json()
    data = git.get("data")
    itemsCount = data.get("total")
    items = data.get("materials")

    for item in items:
        global_id = item.get('global_id')
        title = item.get("title")
        print(f'[-] downloading {title}')
        download(global_id)
    
    # wtf
    if itemsCount < 50:
        return "done"
    offset += 50

    while offset != itemsCount:        
        whypls = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q={term}&_limit=50&_offset={offset}&_sort=%2BstartTime').json()
        helpme = whypls["data"]["materials"]
        if helpme is None:
            break

        for i, v in enumerate(helpme):
            global_id = v.get('global_id')
            title = v.get("title")
            print(f'[-] downloading {title}, {i}')
            download(global_id)

        if (itemsCount - offset) < 50:
            offset += (itemsCount - offset)
        else: 
            offset += 50 


    return ":3"


def grab_metadata(url: str):
   important_part = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{important_part}').json()
   with open(f"{url}_metadata.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(git, ensure_ascii=False))

   return git

def download_file(url):
    try:
        important_part = url.split('nc')[1]
        cookies = {
            'nicosid': '',
            'lang': 'en-us',
            'area': 'US',
            'user_session': '',
            'user_session_secure': '',
            'common-header-oshirasebox-newest': '',
        }

        headers2 = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8, image/jxl',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

        response2 = requests.post(f'https://public-api.commons.nicovideo.jp/v1/materials/{important_part}/download-session', cookies=cookies, headers=headers2).json()
        data = response2.get('data')
        timestamp = data.get('time')
        token = data.get('token')
        res3 = requests.get(f'https://deliver.commons.nicovideo.jp/download/{url}?token={token}&time={timestamp}', cookies=cookies, headers=headers2)

        res3.raise_for_status()
        if res3.headers.get('content-disposition') == None:
            print("FILES BROKEN")
            return "fail"

        d = res3.headers['content-disposition']

        get_file = pyrfc6266.parse_filename(d)

        with open(get_file, 'wb') as f:
            for chunk in res3.iter_content(chunk_size=8192): 
                f.write(chunk)
    except:
        print('something went wrong!, url: ', url)


def download(url: str):
    metadata = grab_metadata(url)
    
    return download_file(url)
    

if __name__ == '__main__':
    # search('%E3%81%A9%E3%81%93%E3%81%A7%E3%82%82%E3%81%84%E3%81%A3%E3%81%97%E3%82%87')
    # download('nc15433')
    # search_user('12574891')
    pass