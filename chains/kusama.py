import requests
from base_chain import BaseChain


class Kusama(BaseChain):

    BLOCK_DURATION = 6
    CONVERSION_RATE = 10 ** 12

    def get_rewards(self, address):
        url = "https://kusama.api.subscan.io/api/scan/account/reward_slash"
        page_num = 0
        data = []
        # 4 eras each day, therefore we need at least 120 lines of data
        while page_num <= 2:
            request_data = {'row': 100,
                            'page': page_num,
                            'address': address}
            response = requests.post(url, headers=self.HEADERS, json=request_data)
            response_data = response.json()["data"]["list"]
            page_num += 1
            if response.status_code == 200 and response_data is not None:
                data = data + response_data
        return self.count_rewards(data, self.BLOCK_DURATION, self.CONVERSION_RATE)
