echo [$(date)]:"START"
echo [$(date)]:"Creating environment"
conda create --prefix ./env python=3.8 -y

echo [$(date)]:"Activating env"
conda activate ./env

echo [$(date)]:"Intsalling dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]:"END"