import os
import time
import requests

CLUSTER_IP = "10.105.120.17"
PORT = "30506"
TEST_TIME = 300

with open('test.log', 'w') as f:
    f.write('')


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
        try:
            response = requests.post(url, json=payload, timeout=0.5)
            response_json = response.json()
        except:
            response_json = "SERVICE_OFFLINE"

        log = "TEST [{}/{}] TIME: {} {}".format(i + 1, TEST_TIME,
                                                time.strftime("%Y-%m-%d %H:%M:%S"), response_json)
        print(log)

        with open('test.log', 'a') as f:
            f.write(log + '\n')
        time.sleep(0.5)


if __name__ == "__main__":
    test_api()
