import argparse
import copy

import params.default_params as default_params
import params.env_params as env_params

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algos', '-a', nargs='+', type=str, default='all',
        choices=['all', 'aop', 'aop-bc', 'polo', 'td3', 'ppo', 'mpc-8', 'mpc-3'])
    parser.add_argument('--env', '-e', type=str, default='microgrid',
        choices=['hopper', 'ant', 'maze-d', 'maze-s', 'microgrid'],
        help='Base environment for agents')
    parser.add_argument('--setting', '-s', type=str, default='continuous',
        choices=['changing', 'novel', 'standard', 'discrete', 'continuous'],
        help='Specify which setting to test in')
    parser.add_argument('--output_dir', '-d', type=str,
        help='Directory to store outputs')
    parser.add_argument('--num_trials', '-n', type=int, default=1,
        help='Number of trials (seeds) to run for')
    parser.add_argument('--num_cpus', '-c', type=int, default=1,
        help='Number of CPUs to use for trajectory generation')
    parser.add_argument('--use_gpu', '-g', default=True,
        help='Whether or not to use GPU (currently only TD3 supports this)')
    parser.add_argument('--test_pol', '-t', default=True,
        help='Whether or not to test the policy in standard episode')

    args = parser.parse_args()

    if not is_valid_env(args.env, args.setting):
        print('Environment \"%s %s\" is not supported, terminating'
                % (args.setting, args.env))
        return

    # Basic information for experiments
    if 'all' in args.algos:
        args.algos = ['aop', 'aop-bc', 'polo', 'td3', 'ppo', 'mpc-8', 'mpc-3']
    agent_classes = []
    for algo in args.algos:
        agent_classes.append(get_agent_class(algo))

    output_dir = args.output_dir if args.output_dir else default_output_dir()

    # Setting parameter settings for experiments

    params = copy.deepcopy(default_params.base_params)
    params.update(env_params.env_params[args.env][args.setting])

    params['env']['setting'] = args.setting
    params['problem']['output_dir'] = output_dir

    params['mpc']['num_cpu'] = args.num_cpus
    params['pg']['num_cpu'] = args.num_cpus

    params['problem']['test_pol'] = args.test_pol
    params['problem']['eval_len'] = 1000
    params['problem']['use_gpu'] = args.use_gpu


    # Setting environment-specific hyperparameter settings
    if args.env == 'maze-s':
        params['aop']['std_thres'] = 0
        params['aop']['bellman_thres'] = 0
    elif args.env == 'ant':
        params['aop']['ratio_thres'] = .01
        params['aop']['init_thres'] = -1

    if 'maze' in args.env:
        params['p-td3']['hs'] = [64,64]
        params['p-bc']['hs'] = [64,64]
        params['td3']['hs'] = [64,64]


    # Run experiments with different agents
    for ag, algo in zip(agent_classes, args.algos):
        params['problem']['algo'] = algo
        # Setting algorithm-specific hyperparameter settings
        if algo == 'polo' or algo == 'mpc-3':
            params['mpc']['num_iter'] = 3

        for i in range(args.num_trials):
            params['problem']['dir_name'] = f'{output_dir}/{algo}_trial_{i}/'
            agent = ag(params)
            agent.run_lifetime()

    print('end of experiments')


def is_valid_env(env_name, setting):
    if env_name == 'hopper':
        return True
    elif env_name == 'ant' and setting in ['changing', 'standard']:
        return True
    elif 'maze' in env_name and setting in ['changing', 'novel']:
        return True
    elif env_name == 'microgrid':
        return True
    else:
        return False

def default_output_dir():
    import datetime
    now = datetime.datetime.now()
    ctime = '%02d%02d_%02d%02d' % (now.month, now.day, now.hour, now.minute)
    return 'ex/' + ctime

def get_agent_class(algo):
    if algo == 'aop':
        from agents.AOPTD3Agent import AOPTD3Agent
        agent_class = AOPTD3Agent
    elif algo == 'aop-bc':
        from agents.AOPBCAgent import AOPBCAgent
        agent_class = AOPBCAgent
    elif algo == 'polo':
        from agents.POLOAgent import POLOAgent
        agent_class = POLOAgent
    elif algo == 'td3':
        from agents.TD3Agent import TD3Agent
        agent_class = TD3Agent
    elif algo == 'ppo':
        from agents.PPOAgent import PPOAgent
        agent_class = PPOAgent
    elif algo == 'mpc-8' or algo == 'mpc-3':
        from agents.MPCAgent import MPCAgent
        agent_class = MPCAgent
    return agent_class



if __name__=='__main__':
    main()
