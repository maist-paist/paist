import os
import subprocess
import shutil
from config import config

print("remove all dist files")

if os.path.exists("./temp"):
    shutil.rmtree("./temp")

if os.path.exists("./dist"):
    shutil.rmtree("./dist")

print("create new building files")

os.makedirs("./temp")

shutil.copytree("./backend/", "./temp/backend/")

subprocess.run(["npm", "run", "build"], cwd="{0}/ReactJS".format(os.path.abspath("./")), shell=config.isWindows)

shutil.copytree("./ReactJS/build/", "./temp/frontend/")

shutil.copy("./app.py", "./temp/")
shutil.copy("./config.py", "./temp/")

# subprocess.run(["cd", "./temp"])
subprocess.Popen(["pyinstaller", "--onefile", "--windowed", "--add-data", "temp/frontend{0}frontend".format(";" if config.isWindows else ":"), "./temp/app.py"])
# subprocess.run(["cd", ".."])
# shutil.copytree("./temp/dist/", "./dist/")

print("build was complete")