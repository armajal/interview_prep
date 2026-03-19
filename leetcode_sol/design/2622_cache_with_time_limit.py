import datetime as dt

class cache_with_time_limit:
    def __init__(self):
        self.cache = {}
        
    
    def get(self, key:str) -> bool:
        if key in self.cache and dt.datetime.now() < self.cache[key][1]:
            return self.cache[key][0]
        return -1
    
    def set(self, key: str, value: str, duration: int) -> bool:
        unexpired = key in self.cache and dt.datetime.now() < self.cache[key][1]

        time_expiration = dt.datetime.now() + dt.timedelta(milliseconds=duration)
        self.cache[key] = [value, time_expiration]
        return unexpired
            
    def count(self):
        return sum(1 for k,v in self.cache.items() if dt.datetime.now() < v[1])

cwtl = cache_with_time_limit()
print(cwtl.set(1,42, 100))
print(cwtl.get(1))
print(cwtl.count())
print(cwtl.get(1))