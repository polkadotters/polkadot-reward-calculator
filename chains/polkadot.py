import requests
from base_chain import BaseChain


class Polkadot(BaseChain):

    BLOCK_DURATION = 6
    CONVERSION_RATE = 10 ** 10

    def get_rewards(self, address):
        url = "https://polkadot.api.subscan.io/api/scan/account/reward_slash"
        data = {'row': 100,
                'page': 0,
                'address': address}
        response = requests.post(url, headers=self.HEADERS, json=data)
        if response.status_code == 200:
            return self.count_rewards(response.json()["data"]["list"], self.BLOCK_DURATION, self.CONVERSION_RATE)
