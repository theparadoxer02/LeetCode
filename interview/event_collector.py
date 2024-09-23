from datetime import datetime, timedelta


class EventCollector:
    def __init__(self):
        self.sec_count = {}

    def clean_data(self):
        curr_time = datetime.now()
        before_1_mins = datetime.now() - timedelta(seconds=60)
        for store_time in self.sec_count.keys():
            if curr_time >= before_1_mins:
                del self.sec_count[store_time]

    def onEvent(self):
        curr_time = datetime.now()
        if curr_time not in self.sec_count:
            self.sec_count[curr_time] = 1
        else:
            self.sec_count[curr_time] = self.sec_count[curr_time] + 1
        self.clean_data()

    def getCountLast10Seconds(self):
        curr_time = datetime.now()
        ten_sec_back = curr_time - timedelta(seconds=10)
        counter = 0
        for store_time in self.sec_count.keys():
            if ten_sec_back <= store_time <= curr_time:
                counter += self.sec_count[store_time]
        return counter

    def getCountLast60Seconds(self):
        curr_time = datetime.now()
        ten_sec_back = curr_time - timedelta(seconds=60)
        counter = 0
        for store_time in self.sec_count.keys():
            if ten_sec_back <= store_time <= curr_time:
                counter += self.sec_count[store_time]

        return counter
