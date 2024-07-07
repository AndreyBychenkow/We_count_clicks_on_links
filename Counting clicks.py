import os
from urllib.parse import urlparse, urljoin

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    base_url = "https://api.vk.com/method/"
    method = "utils.getShortLink"
    api_url = urljoin(base_url, method)
    params = {"url": url, "access_token": token, "v": "5.131"}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    response_data = response.json()
    if "response" in response_data:
        return response_data["response"]["short_url"]
    elif "error" in response_data:
        raise ValueError(
            f"Ошибка VK API: {response_data['error']['error_msg']}")


def get_click_stats(token, url):
    base_url = "https://api.vk.com/method/"
    method = "utils.getLinkStats"
    parsed_url = urlparse(url)
    key = parsed_url.path.strip("/")
    api_url = urljoin(base_url, method)
    params = {"key": key, "access_token": token, "v": "5.131", "extended": 1}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    response_data = response.json()
    if "response" in response_data:
        stats = response_data["response"].get("stats", [])
        total_views = sum(item.get("views", 0) for item in stats)
        return total_views
    elif "error" in response_data:
        raise ValueError(
            f"Ошибка VK API: {response_data['error']['error_msg']}")


def is_shorten_link(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == "vk.cc"


def main():
    load_dotenv()
    vk_service_key = os.environ['VK_SERVICE_KEY']

    url = input("Введите ссылку: ")

    try:
        if is_shorten_link(url):
            views = get_click_stats(vk_service_key, url)
            print(f"Количество просмотров: {views}")
        else:
            short_url = shorten_link(vk_service_key, url)
            print(f"Сокращенная ссылка: {short_url}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка HTTP: {str(e)}")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
