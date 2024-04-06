# -*- coding: utf-8 -*-
"""Taxi-V2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TmE4i36YJnkTO0X3MiAkR2wfkRqJKYHQ

### OpenAI Taxi-V2 Player via Q-Learning

#### Load Environment
"""

# IMPORT MODULES
# Import Numpy, Gym etc
import numpy as np
import gym
import random
print('Import Modules')

# CREATE ENVIRONMENT
# Load Taxi-V2 Environment
# In this Environment the Yellow Square represents the Taxi, the (“|”) represents a Wall, the Blue Letter represents the Pick-Up Location, and the Purple letter is the Drop-Off Location. The Taxi will turn Green when it has a Passenger Aboard.

Env = gym.make("Taxi-v3").env

state = Env.encode(1, 1,3, 2)
print("State:", state)

Env.s = state


Env.render()

print('Load Taxi-V3 Environment')
print('In this Environment the Yellow Square represents the Taxi, the (“|”) represents a Wall.')
print('The Blue Letter represents the Pick-Up Location, and the Purple letter is the Drop-Off Location.')
print('The Taxi will turn Green when it has a Passenger Aboard.')
print('The Environment gives a -1 Reward for each Step in order for the Agent to try and find the quickest solution.')
print('The Environment gives a -10 Reward if Agent incorrectly Picks Up or Drops Off a Passenger.')
print('The Environment gives a 20 Reward on Success')

# LOAD ENVIRONMENT
# Explore Environment
ActionSize=Env.action_space.n
print("Action Size ",ActionSize)
StateSize=Env.observation_space.n
print("State Size ",StateSize)

"""#### Initialization"""

# INITIALIZATION
# Initialize Q-Table
QTable=np.zeros((StateSize,ActionSize))
print(QTable)

# INITIALIZATION
# Add Hyper-Parameters Episodes
TotalEpisodes=50000        # Total Episodes
TotalTestEpisodes=1        # Total Test Episodes
MaxSteps=99                # Max Steps per Episode

# Add Hyper-Parameters Bellman Equation
LearningRate=0.7           # Learning Rate
Gamma=0.618                # Discounting Rate

# Add Exploration Parameters
Epsilon=1.0                # Exploration rate
MaxEpsilon=1.0             # Exploration probability at start
MinEpsilon=0.01            # Minimum exploration probability
DecayRate=0.01             # Exponential decay rate for exploration prob
print('Add Hyper-Parameters')

"""#### Q-Learning"""

# Q-LEARNING
# Perform Learning for each Episode
for Episode in range(TotalEpisodes):
    # Reset the Environment
    State=Env.reset()
    State = Env.encode(1, 1, 3, 2)
    Step=0
    Done=False

    # Perform Temporal Difference Learning for each Step
    for Step in range(MaxSteps):
        # Choose an Action (A) in Current World State (S)
        # First Randomize a Number
        ExploreExploitTradeoff=random.uniform(0,1)

        # Check if this number is Greater than Epsilon, Then Exploitation (Take the Biggest Q-Value for this State)
        if ExploreExploitTradeoff > Epsilon:
            Action=np.argmax(QTable[State,:])

        # Otherwise Exploration (Perform a Random Action)
        else:
            Action=Env.action_space.sample()

        # Take the Action (A) and Observe the Outcome State(S') and Reward (R)
        NewState,Reward,Done,Info=Env.step(Action)

        # Update Q(S,A):= Q(S,A) + Learning Rate * [R(S,A) + Gamma * Max Q(S',A') - Q(S,A)]
        QTable[State,Action]=QTable[State,Action]+LearningRate*(Reward+Gamma*np.max(QTable[NewState,:])-QTable[State,Action])

        # Update State
        State=NewState

        # Check if Episode is Finished
        if Done==True:
            break

    # Increment Episode
    Episode+=1

    # Reduce Epsilon (We Need Less and Less Exploration after each Episode)
    Epsilon=MinEpsilon+(MaxEpsilon-MinEpsilon)*np.exp(-DecayRate*Episode)

# Print Final Q-Table
print(QTable)

"""#### Test"""

# TEST
# Test the Q-Learning via Playing

State = Env.encode(1, 1, 3, 2)

Rewards=[]

# Run Player for each Episode
for Episode in range(TotalTestEpisodes):
    State=Env.reset()
    State = Env.encode(1, 1, 3, 2)
    Step=0
    Done=False
    TotalRewards=0
    print("")
    print("Episode ",Episode)
    for Step in range(MaxSteps):
        Env.render()
        # Take the Action (A) that have the Maximum Expected Future Reward given that State
        Action=np.argmax(QTable[State,:])

        # Update State
        NewState,Reward,Done,Info=Env.step(Action)

        # Update Rewards
        TotalRewards +=Reward

        # Check if Task Completed
        if Done:
            Rewards.append(TotalRewards)
            print ("Score ",TotalRewards)
            break

        # Update State
        State=NewState

# Close Environment
Env.close()
print ("Score Over Time: "+str(sum(Rewards)/TotalTestEpisodes))

# Commented out IPython magic to ensure Python compatibility.
# %%time
# """Training the agent"""
# 
# import random
# from IPython.display import clear_output
# 
# # Hyperparameters
# alpha = 0.1
# gamma = 0.6
# epsilon = 0.1
# max_steps = 99
# total_test_episodes = 100
# 
# # For plotting metrics
# all_epochs = []
# all_penalties = []
# 
# for i in range(1, 100001):
#     state = env.reset()
# 
#     epochs, penalties, reward, = 0, 0, 0
#     done = False
# 
#     while not done:
#         if random.uniform(0, 1) < epsilon:
#             action = env.action_space.sample() # Explore action space
#         else:
#             action = np.argmax(q_table[state]) # Exploit learned values
# 
#         next_state, reward, done, info = env.step(action)
# 
#         old_value = q_table[state, action]
#         next_max = np.max(q_table[next_state])
# 
#         new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
#         q_table[state, action] = new_value
# 
#         if reward == -10:  #computing rewards and penalties
#             penalties += 1
# 
#         state = next_state
#         epochs += 1
# 
#     if i % 100 == 0:
#         clear_output(wait=True)
#         print("Episode:",{i})
# 
# print("Training finished.\n")

#evaluate the agent's performance

from IPython.display import clear_output
from time import sleep


env.reset()


rewards = []

for episode in range(total_test_episodes):
    state = env.reset()
    env.encode(1, 1, 3, 2)

    step = 0
    done = False
    total_rewards = 0
    print("****************************************************")
    print("EPISODE ", episode)

    for step in range(max_steps):
        #  The AGENT is PLAYING
        env.render()
        # Take the action (index) that have the maximum expected future reward given that state
        action = np.argmax(q_table[state])

        new_state, reward, done, info = env.step(action)
        total_rewards += reward
        if done:
            rewards.append(total_rewards)
            print ("Score", total_rewards)
            break
        state = new_state
env.close()
print ("Score over time: " +  str(sum(rewards)/total_test_episodes))