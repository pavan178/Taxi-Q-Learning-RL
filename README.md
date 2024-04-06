# OpenAI Taxi-V2 Player via Q-Learning

## Environment Methods:
- env.reset(): Resets the environment and returns a random initial state
- env.step(action): Steps the environment by one timestep. Returns:
- observation: Observation of the environment
- reward: If your action was beneficial or not
- done: Indicates if we have successfully picked up and dropped off a passenger, also called one episode
- info: Additional info such as performance and latency for debugging purposes
- env.render(): Renders one frame of the environment

## Using Reinforcement Learning
We are going to use a simple RL algorithm called Q-learning which will give our agent some memory. We use a Q-table with Q-values (Q: quality) that states the quality of a state-action-combination.

The Q-values are initialized to arbitrary values, and as the agent exposes itself to the environment and receives different rewards by executing different actions, the Q-values are updated using the equation:

```Q(state, action) = (1−α)Q(state, action) + α(reward + γ*max_a {Q(next state,all actions)})```

The Q-table is a matrix where we have a row for every state (500) and a column for every action (6). It's first initialized to 0, and then values are updated after training. Note that the Q-table has the same dimensions as the reward table, but it has a completely different purpose.

After enough random exploration of actions, the Q-values tend to converge serving our agent as an action-value function which it can exploit to pick the most optimal action from a given state.

There's a tradeoff between exploration (choosing a random action) and exploitation (choosing actions based on already learned Q-values). We want to prevent the action from always taking the same route, and possibly overfitting, so we'll be introducing another parameter called ϵ "epsilon" to cater to this during training.
