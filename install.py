"""
Install basic PAIST setting
:author Chanwoo Gwon, YonseiUniv. Researcher, since 2020.05. ~
:Date 2021.09.29
"""
import subprocess
from config import config
import os
import shutil

# install requirement package
subprocess.run(["pip", "install", "-r", "requirement.txt"])

git_remove = config.removeReactJsGit

# clone or update git repository
if not git_remove and os.path.exists('./ReactJS/package.json'):
    subprocess.run(["cd", "./ReactJS"])
    subprocess.run(["git", "pull"])
    subprocess.run(["cd", ".."])  # back to the root
else:
    shutil.rmtree("./ReactJS/")
    os.makedirs("./ReactJS/")
    subprocess.run(["git", "clone", config.reactJSGitRepository, "ReactJS"])
    if git_remove:
        shutil.rmtree("./ReactJS/.git/")
        os.remove("./ReactJS/.gitignore")

if not os.path.exists('./ReactJS/node_modules'):
    # run 'npm install'
    subprocess.run(["npm", "install", "--prefix", "./ReactJS"])