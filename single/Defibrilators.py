import sys
import math


def num(x):
    return x.replace(",",".")


def distance(lat_a, lon_a, lat_b, lon_b):
    x = (lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
    y = lat_b - lat_a
    return math.sqrt(x**2 + y**2) * 6371


lon = float(num(input()))
lat = float(num(input()))

min_dist = sys.maxsize
min_place = ""

for i in range(int(input())):
    info = input().split(";")
    lon_tmp = float(num(info[-2]))
    lat_tmp = float(num(info[-1]))
    dist = distance(lat, lon, lat_tmp, lon_tmp)
    if dist < min_dist:
        min_dist = dist
        min_place = info[1]

print(min_place)
