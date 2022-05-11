import requests
import json


def requesting() -> str:
    url = "http://127.0.0.1:8000/About"
    response = requests.get(url)
    json_string = response.text
    new_dict = json.loads(json_string)
    lst = list(new_dict)
    print(lst)



def main():
    requesting()




if __name__ == "__main__":
    main()