#!/usr/bin/python3
""" using fabric"""
# to execute run this:
# fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.74.82.97", "54.236.20.188"]


def do_pack():
    """ pack all web_static"""
    time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year, time.month, time.day, time.hour,
        time.minute, time.second)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file))
    except all:
        return None
    return file


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


def deploy():
    """ combines all into one command"""
    f = do_pack()
    if f is None:
        return False
    return do_deploy(f)
