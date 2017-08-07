import numpy as np
import gym
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr


def rargmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector ==m)[0]
    return pr.choice(indices)

env = gym.make('FrozenLake-v0')

Q = np.zeros([env.observation_space.n, env.action_space.n])
# 16 x 4 array
learning_rate = .85
dis = .99
num_episodes = 2000

rList = []
for i in range(num_episodes):
    # decaying E-greedy
    # e = 1. / ((i/100)+1)
    state = env.reset()
    rAll = 0
    done = False

    while not done:

        # decaying E-greedy
        # if np.random.rand(1) < e:
        #     action = env.action_space.sample()
        # else:
        #     action = np.argmax(Q[state, :])

        action = np.argmax(Q[state, :]
        + np.random.randn(1, env.action_space.n) / (i+1))

        new_state, reward, done,_ = env.step(action)

        Q[state, action] = (1 - learning_rate) * Q[state, action] + learning_rate*(reward + dis * np.max(Q[new_state, :]))
        rAll += reward
        state = new_state

    rList.append(rAll)


print("success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)
plt.bar(range(len(rList)), rList, color = "blue")
plt.show
