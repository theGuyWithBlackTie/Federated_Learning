## Setting Up the Code
There's nothing extra ordinary to be done to set-up the code. Just clone the repository and under <code>bert_finetuning</code> folder execute the following commands on the terminal.
```
# Creates hidden folder to be used by pipenv to create virtual environment.
mkdir .venv

# Automatically reads Pipfile and installs all the packages
pipenv instal 
```

Note: You need to have <code>pipenv</code> installed in the system.


## Running the Code
You need to append <code>src</code> folder in the <code>$PYTHONPATH</code> environment variable for <code>flwr</code> to identify it before building the <code>flwr</code> app.
```
export PYTHON="<FULLPATH>/federated_learning/bert_finetuning/src/"

# Run the app with default CPU federation
flwr run .

# OR Run the app with GPU simulation
flwr run . local-simulation-gpu
```