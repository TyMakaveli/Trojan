import os
import platform
import subprocess


if platform.system() == 'Windows':
    # deleting chrome cookies
    subprocess.run(["cmd", "/c", "del", "/Q", "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies"])

    # obtaining network name
    network_name_command = "FOR /F \"tokens=2 delims=:\" %i IN ('netsh wlan show interfaces ^| findstr /C:\"SSID\"') DO @echo %i"
    network_name = subprocess.run(
        ["cmd", "/c", network_name_command],
        capture_output=True,
        text=True
        ).stdout.strip()
    
    # Trim leading spaces
    network_name = network_name.lstrip()


elif platform.system() == 'Linux':
    # Delete Chrome cookies to sign client out of websites
    subprocess.run(["rm", "-rf", "~/.config/google-chrome/Default/Cookies"])

    # Obtain the current network name
    current_network = subprocess.run(
    ["bash", "-c", "nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d':' -f2"],
    capture_output=True,
    text=True
    )

    network_name = current_network.stdout.strip()

    # Disconnect and forget the current Wi-Fi profile
    subprocess.run(["bash", "-c", f"nmcli connection delete '{network_name}'"])


else:
    # delete safari cookies to sign client out of websites 
    subprocess.run(["rm", "-rf", "~/Library/Cookies/Cookies.binarycookies"])


    # obtain current network name
    current_network = subprocess.run(
        ["networksetup", "-getairportsetup", "en0"],
        capture_output=True, 
        text=True
        )

    network_name = current_network.stdout.split(": ")[1]


    # disconnect and forget current wifi profile
    subprocess.run(["networksetup", "-removeprefferedwirelessnetwork", "en0", network_name])
