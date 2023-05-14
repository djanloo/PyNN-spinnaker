"""Explore the server tree and API"""
import os

env_folder = os.getcwd()

file_tree = os.path.join(env_folder, 'filetree.txt')
module_tree = os.path.join(env_folder, 'moduletree.txt')
installation_log_file = os.path.join(env_folder, 'install_log.txt')
pipfreeze = os.path.join(env_folder, 'pipfreeze.txt')
# Explore remote folders
# os.chdir("../")
os.system(f"python -m dirtree '..' > {file_tree}")
os.system(f"pip freeze > {pipfreeze}")

# Eplore the remote API
os.system(f"pip install inspectshow dirtree > {installation_log_file}")
os.system(f"python -m inspectshow pyNN.spiNNaker > {module_tree}")

# Goes back to environment directory
os.chdir(env_folder)





