echo [$(date)]:"START"
echo [$(date)]:"Creating conda envn with python 3.8"
conda create --prefix ./env_ren python=3.8 -y
echo [$(date)]:"activate env"
source activate ./env_ren
echo [$(date)]:"dev requirements intalling"
pip install -r requirements_dev.txt
echo [$(date)]:"finished"
