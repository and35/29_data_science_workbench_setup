import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
py_ver = "python"+"{{ cookiecutter.python_version }}"
print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

try:
    subprocess.call(['python3', '-m', 'pip', 'install', '--upgrade', 'pip']) #actualizamos o instalamos pip
    subprocess.call(['pip', 'install', 'virtualenv ']) #instalamos venv

    #subprocess.call(['virtualenv', '-p', py_ver,'venv']) # creamos el venv con una version especifica de python 
    subprocess.call(['virtualenv','venv'])
except ValueError as ev: 
    print("tuvimos el siguiente error: ", ev, "fue durante la creacion del ambiente con venv")
# subprocess.call(['conda', 'env', 'create','--file','environment.yml'])

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")