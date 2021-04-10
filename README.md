## VXI-11 Server in Python

forked from https://github.com/coburnw/python-vxi11-server


## install on Raspberry Pi

    cd ~
    mkdir repos
    cd repos
    git clone https://github.com/PhilippCo/python-vxi11-server.git
    
    sudo cp python-vxi11-server/vxi-bridge.service /lib/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable vxi-bridge.service
    sudo systemctl start vxi-bridge.service

    sudo systemctl status vxi-bridge.service
 
