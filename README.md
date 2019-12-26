# Calculus in Professional Practice
A school project
# Setup
## Linux/MacOS
```
git clone https://github.com/smitssjors/calculus-in-professional-practice.git
cd calculus-in-professional-practice
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```
## Windows
```
git clone https://github.com/smitssjors/calculus-in-professional-practice.git
cd calculus-in-professional-practice
python -m venv .venv
.venv/Scripts/activate.bat
pip install -r requirements.txt
python run.py
```
## Conda
```
conda create -n sjors_demo python=3.7.5
conda activate sjors_demo
git clone https://github.com/smitssjors/calculus-in-professional-practice.git
cd calculus-in-professional-practice
pip install -r requirements.txt
python run.py
```
Nadat je klaar ben bent
```
conda activate // Gaat trug naar de root environment
conda remove --name sjors_demo --all
```

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
