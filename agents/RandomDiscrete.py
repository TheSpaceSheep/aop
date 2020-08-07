from agents.Agent import Agent
import gym



class RandomDiscrete(Agent):
    """ An agent that takes actions in an environment
    with a discrete action space """
    def __init__(self, params):
        super(RandomDiscrete, self).__init__(params)
        assert isinstance(self.env, gym.Env)

    def get_action(self):
        """ get a random action """
        return self.env.action_space.sample()
