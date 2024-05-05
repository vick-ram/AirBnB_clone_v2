#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents
    of the web_static folder.
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {archive_name} web_static")
        print(
            f"web_static packed: {archive_name}\n"
            f"-> {local('wc -c < ' + archive_name, capture=True)} Bytes"
        )
        return archive_name
    except Exception as e:
        print(e)
        return None
