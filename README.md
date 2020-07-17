# Adaptive Online Planning on a microgrid environment
Applying AOP and other agents (Lu et al. 2019), on a microgrid simulator environment.

## Current status
Repo ready to experiment on large scale

## Installation
Run the `install.sh` file

``` ./install.sh ```

## Usage
Run an aop agent on the microgrid environment using 

```
source aopmgenv/bin/activate
python run.py -a aop -e microgrid -s standard -c 1
```

Run several agents using

```
python do_experiments.py --algos aop ppo td3
```

Then plot it 
```
python graph.py ex/ 4
```
Replace 4 with the number of steps you ran the experiments for (can be changed in params/env_params.py)

!several agents for 4 timesteps(https://github.com/TheSpaceSheep/aop/blob/master/rewards.png?raw=true)
