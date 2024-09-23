
class RainSolution:
    def __init__(self):
        self.rains = []

    def addRainRate(self, start_time, end_time, rate):
        self.rains.append((start_time, end_time, rate))

    def getRainRate(self, time):
        rain_rate = 0
        for rain in self.rains:
            if rain[0] <= time < rain[1]:
                rain_rate += rain[2]
        return rain_rate

    def getRainAccumulation(self, start_sec, end_sec):
        accumation = 0
        for sec in range(start_sec, end_sec):
            rain_rate = self.getRainRate(sec)
            accumation += rain_rate
        return accumation


r = RainSolution()

r.addRainRate(20, 70, 300)
r.addRainRate(50, 60, 100)
r.addRainRate(10, 40, 200)


total_accumation = r.getRainAccumulation(30, 60)

print(total_accumation)

# print(r.rains)
# result = r.getRainRate(30)
# print(result)