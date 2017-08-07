import numpy as np
import gym
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr

import readchar

#MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

#Key mapping
arrow_keys ={
'\x1b[A' : UP,
'\x1b[B' : DOWN,
'\x1b[C' : RIGHT,
'\x1b[b' : LEFT
}

# register(
#     id='FrozenLake-v3',
#     entry_point = 'gym.envs.toy_text:FrozenLakeEnv',
#     kwargs = {'map_name': '4x4',
#                 'is_slippery' : False}
# )
# env = gym.make('FrozenLake-v3')
env = gym.make('FrozenLake-v0')
env.render()

#before calling step method, call reset()
state = env.reset()

while True:
    key = readchar.readkey()
    if key not in arrow_keys.keys():
        print("Game aborted")
        break

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print("state: ",state, "Action: ",action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward". reward)
        break
