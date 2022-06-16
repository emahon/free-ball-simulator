import argparse
import random

parser = argparse.ArgumentParser(description='Check how many free balls are gotten.')
parser.add_argument('balls', type=int, help='the initial number of balls')
parser.add_argument('trials', type=int, help='the number of times to run the simulation')
parser.add_argument('probability', type=float, help='the probability of a free ball')

args = parser.parse_args()

for i in range(args.trials):
    print("Trial " + str(i+1))
    num_balls = args.balls    
    free_balls = 0
    while num_balls > 0:
        num_balls = num_balls - 1
        if random.random() <= args.probability:
            free_balls = free_balls + 1
            num_balls = num_balls + 1
    print("Free balls given: " + str(free_balls))
