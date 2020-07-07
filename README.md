# Adaptive Online Planning on a microgrid environment
Applying an AOP agent (Lu et al. 2019), on a microgrid simulator environment.

## Current status
Successfully merged the two repos, setting up for experiments and plotting.

## Installation
Run the `install.sh` file

``` ./install.sh ```

Run an aop agent on the microgrid environment using 

```
source aopmgenv/bin/activate
python3 run.py -a aop -e microgrid -s standard -c 1
```
