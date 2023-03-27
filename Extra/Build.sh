#!/bin/zsh

# this is a bash script meant to build the programs dependencies. Will work on Darwin, Unix/Linux and Windows with WSL enabled.
# This function runs first. Once it grabs local authenticatiion the it will run an update/upgrade + program build

## ADDON  : THIS OROGRAM WILL FETCH THE LOCAL IP / BROADCAST INFORMATION -- IT WILL ALSO RELAY A [func] SSH TUNNEL (SSHTunnel)

function Authentication() {
  echo '[!] Running authenticatiion!'
  sudo su
  FirstBuildRun
  BuildCredibilityAPI
  BuildExe
  echo '[!][+] Build comlete '
  }


function FirstBuildRun(){
    echo '[!] #Building first run'
    sudo apt update
    sudo apt upgrade
    echo '[+] Complete'
}



function BuildCredibilityAPI() {
     echo '[!]Building main.py dependencies'
     pipreqs --savepath=requirements.in && pip-compile

  pip install auto-py-to-exe



    apt install infix
    apt install ipcalc
    pip install pyinstaller
    pip install requests
    pip install json

    Infix -Fxz
        echo '[+] Complete'


}

function BuildExe() {
  echo '[!] Building executiabel'


    pyinstaller --onefile pythonScriptName.py

    echo '[+] Complete'

}

# USE THIS FUNCTION TO SPAWN AN SSH SESSION AND FIND BROADCAST INFORMATION (SUCH AS IP ADDRESS ETC. )
function SSHTunnel() {

DIRS=$(ls *.txt)
_broadcast = $(ifconfig | grep broadcast)
_inet = $(ifconfig | grep inet)
_mac = $(ifconfig | grep mac)
_radio_name = $(iw dev | awk) '$1=="Interface"{print $2}'

# spawn process
spawn ssh "$user\@ip" "reboot"
send "$password\r";
interact

scp <file to upload> <username>@<hostname>:<destination path>
scp -r <directory to upload> <username>@<hostname>:<destination path> # dir scp
echo "put files*.xml" | sftp -p -i ~/.ssh/key_name username@hostname.example #u using relative loc
sftp -b batchfile.txt ~/.ssh/key_name username@hostname.example # using batch in text
}

function IsComplete() {
  echo '[!] Checkingt if build is complete '

  echo '[+] Build Complete'
}

Authentication
