import mainenv
import gym

#Register Environment
gym.envs.registration.register(id="MegamanLol", entry_point="mainenv:MegamanEnv", max_episode_steps=9999999, reward_threshold=9999999, kwargs={}, nondeterministic=True)

env = gym.make("MegamanLol")

from nes_py.wrappers import JoypadSpace
from actions import BASE_ACTIONS
env = JoypadSpace(env, BASE_ACTIONS)

done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()

env.close()