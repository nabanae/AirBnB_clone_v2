#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
using the function do_deploy
"""
from fabric.api import env, run, put, hosts
# from datetime import datetime
import os

env.hosts = ['35.74.43.78', '36.126.181.52']


def do_deploy(archive_path):
    """
    upload the archive to the /tmp/ directory of the web server
    uncompress the archive
    delete the archive from the web server
    handle symbolic links
    return True is all operations went well, False otherwise
    """
    if not os.path.exists(archive_path):
        return False
    try:
