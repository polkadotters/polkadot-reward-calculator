import requests
from base_chain import BaseChain


class Moonriver(BaseChain):

    BLOCK_DURATION = 24
    CONVERSION_RATE = 10 ** 18

    def get_rewards(self, address):
        url = "https://moonriver.api.subscan.io/api/scan/account/reward_slash"
        page_num = 0
        data = []
        # 10 rewards per day, therefore we need at least 300 lines of data
        while page_num <= 4:
            request_data = {'row': 100,
                            'page': page_num,
                            'address': address}
            response = requests.post(url, headers=self.HEADERS, json=request_data)
            response_data = response.json()["data"]["list"]
            page_num += 1
            if response.status_code == 200 and response_data is not None:
                data = data + response_data
        return self.count_rewards(data, self.BLOCK_DURATION, self.CONVERSION_RATE)
