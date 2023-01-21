#region Imports
import os
import sys
import docker
from dateutil.parser import isoparse
from datetime import datetime
import uuid
#endregion

#region Dependencies
# python3 -m pip install docker
# python3 -m pip install dateutils
#endregion


#region Logger
class Logger(object):
    def __init__(self):
        self.log = open("hole_updater.log", "a")
   
    def write(self, message):
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass
#endregion

#region Update Pihole
def update_pihole():
    print_with_current_date_time("Starting update")
    print_with_current_date_time("Update ID: " + str(uuid.uuid4()))
    update_image()
    docker_compose_down()

    client = docker.from_env()
    images = client.images.list()

    for img in images:
        created_str = img.attrs["Created"]
        image_name = img.attrs["RepoTags"][0]
        created_datetime = isoparse(created_str)

        if image_name == "pihole/pihole:latest":
            print_with_current_date_time("Latest image found")
            print_with_current_date_time(str(image_name) + "  created:  " + str(created_datetime))
            os.system("docker save -o pihole.docker pihole/pihole:latest")
            print_with_current_date_time("pihole.docker " + image_name + "  saved")
        else:
            print_with_current_date_time(str(image_name) + "  created:  " + str(created_datetime))

    clean_docker(client)

    load_image()
    docker_compose_up()
#endregion

#region Docker Helpers
def docker_compose_up():
    print_with_current_date_time("docker compose up")
    os.system("docker-compose up -d")
    print_with_current_date_time("docker compose up done")

def load_image():
    print_with_current_date_time("loading pihole image")
    os.system("docker load -i pihole.docker")
    print_with_current_date_time("pihole image loaded")

def update_image():
    print_with_current_date_time("pulling latest pihole image")
    os.system("docker pull pihole/pihole:latest")
    print_with_current_date_time("latest pihole image pulled")

def docker_compose_down():
    print_with_current_date_time("docker compose down")
    os.system("docker-compose down")
    print_with_current_date_time("docker compose down done")

def clean_docker(client):
    print_with_current_date_time("Cleaning docker")
    print_with_current_date_time("Purge containers")
    client.containers.prune()
    print_with_current_date_time("Containers purged")
    print_with_current_date_time("Purge images")
    client.images.prune(filters={'dangling': False})
    print_with_current_date_time("Images purged")
    print_with_current_date_time("Purge networks")
    client.networks.prune()
    print_with_current_date_time("Networks purged")
    print_with_current_date_time("Purge volumes")
    client.volumes.prune()
    print_with_current_date_time("Volumes purged")
    print_with_current_date_time("Docker cleaned")
#endregion

#region Time Helpers
def print_with_current_date_time(msg):
    date_time_now = get_current_date_time()
    print(date_time_now + "     " + msg)

def get_current_date_time():
    now = datetime.now()
    date_time_now = now.strftime("%d/%m/%Y %H:%M:%S")

    return date_time_now
#endregion

if __name__ == "__main__":
    sys.stdout = Logger()
    update_pihole()