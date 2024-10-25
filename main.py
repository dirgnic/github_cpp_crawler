""" 
import os
import requests

def download_cpp_files(repo, branch='main'):
    # Get the tree of the repository
    url = f'https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1'
    response = requests.get(url)
    data = response.json()

    if 'tree' in data:
        for item in data['tree']:
            # Check if the item is a .cpp file
            if item['path'].endswith('.cpp'):
                # Get the raw content of the file
                file_url = f'https://raw.githubusercontent.com/{repo}/{branch}/{item["path"]}'


                try:
                    # Create directories if needed
                    os.makedirs(os.path.dirname(item['path']), exist_ok=True)


                    # Download the file
                    file_response = requests.get(file_url)
                    with open(item['path'], 'wb') as f:
                        f.write(file_response.content)
                    print(f'Downloaded: {item["path"]}')
                except Exception as e:
                    print(f'Error downloading {item["path"]}: {e}')
    else:
        print("No files found or an error occurred.")

if __name__ == "__main__":
    repo = 'mdmzfzl/NeetCode-Solutions'  # rename to repo in 'user/repo' format
    download_cpp_files(repo)
"""

import os
import requests


def download_cpp_files(repo, branch='main'):
    # Get the tree of the repository
    url = f'https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1'
    response = requests.get(url)
    data = response.json()

    if 'tree' in data:
        for item in data['tree']:
            if item['path'].endswith('.cpp'):
                file_url = f'https://raw.githubusercontent.com/{repo}/{branch}/{item["path"]}'
                try:
                    file_response = requests.get(file_url)
                    filename = os.path.basename(item['path'])
                    base, extension = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(filename):
                        filename = f"{base}_{counter}{extension}"
                        counter += 1
                    with open(filename, 'wb') as f:
                        f.write(file_response.content)
                    print(f'Downloaded: {filename}')
                except Exception as e:
                    print(f'Error downloading {item["path"]}: {e}')
    else:
        print("No files found or an error occurred.")


if __name__ == "__main__":
    repo = 'mdmzfzl/NeetCode-Solutions'  # Change this to the repo in 'username/repo' format
    download_cpp_files(repo)
