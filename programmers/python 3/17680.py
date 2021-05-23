# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = []

    times = 0
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            times += 1
        else:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
            times += 5

    return times