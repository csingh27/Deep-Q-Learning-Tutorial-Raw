# A1 Environment

# A1.1 Install and import gymnasium
import gymnasium as gym

# A1.2 Create Breakout environment
env = gym.make('BreakoutDeterministic-v4')

# A1.3 Reset environment
episodes = 50000

# A2 Frame pre-processing
import cv2
import numpy as np
def frame_preprocess(obs):

    new_width = 110
    new_height = 84

    frame = np.asarray(obs[0])

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    downsampled_frame = cv2.resize(gray_frame, (110, 84))

    state = downsampled_frame[:,13:97]
    
    return state

for i in range(episodes):

    observation = env.reset()

    state = frame_preprocess(observation)

    cv2.imshow("Frame", state)
    cv2.waitKey(0)

    done = False

    # 0 NOOP (No action)
    # 1 FIRE
    # 2 RIGHT
    # 3 LEFT

    action = env.action_space.sample()

    while not done:
        state, reward, done, truncate, info = env.step(action)
