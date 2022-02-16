"""Module for parsing JSON files got from twitter API"""

import json
import requests
from pprint import pprint


AUTH_INFO = {'Authorization': 'Bearer \
AAAAAAAAAAAAAAAAAAAAAHYZZQEAAAAACaTY6qZpAmIQumkIXGSXh%2BmermQ\
%3Diu3as5a5RqUZ5m49HRqaGjm6dpnkXphGAVGuA82gyVlQdeWyVJ'}


def get_json_from_api(url: str, add_info: dict) -> dict:
    """Return JSON object got from request to the Twitter API.

    Args:
        url (str): Endpoint url
        add_info (dict): Additional info that you want to get in response.

    Returns:
        dict: JSON object with info.
    """
    response = requests.get(url, headers=AUTH_INFO, params=add_info)

    return response.json()


def get_json_from_file(path: str) -> dict:
    """Return JSON object got from .json file.

    Args:
        path (str): Path to the .json file.

    Returns:
        dict: JSON object with info.
    """
    with open(path, 'r', encoding='utf-8') as file:
        json_info = json.load(file)

    return json_info


def navigate_in_json(info: dict):
    """Recursive function to navigate inside a JSON object.

    Args:
        info (dict): A JSON object with info.
    """
    if isinstance(info, dict):
        print("""
        This is a dictionary with {} keys. Type 'K' to see the keys.
        To view full dictionary, type 'F'.
        """.format(len(info)))
        while True:
            option = input('>>> ')
            if option in ('K', 'F'):
                break
            else:
                print('Chose correct option.')
        if option == 'K':
            pprint(info.keys())
            print("""
            Select one key.
            """)
            while True:
                key = input('>>> ')
                if key in info.keys():
                    break
                else:
                    print('Chose correct key.')
            navigate_in_json(info[key])
        elif option == 'F':
            pprint(info)
    elif isinstance(info, list):
        print("""
        This is a list that has {} elements. Type 'I' to chose element index.
        To view full list type 'F'.
        """.format(len(info)))
        while True:
            option = input('>>> ')
            if option in ('I', 'F'):
                break
            else:
                print('Chose correct option.')
        if option == 'I':
            print("""
            Select index.
            """)
            while True:
                index = int(input('>>> '))
                if index in range(len(info)):
                    break
                else:
                    print('Chose correct index.')
            navigate_in_json(info[index])
        elif option == 'F':
            pprint(info)
    else:
        pprint(info)


def main():
    """Main function control the overall flow.
    """
    print("""
    What source of json you want to use?
    'api' or 'file'.
    """)
    json_source = input('>>> ')

    if json_source == 'api':
        url = 'https://api.twitter.com/2/users/by/username/JoeBiden'
        add_info = {'user.fields': 'location'}

        r_json = get_json_from_api(url, add_info)
    elif json_source == 'file':
        print("""
        Choose a file. 'twitter1.json' and 'twitter2.json' availabe.
        """)
        while True:
            filename = input('>>> ')
            if filename in ('twitter1.json', 'twitter2.json'):
                break
            else:
                print('Choose correct name.')
        path = 'data/{}'.format(filename)

        r_json = get_json_from_file(path)
    else:
        print('Type correct option.')
        main()

    navigate_in_json(r_json)


if __name__ == "__main__":
    main()
