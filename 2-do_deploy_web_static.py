#!/usr/bin/python3
from fabric.api import env, local, put, run
from os.path import exists, basename

env.hosts = ['100.26.244.231', '100.26.173.249']


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.
    """
    if not exists(archive_path):
        return False

    archive_name = basename(archive_path)
    archive_name_no_ext = archive_name.split(".")[0]
    remote_tmp_path = f"/tmp/{archive_name}"
    remote_release_path = f"/data/web_static/releases/{archive_name_no_ext}"

    try:
        # Upload archive to the /tmp/ directory
        put(archive_path, remote_tmp_path)

        # Create the release directory
        run(f"mkdir -p {remote_release_path}")

        # Uncompress the archive to the release directory
        run(f"tar -xzf {remote_tmp_path} -C {remote_release_path}")

        # Delete the archive from the /tmp/ directory
        run(f"rm {remote_tmp_path}")

        # Move content from web_static folder to the release directory
        run(f"mv {remote_release_path}/web_static/* {remote_release_path}/")

        # Delete the web_static folder
        run(f"rm -rf {remote_release_path}/web_static")

        # Delete the current symlink
        run(f"rm -rf /data/web_static/current")

        # Create a new symlink to the release directory
        run(f"ln -s {remote_release_path} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
