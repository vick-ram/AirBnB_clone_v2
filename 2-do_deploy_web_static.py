#!/usr/bin/python3
from fabric.api import env, local, run, put

env.hosts = ['<IP_WEB-01>', '<IP_WEB-02>']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Args:
        archive_path (str): The path of the archive to be deployed.
    Returns:
        bool: True if the deployment was successful, False otherwise.
    """
    try:
        if not local("stat {}".format(archive_path), capture=True):
            return False
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        release_folder = ("/data/web_static/releases/{}"
                          .format(filename.replace(".tgz", ""))
                          )
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(filename, release_folder))
        run("mv {}/web_static/* {}/".format(release_folder, release_folder))
        run("rm -rf {}/web_static".format(release_folder))
        run("rm /tmp/{}".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
