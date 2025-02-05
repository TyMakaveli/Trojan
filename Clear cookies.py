import os
import subprocess

# delete safari cookies to sign client out of websites 
subprocess.run('rm -rf ~/Library/Cookies/Cookies.binarycookies', shell=True)

# disconnect and forget current wifi profile
subprocess.run('networksetup -removepreferredwirelessnetwork en0' +  ' "$(networksetup -getairportnetwork en0' + '| awk -F': ' '{print $2}')" ' , shell=True)




