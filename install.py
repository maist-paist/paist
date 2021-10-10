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
    subprocess.run(["git", "pull"], cwd="{0}/ReactJS".format(os.path.abspath("./")), shell=config.isWindows)
elif not os.path.exists('./ReactJS/package.json'):
    if os.path.exists("./ReactJS"):
        shutil.rmtree("./ReactJS/")
    os.makedirs("./ReactJS/")
    print(config.reactJSGitRepository)
    subprocess.run(["git", "clone", config.reactJSGitRepository, "ReactJS"])
    if git_remove:
        shutil.rmtree("./ReactJS/.git/")
        os.remove("./ReactJS/.gitignore")

if not os.path.exists('./ReactJS/node_modules'):
    # run 'npm install'
    subprocess.run(["npm", "install"], cwd="{0}/ReactJS".format(os.path.abspath("./")), shell=config.isWindows)