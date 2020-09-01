#!/usr/bin/python3
""" send archive to servers"""
# to execute run this as one:
# fab -f 2-do_deploy_web_static.py
# do_deploy:archive_path=versions/web_static_20170315003959.tgz
# -i ~/.ssh/id_rsa -u ubuntu
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.74.82.97", "54.236.20.188"]


def do_deploy(archive_path):
    """ deploy archive in servers"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    try:
        put(archive_path, "/tmp/{}".format(file))
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file, name))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name))
    except all:
        return False
    return True
