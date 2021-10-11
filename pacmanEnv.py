
import random
import json
import gym
from gym import spaces
import pandas as pd
import numpy as np
import keyboard

keyboard_keys = ["down","up","left","right"]

MAX_REWARD = 100000
N_DISCRETE_ACTIONS = 4



MAX_NUM_SHARES = 2147483647
MAX_SHARE_PRICE = 5000
MAX_OPEN_POSITIONS = 5
MAX_STEPS = 20000



class PacManEnv(gym.Env):
    """A stock trading environment for OpenAI gym"""
    metadata = {'render.modes': ['human']}

    def __init__(self,game):
        super(PacManEnv, self).__init__()

        self.game = game

        self.saved_score = self.game.score
        self.saved_lives = self.game.lives

        self.reward_range = (0, MAX_REWARD)

        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

        self.observation_space = spaces.Box(
            low=0, high=1, shape=(6, 6), dtype=np.float16)
            

    def _next_observation(self):
        
        ########################################################################

        return obs

    def _take_action(self, action):
        if action == 0:
            keyboard.press_and_release('down')
        elif action == 1:
            keyboard.press_and_release('up')
        elif action == 2:
            keyboard.press_and_release('left')
        elif action == 3:
            keyboard.press_and_release('right')
        else:
            print("something went wrong, _take_action()")
        
        self.game.update()
            
    def step(self, action):
        # Execute one time step within the environment
        self._take_action(action)

        

        if self.current_step > len(self.df.loc[:, 'Open'].values) - 6:
            self.current_step = 0

        delay_modifier = (self.current_step / MAX_STEPS)

        reward = self.balance * delay_modifier
        done = self.net_worth <= 0

        obs = self._next_observation()

        return obs, reward, done, {}

    def reset(self):
        self.game.restartGame()
        self.saved_score = self.game.score
        self.saved_lives = self.game.lives

        return self._next_observation()

    def render(self, mode='human', close=False):
        self.game.rendering = 1

    def _get_reward(self):
        score_diff = self.game.score  - self.saved_score


