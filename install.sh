python3 -m venv aopmgenv
source aopmgenv/bin/activate

python -m pip install --upgrade pip setuptools
pip install -r requirements.txt

git submodule init
git submodule update
pip install -e envs/microgrids_rl_new
