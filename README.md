# Pi Hole Updater

```
██████╗ ██████╗  █████╗ ██╗███╗   ██╗    ████████╗ ██████╗     ██████╗ ██╗   ██╗████████╗███████╗███████╗  
██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝  
██████╔╝██████╔╝███████║██║██╔██╗ ██║       ██║   ██║   ██║    ██████╔╝ ╚████╔╝    ██║   █████╗  ███████╗  
██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║       ██║   ██║   ██║    ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ╚════██║  
██████╔╝██║  ██║██║  ██║██║██║ ╚████║       ██║   ╚██████╔╝    ██████╔╝   ██║      ██║   ███████╗███████║  
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝       ╚═╝    ╚═════╝     ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚══════╝  
```

-----

## Description

A very simple python script to update your pi-hole without having to change DNS everytime
All the script does is:

- Pulls down latest pi-hole image
- Pulls and saves latest image
- Checks for latest image
- Purges all your docker container, images, volumes and networks to give you a clean slate (I ll remove that soon)
- Rebuilds the pi-hole docker image through ```docker-compose```
- Everything is logged with timestamps and a log UUID is produced for each run

For now, if you don't want to purge everything, you can just remove ```clean_docker(client)``` at line 54


Hope you enjoy!

-----
## Install

```bash
git clone git@github.com:BraintoByte/Pi-Hole-Updater.git

# As cron job

cd Pi-Hole-Updater/
touch pi_hole_job.sh
nano pi_hole_job.sh
```

Paste in this:

```bash
#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
your_python_version pi_hole_updater.py
```

**Use this to get your cron schedule: [Crontab Guru](https://crontab.guru/)**

Then to add it to crontab:

```
* * * *_your_run_schedule your_path_to_job/pi_job.sh >> your_log_preferred_path/pi_job.log  2>&1
```

This will log all output, the python script logs all output with timestamps

# Run

```bash
python pi_hole_updater.py
```




                                   Check out our website, www.braintobytes.com for more!
