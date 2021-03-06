import numpy as np

with open('inputs/input_12.txt', 'r') as infile:
    moves = infile.read().split()

position = np.array([0, 0])
direction = np.array([1, 0])

card2vec = {'E': np.array([1, 0]), 'W': np.array([-1, 0]),
            'N': np.array([0, 1]), 'S': np.array([0, -1])}
dir2sign = {'L': +1, 'R': -1}


def turn(deg: int, rot_dir: str, cur_dir: np.ndarray) -> np.ndarray:
    rad = dir2sign[rot_dir] * np.pi * deg / 180
    rotation = np.array([[np.cos(rad), -np.sin(rad)],
                         [np.sin(rad), np.cos(rad)]])
    cur_dir = np.rint(np.matmul(rotation, cur_dir)).astype(int)
    return cur_dir


for line in moves:
    command = line[0]
    value = int(line[1:])
    if command in card2vec.keys():
        position += value * card2vec[command]
    elif command == 'F':
        position += value * direction
    elif command in dir2sign.keys():
        direction = turn(value, command, direction)
    else:
        raise ValueError(f'Could not understand command {line}')

print(np.abs(position).sum())
