#!/usr/bin/python3
'''
fabric script to distribute an archive to web servers
'''

# import os
# from datetime import datetime
# from fabric.api import env, local, put, run, runs_once


# env.hosts = ['34.232.72.158', '34.224.83.81']


# def do_deploy(archive_path):
#     """Deploys the static files to the host servers.
#     Args:
#         archive_path (str): The path to the archived static files.
#     """
#     if not os.path.exists(archive_path):
#         return False
#     file_name = os.path.basename(archive_path)
#     folder_name = file_name.replace(".tgz", "")
#     folder_path = "/data/web_static/releases/{}/".format(folder_name)
#     success = False
#     try:
#         put(archive_path, "/tmp/{}".format(file_name))
#         run("mkdir -p {}".format(folder_path))
#         run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
#         run("rm -rf /tmp/{}".format(file_name))
#         run("mv {}web_static/* {}".format(folder_path, folder_path))
#         run("rm -rf {}web_static".format(folder_path))
#         run("rm -rf /data/web_static/current")
#         run("ln -s {} /data/web_static/current".format(folder_path))
#         print('New version deployed!')
#         success = True
#     except Exception:
#         success = False
#     return success

import os
from fabric.api import env, put, run


env.user = 'ubuntu'
env.hosts = ['34.232.72.158', '34.224.83.81']
env.warn_only = True


def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not os.path.isfile(archive_path):
        return False

    try:
        # Upload the archive to the '/tmp/' directory on the web servers
        put(archive_path, '/tmp/')

        # Extract the archive to the releases directory
        archive_filename = os.path.basename(archive_path)
        release_name = os.path.splitext(archive_filename)[0]
        release_path = '/data/web_static/releases'

        run(f'mkdir -p {release_path}/{release_name}/')
        run('tar -xzf /tmp/{} -C {}/{}/'
            .format(archive_filename, release_path, release_name))

        # Delete the archive from the web servers
        run(f'rm /tmp/{archive_filename}')

        # Move web_static files to web_static current version directory
        move_command = (f'mv {release_path}/{release_name}/web_static/* '
                        f'{release_path}/{release_name}/')
        run(move_command)
        run(f'rm -rf {release_path}/{release_name}/web_static')

        # Delete the symbolic link '/data/web_static/current' if exists
        current_symlink = '/data/web_static/current'
        run(f'rm -rf {current_symlink}')

        # Create a new symbolic link to the new version
        new_symlink = f'{release_path}/{release_name}'
        run(f'ln -s {new_symlink} {current_symlink}')

        print("New version deployed!")
        return True
    except Exception:
        return False
