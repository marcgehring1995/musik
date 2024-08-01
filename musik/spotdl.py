import os
import subprocess
import time
import random


def install_ffmpeg():
    try:
        subprocess.run("spotdl --download-ffmpeg", shell=True, check=True)
        print("FFmpeg installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing FFmpeg: {e}")
        return False
    return True

def download_playlist(output_dir, playlist_url):
    max_retries = 5
    base_delay = 1  # Start with a 1-second delay

    for attempt in range(max_retries):
        try:
            command = f'spotdl --output "{output_dir}" download {playlist_url}'
            subprocess.run(command, shell=True, check=True)
            return  # If successful, exit the function
        except subprocess.CalledProcessError as e:
            if attempt < max_retries - 1:  # If it's not the last attempt
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                print(f"Rate limit hit. Retrying in {delay:.2f} seconds...")
                time.sleep(delay)
            else:
                raise  # If all retries failed, raise the exception

# Add this at the beginning of your main execution
if not install_ffmpeg():
    print("Failed to install FFmpeg. Please install it manually.")
    exit(1)

playlists = [
    ("set", "https://open.spotify.com/playlist/38BNqZsjMnAZXNSucEJUY8"),
    ("beach set", "https://open.spotify.com/playlist/3ELb7tw4a4HjkgKWHo4kGo"),
    ("meetings in the afterlife", "https://open.spotify.com/playlist/4aPGvBHWg47QCyZ371eSEb"),
    ("electronic fiday", "https://open.spotify.com/playlist/4JwXdeg17YUr4OyPJ0rHjo"),
    ("if else whatelse", "https://open.spotify.com/playlist/1upk12gpbd6YtInQ0JAo7f"),
    ("wenzel", "https://open.spotify.com/playlist/4EUOjRqO57cEwxhiFR7LwI"),
    ("organische house", "https://open.spotify.com/playlist/6zBMQuIXJpgx7NvBdMPmqs"),
    ("lauschige disco", "https://open.spotify.com/playlist/6v2uzAeQfpbn0OwILs5vtg"),
    ("Gute vibes house", "https://open.spotify.com/playlist/5YqMdp4HbSG4nMRkMP8tru"),
    ("Afro mäßig", "https://open.spotify.com/playlist/7kOTCf9mDT1tQfGHCdcaS3"),
    ("Bunte lichter am Strand", "https://open.spotify.com/playlist/7qiq0qxc8hxXefrIglIpw9"),
    ("Mix- Funky nights", "https://open.spotify.com/playlist/0z8RzjVjbqIJJXrk3kxZ0D"),
    ("Tiefe Vollgas", "https://open.spotify.com/playlist/5wrCKYA7SUt6psmkJjBMge"),
    ("mix neue", "https://open.spotify.com/playlist/2VF8CE611PN6PTa7taSTSh"),
    ("mix Latin:funk elektro", "https://open.spotify.com/playlist/5gNdfxpFhdYC6zq3JwxHEL"),
    ("trance trance trance", "https://open.spotify.com/playlist/6N6e1n2BTx3b2EwAWxUFrD"),
    ("Techno set middle", "https://open.spotify.com/playlist/21ivE1botkGdbkZDtXAmXB"),
]

base_dir = "/Users/marcgehring/Desktop/music"

for playlist_name, playlist_url in playlists:
    output_dir = os.path.join(base_dir, playlist_name)
    print(f"Downloading playlist: {playlist_name}")
    try:
        download_playlist(output_dir, playlist_url)
        print(f"Successfully downloaded: {playlist_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {playlist_name}: {e}")
    print("---")

print("All downloads completed.")