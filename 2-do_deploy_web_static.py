#!/usr/bin/python3
""" send archive to servers"""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.74.82.97", "54.236.20.188"]


def do_deploy(archive_path):
    """ deploy archive in servers"""
    if os.path.isfile(archive_path) is False:
        return False
    split = archive_path.split('/')
    name = split[-1]
    long_name = name[:-4]
    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(long_name))
    run("tar -xzf /tmp/{} -C /data/".format(name) +
        "web_static/releases/{}/".format(long_name))
    run("rm /tmp/{}".format(name))
    run("mv /data/web_static/releases/{}/".format(long_name) +
        "web_static/* /data/web_static/releases/{}/".format(long_name))
    run("rm -rf /data/web_static/releases/{}/web_static".format(long_name))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ ".format(long_name) +
        "/data/web_static/current")
    return True
