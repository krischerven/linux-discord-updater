#!/usr/bin/env python3

import urllib.request
import os


def main():

    url = "https://discord.com/api/download/stable?platform=linux&format=tar.gz"
    file_name = "_ldu_discord.tar.gz"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            with open(file_name, 'wb') as file:
                file.write(response.read())
        print(f"File '{file_name}' downloaded successfully.")
        print(f"Extracting '{file_name}' to /usr/lib64/discord. This requires root permissions:")
        os.system(f"sudo tar -xvzf {file_name} -C /usr/lib64/discord")
        print("Installation complete. If you encounter errors, please make sure that"
              + "/usr/bin/Discord is symlinked to /usr/lib64/discord/Discord/Discord.")
        os.remove(file_name)
    except IOError as err:
        print(f"Error downloading the file: {err}")


main()
