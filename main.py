# A1 Environment

# A1.1 Install and import gymnasium
import gymnasium as gym

# A1.2 Create Breakout environment
env = gym.make('BreakoutDeterministic-v4')

# A1.3 Reset environment
episodes = 1

# A2 Frame pre-processing
import cv2
import numpy as np
def frame_preprocess(obs):

    # A2.1 Define the new height and width
    new_width = 110
    new_height = 84

    # A2.2 Define frame as array
    frame = np.asarray(obs[0])

    # A2.3 Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # A2.4 Resize frame
    downsampled_frame = cv2.resize(gray_frame, (110, 84))

    # A2.5 Crop frame to 84x84
    state = downsampled_frame[:,13:97]
    
    return state

# A1.5 Define RL loop
for i in range(episodes):

    # A1.6 Reset environment
    observation = env.reset()

    # A2 Frame pre-processing
    state = frame_preprocess(observation)
    print(state.shape)

    cv2.imshow("Frame", state)
    cv2.waitKey(0)

    done = False

    # 0 NOOP (No action)
    # 1 FIRE
    # 2 RIGHT
    # 3 LEFT

    # A1.8 Define random action
    action = env.action_space.sample()

    while not done:
        # A1.9 Take step
        state, reward, done, truncate, info = env.step(action)

        # A2.6 Preprocess frame
        next_state = frame_preprocess(state)
        print(next_state.shape)
        exit()
