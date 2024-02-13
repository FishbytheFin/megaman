import mainenv
import gym

#Register Environment
gym.envs.registration.register(id="MegamanLol", entry_point="mainenv", max_episode_steps=9999999, reward_threshold=9999999, kwargs=[], nondeterministic=True)

env = gym.make("MegamanLol")