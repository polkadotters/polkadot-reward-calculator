from os import environ


class BaseChain:

    HEADERS = {'X-API-KEY': environ["SUBSCAN_API_KEY"],
               'Content-Type': 'application/json'}

    def get_block_num_for_30_days(self, block_duration):
        return int(30 * 24 * 60 * 60 / block_duration)

    def convert_number(self, number, rate):
        return float(number) / rate

    def count_rewards(self, data, block_duration, rate):
        count = 0
        block_30_days_ago = data[0]["block_num"] - self.get_block_num_for_30_days(block_duration)
        for item in data:
            if item["block_num"] > block_30_days_ago and item["event_id"] == "Reward":
                count = count + self.convert_number(item["amount"], rate)
        return count

    def count_transfer_rewards(self, data, block_duration, rate, address):
        count = 0
        block_30_days_ago = data[0]["block_num"] - self.get_block_num_for_30_days(block_duration)
        for item in data:
            if item["block_num"] > block_30_days_ago and item["from"] == address:
                count = count + self.convert_number(item["amount"], rate)
        return count
