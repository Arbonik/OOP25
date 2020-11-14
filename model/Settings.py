from random import Random


# Диапазон времени заселения
# 4 = одна секунда

LONG_MODELING = 10
DELTA_TIME = 1000
# Количество комнат в отеле
ROOM_QUNTITY = 10

def timeLife():
    # заселение на от 1 DELTA_TIME до 5
    return Random().randint(4, 20)