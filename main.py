import requests

USER_AGENT_HEADER = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
ACCEPT_HEADER = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"


class Nicovideo:
    def __init__(self) -> None:
        self.__session = requests.Session()
        self.__session.headers["user-agent"] = USER_AGENT_HEADER
        self.__session.headers["accept"] = ACCEPT_HEADER
    
    def perform_login(self) -> None:
        pass # TODO @synzr

    def fetch_nc_material(self, id: int) -> None:
        pass # TODO @synzr


def search(url: str):
    git = requests.get('https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q=%E3%81%A9%E3%81%93%E3%81%A7%E3%82%82%E3%81%84%E3%81%A3%E3%81%97%E3%82%87&_limit=50&_offset=0&_sort=%2BstartTime').json()
    print(git)

def grab_metadata(url: str):
   url = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{url}').json()
   # return
   return git



def download(url: str):
    metadata = grab_metadata(url)
    

if __name__ == '__main__':
    search('help')
    download('nc15531')