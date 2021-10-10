import platform


class Config:
    name = "PAIST 3DEditor"
    version = "0.0.1"
    reactJSGitRepository = "https://github.com/KChanwoo/react-default-app.git"
    removeReactJsGit = True
    reactJSDevWebPort = 3000
    isWindows = platform.system() == "Windows"

config = Config()