Created a conda env 
```bash
conda create -n Winequa python=3.7 -y
```
```bash
conda activate Winequa
```
created requirements file

install the requirements.txt
```bash
pip install -r requirements.txt
```
Download the data 

git init

dvc init
```bash
download datasets from "https://archive.ics.uci.edu/ml/datasets/wine+quality"
```

dvc add data_given/winequality.csv
```bash
git add .
```
```bash
git commit -m "First commit"
```
```bash
online updates for readme gitadd. && git commit -m "README.md updated"
```
```bash
git branch -M main
```
```bash
git remote add origin https://github.com/sureshmami/Simple-MLops-with-dvc.git
```
```bash
git push -u origin main
```
```bash
Created configuration file "params.yaml" for our project
```
tox command - 
```bash
tox
```
for rebuilding -
```bash
tox -r
```
pytest -
```bash
pytest -v
```
setup commands - 
```bash
pip install -e .
```

build your own package commands -
```bash
python setup.py sdist bdist_wheel
```

