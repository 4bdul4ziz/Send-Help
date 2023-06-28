import numpy as np
import random
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Diamond-Square Algorithm')
parser.add_argument('seed', type=int, help='Random seed')
parser.add_argument('offset_change', type=int, help='Offset change by order of magnitude as depth increases')
args = parser.parse_args()

# Set random seed
random.seed(args.seed)

# Set up map and corner values
size = 33
map = np.zeros((size, size))
map[0, 0] = random.randint(0, 255)
map[0, size-1] = random.randint(0, 255)
map[size-1, 0] = random.randint(0, 255)
map[size-1, size-1] = random.randint(0, 255)

# Recursive function for diamond-square algorithm
def diamond_square(map, x, y, size, offset):
    if size < 2:
        return

    # Diamond step
    map[x+size//2, y+size//2] = (map[x, y] + map[x+size, y] + map[x, y+size] + map[x+size, y+size]) / 4 + random.randint(-offset, offset)

    # Square step
    map[x+size//2, y] = (map[x, y] + map[x+size, y] + map[x+size//2, y+size//2]) / 3 + random.randint(-offset, offset)
    map[x, y+size//2] = (map[x, y] + map[x, y+size] + map[x+size//2, y+size//2]) / 3 + random.randint(-offset, offset)
    map[x+size, y+size//2] = (map[x+size, y] + map[x+size, y+size] + map[x+size//2, y+size//2]) / 3 + random.randint(-offset, offset)
    map[x+size//2, y+size] = (map[x, y+size] + map[x+size, y+size] + map[x+size//2, y+size//2]) / 3 + random.randint(-offset, offset)

    # Recur four times with new corners
    diamond_square(map, x, y, size//2, offset//args.offset_change)
    diamond_square(map, x+size//2, y, size//2, offset//args.offset_change)
    diamond_square(map, x, y+size//2, size//2, offset//args.offset_change)
    diamond_square(map, x+size//2, y+size//2, size//2, offset//args.offset_change)

# Run diamond-square algorithm
diamond_square(map, 0, 0, size-1, 16)

# Define color partitions
partitions = [
    {'min': -np.inf, 'max': 50, 'color': WATER_COLOR, 'symbol': WATER_SYMBOL},
    {'min': 50, 'max': 100, 'color': BEACH_COLOR, 'symbol': BEACH_SYMBOL},
    {'min': 100, 'max': 200, 'color': GRASS_COLOR, 'symbol': GRASS_SYMBOL},
    {'min': 200, 'max': np.inf, 'color': SNOW_COLOR, 'symbol': SNOW_SYMBOL}
]

def draw_map(map, partitions):
    for y in range(size):
        for x in range(size):
            for partition in partitions:
                if map[y, x] >= partition['min'] and map[y, x] < partition['max']:
                    print(partition['symbol'], end='')
                    break
        print()

draw_map(map, partitions)

