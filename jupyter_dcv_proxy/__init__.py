import getpass
import os
import pwd
import shutil
import uuid


def get_dcv_executable(prog):
    if shutil.which(prog):
        return prog

    raise FileNotFoundError(f'Could not find {prog} in PATH')


def get_icon_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'dcv.svg'
    )


def rewrite_auth(response, request):
    '''
    '''
    return


def get_system_user():
    try:
        user = pwd.getpwuid(os.getuid())[0]
    except:
        user = os.environ.get('NB_USER', getpass.getuser())
    return user


def setup_dcv():
    def _get_env(port):
        return dict(USER=get_system_user())


def setup_dcv():
    def _get_env(port):
        return {
        }

    def _get_cmd(port):
        session_id = str(uuid.uuid4())
        user = get_system_user()
        dcv_exec = get_dcv_executable('dcv')
        configurable_http_proxy_command = get_dcv_executable('configurable-http-proxy')
        command = f"""{dcv_exec} create-session --owner {user} {session_id}; {configurable_http_proxy_command} --port {port} --default-target=https://localhost:8443 --insecure --log-level=debug"""
        return command.split(" ")

    return {
        'command': _get_cmd,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'DCV',
            'icon_path': get_icon_path()
        }
    }
