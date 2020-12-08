# pylint: disable=no-member

from concurrent.futures import ThreadPoolExecutor, as_completed
from os import environ

import requests
import requests_random_user_agent
from dotenv import load_dotenv
from stem import Signal
from stem.control import Controller

load_dotenv()


def get_session():
    session = requests.Session()
    session.proxies = {"http": "socks5://127.0.0.1:9050",
                       "https": "socks5://127.0.0.1:9050"}

    return session


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=environ.get("TOR_PASSWORD"))
        controller.signal(Signal.NEWNYM)


def check_ip(timeout=10):
    try:
        with get_session() as session:
            response = session.get("https://httpbin.org/ip", timeout=timeout)

        raw_ip = response.json()["origin"]
        return raw_ip
    except:
        return False


def test():
    # change ip
    renew_connection()

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_ip) for _ in range(50)]

        for future in as_completed(futures):
            result = future.result()
            print(result)


if __name__ == "__main__":
    test()
