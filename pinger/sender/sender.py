import requests

from pprint import pprint
from timeit import default_timer as timer 
from enum import Enum

from config import Config


class Protocol(Enum):
    HTTP = "http://"
    HTTPS = "https://"


class Sender:
    """
    Class for sends requests and measures their time 
    """
    def __init__(self):
        self.password = Config.PASSWORD
        self.email = Config.EMAIL
        self.url = Config.URL
        self.session = requests.Session()
        self.protocol = Protocol.HTTPS.value
    
    def _login(self, endpoint, login_data):
        """
        Login
        """
    
        pprint(f"{self.protocol}{self.url}{endpoint}")

        try:
            response = self.session.post(f"{self.protocol}{self.url}{endpoint}", json=login_data)
            response.raise_for_status()
        # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

        print("Login successful OK {} \n", response.status_code)

        access_token = response.json().get("access_token")
        self.session.headers.update({"Authorization": f"Bearer {access_token}"})

    def _ping(self, endpoint):
        """
        Send request to `endpoint`
        """
        try:
            pprint(f"Try to get: {endpoint}")
            response = self.session.get(f"{self.protocol}{self.url}{endpoint}")
            response.raise_for_status()
        # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

        pprint(response.json())

    def run(self):
        """
        Start pinging
        """
        json_data = {
            "email": self.email,
            "password": self.password
        }

        self._login("/auth/login", json_data)

        endpoint = "/statuses?group_id=6280"
        start = timer()
        self._ping(endpoint=endpoint)
        end = timer()
        print(end - start)
