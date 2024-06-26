#!/usr/bin/env python3

import hashlib
import os
import sys
import urllib.request

from colorama import Fore, Style


def warn(msg):
    "Print {msg} in red"
    print(f"{Fore.RED}{msg}{Style.RESET_ALL}")


def main():
    "Main entry point"

    url = "https://discord.com/api/download/stable?platform=linux&format=tar.gz"
    file_name = "/tmp/_ldu_tmp_discord_{}.tar.gz".format(
        hashlib.md5("ldu magic string".encode()).hexdigest())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            with open(file_name, 'wb') as file:
                file.write(response.read())

        print(f"File '{file_name}' downloaded successfully.")
        print(f"Extracting '{file_name}' to /usr/lib64/discord. " +
              "If you are not root, you will be prompted for a password`:")

        os.system(f"sudo tar -xvzf {file_name} -C /usr/lib64/discord")

        if not os.path.exists("/usr/lib64/discord/Discord/Discord"):
            warn("An internal installation error occured: /usr/lib64/discord/Discord/Discord does not exist.")
            sys.exit(1)

        if not os.path.exists("/usr/bin/Discord"):
            warn("Warning: /usr/bin/Discord does not exist. Discord probably won't run.")

        elif not os.path.samefile("/usr/lib64/discord/Discord/Discord", "/usr/bin/Discord"):
            warn("Warning: /usr/bin/Discord is not symlinked to /usr/lib64/discord/Discord/Discord. " +
                 "You will probably encounter errors when running Discord.")

        else:
            print("Update successful.")

        os.remove(file_name)

    except IOError as err:
        warn(f"Error downloading the file: {err}")


main()
