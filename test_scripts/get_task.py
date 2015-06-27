import json
import random
import requests
from test_config import API_URL, TASK_TAIL
from test_config import DEFAULT_USERNAME as USERNAME
from test_config import DEFAULT_PASSWORD as PASSWORD


class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        task_id = random.randint(1, 3)
        raw_response = requests.get(url=API_URL + TASK_TAIL +
                                    str(task_id), auth=(USERNAME, PASSWORD))

        assert raw_response.status_code == 200, 'Invalid status code.'
        assert len(json.loads(raw_response.text)['task']['description']) != 0, \
            'Invalid task id.'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
