#!/usr/bin/python3
'''fcreates and distributes an archive to your web servers, using deploy():
'''

import os

try:
    do_pack = __import__('1-pack_web_static').do_pack
    do_deploy = __import__('2-do_deploy_web_static').do_deploy
except ImportError as e:
    print(f"Error: {e}")


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
