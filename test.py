import os
import time
import requests

CLUSTER_IP = "10.105.120.17"
PORT = "30506"
TEST_TIME = 200


def test_api():
    print("---- test started ----")
    url = "http://{}:{}/api/recommend".format(CLUSTER_IP, PORT)
    print('url: {}'.format(url))

    payload = {
        'songs': [
            "1985",
            "All The Small Things"
        ]
    }

    for i in range(TEST_TIME):
        response = requests.post(url, json=payload, timeout=1)
        print("TEST [{}/{}]".format(i + 1, TEST_TIME),
              "TIME: {}".format(time.strftime("%Y-%m-%d %H:%M:%S")), response.json())
        time.sleep(1)


if __name__ == "__main__":
    test_api()
