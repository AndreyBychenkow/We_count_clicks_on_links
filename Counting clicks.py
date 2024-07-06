import os
from urllib.parse import urlparse, urljoin

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    base_url = "https://api.vk.com/method/"
    method = "utils.getShortLink"
    api_url = urljoin(base_url, method)
    params = {"url": url, "access_token": token, "v": "5.131"}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        response_json = response.json()
        if "response" in response_json:
            return response_json["response"]["short_url"]
        elif "error" in response_json:
            print(f"Ошибка VK API: {response_json['error']['error_msg']}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка HTTP: {str(e)}")
    return None


def get_click_stats(token, url):
    base_url = "https://api.vk.com/method/"
    method = "utils.getLinkStats"
    parsed_url = urlparse(url)
    key = parsed_url.path.strip("/")
    api_url = urljoin(base_url, method)
    params = {"key": key, "access_token": token, "v": "5.131", "extended": 1}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        response_json = response.json()
        if "response" in response_json:
            stats = response_json["response"].get("stats", [])
            total_views = sum(item.get("views", 0) for item in stats)
            return total_views
        elif "error" in response_json:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка HTTP: {str(e)}")
    return None


def main():
    load_dotenv()
    VK_ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

    url = input("Введите ссылку: ")
    views = get_click_stats(VK_ACCESS_TOKEN, url)

    if views:
        print(f"Количество просмотров: {views}")
    else:
        short_url = shorten_link(VK_ACCESS_TOKEN, url)
        if short_url:
            print(f"Сокращенная ссылка: {short_url}")


if __name__ == "__main__":
    main()

