import requests
from base_chain import BaseChain


class Astar(BaseChain):

    BLOCK_DURATION = 15
    CONVERSION_RATE = 10 ** 0
    STAKE_ACCOUNT = "YQnbw3h6couUX48Ghs3qyzhdbyxA3Gu9KQCoi8z2CPBf9N3"

    def get_rewards(self, address):
        url = "https://astar.api.subscan.io/api/scan/transfers"
        page_num = 0
        data = []
        # reward approx every 9 minutes, therefore we need to fetch around 6500 lines
        while page_num <= 65:
            request_data = {'row': 100,
                            'page': page_num,
                            'address': address}
            response = requests.post(url, headers=self.HEADERS, json=request_data)
            response_data = response.json()["data"]["transfers"]
            page_num += 1
            if response.status_code == 200 and response_data is not None:
                data = data + response_data
        return self.count_transfer_rewards(data, self.BLOCK_DURATION, self.CONVERSION_RATE, self.STAKE_ACCOUNT)
