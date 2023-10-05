#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
from fabric.api import local, env, run, put, hosts
from datetime import datetime
import os

env.hosts = ['35.74.43.78', '36.126.181.52']


def do_pack():
    """
    create the archive file with the contents of the web_static folder
    and return the archive path if the archive has been correctly generated
    otherwise return None
    """
    datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(datetime_str)
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(file_name))
