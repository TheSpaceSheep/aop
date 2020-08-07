# Adaptive Online Planning on a microgrid environment
Applying AOP and other agents (Lu et al. 2019), on a microgrid simulator environment.

## Current status
Repo ready to experiment on large scale

## Installation
Run the `install.sh` file

``` ./install.sh ```

## Quick usage
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

## Usage

Make sure the aopmgenv virtual environment is activated
```
python do_experiments.py [--algos {all,aop,aop-bc,polo,td3,ppo,mpc-8,mpc-3}]          # defaults to all, can take several arguments  
                         [--env {maze-d,maze-s,microgrid}]                            # defaults to microgrid
                         [--setting {changing,novel,standard,discrete,continuous}]    # use continuous for the microgrid
                         [--output_dir OUTPUT_DIR]
```

Results are stored in the output folder (```./ex/``` by default), with a subfolder specific to the date. You can simultaneously plot all the results stored in the output folder using.

```
python graph.py <folder-name> <lifetime-length>
```

Folder name should be ex/ if you didn't specify an output folder, and lifetime-length should be the same one you ran the experiments with (can be changed in params/env_params.py, by modifying the ```T``` and ```save_freq``` parameter).

![several agents for 4 timesteps](https://github.com/TheSpaceSheep/aop/blob/master/rewards.png?raw=true)
