import argparse
import sys
import gym
from nes_py.wrappers import JoypadSpace
from nes_py.app.play_human import play_human
from nes_py.app.play_random import play_random
from ..actions import BASE_ACTIONS, SECONDARY_ACTIONS

ACTION_GROUPS = {
    'base': BASE_ACTIONS,
    'secondary': SECONDARY_ACTIONS
}
