import getpass
import os
import pwd
import shutil
import uuid


def get_dcv_executable(prog):
    if shutil.which(prog):
        return prog

    raise FileNotFoundError(f"Could not find {prog} in PATH")


def get_icon_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons", "dcv.svg")


def rewrite_auth(response, request):
    """ """
    return


def get_system_user():
    try:
        user = pwd.getpwuid(os.getuid())[0]
    except:
        user = os.environ.get("NB_USER", getpass.getuser())
    return user


def setup_dcv():
    def _get_env(port):
        return dict(
            PORT=str(port), NB_USER=get_system_user(), SESSION_ID=str(uuid.uuid4())
        )

    def _get_cmd(port):
        dcv_exec = get_dcv_executable("dcv")
        configurable_http_proxy_command = get_dcv_executable("configurable-http-proxy")
        this_dir = os.path.abspath(os.path.dirname(__file__))
        command = f"""bash {this_dir}/run-dcv-user-session.sh"""
        return command.split(" ")

    return {
        "command": _get_cmd,
        "environment": _get_env,
        "timeout": 120,
        "launcher_entry": {
            "title": "DCV",
            # the icon doesn't display
            # "icon_path": get_icon_path()
        },
    }


from . import _version

__version__ = _version.get_versions()["version"]
