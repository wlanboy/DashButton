# DashButton
Python based script to listen on Dash Button events.

## Basic requirements
Python and sudo apt install libnet1-dev

## Install as service
sudo mkdir /dash && chown yourusername:yourgroup 

cp dash.py /dash/dash.py

sudo cp dash.service /lib/systemd/system/

sudo chmod 644 /lib/systemd/system/dash.service

sudo systemctl daemon-reload

sudo systemctl enable dash.service


## Define actions
Within dash.py. Examples for send email and http calls included.
Keep in mind to define mac addresses in lower case.
