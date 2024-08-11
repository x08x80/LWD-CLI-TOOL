#!/usr/bin/env python3
"""
        It is a simple experimetal CLI tool which deploys your html website in your machine and hosts in localhost(127.0.0.1) and also in INTERNET through nginix
        BY asking some questions
"""
import subprocess
import os
import sys
import apache
import htttp
import threading

def clone_github_repo(repo_url):
    try:
        # Extract the repository name from the URL
        repo_name = repo_url.rstrip('/').split('/')[-1]#.replace('.git', '')
      
        
        # Clone the repository
        subprocess.run(["git", "clone", repo_url], check=True)
        
        # Get the current working directory
        current_directory = os.getcwd()
        
        # Construct the full path to the cloned repository
        repo_path = os.path.join(current_directory, repo_name)
        
        print(f"Repository cloned successfully to {repo_path}")
        
        return repo_path
    except subprocess.CalledProcessError as e:
        print(f"Error cloning the repository: {e}")
        sys.exit(1)

#getting file
print("\n\n\t***MODES***\n\n\n")

file_mode=int(input("Enter the mode(1 or 2):\n\t1.Using github link\n\t2.Using the path of the file\n\n:"))


if file_mode==1:
    fi=input("Enter the github link:\n")
    path = clone_github_repo(fi)

elif file_mode==2:
    print("***the files directory without (.html) ***\n")
    print("like /path/to/website/folder")
    path=input("Enter the path of the file:\n")
else:
    print("---wrong choice---")
    sys.exit(1)
if not os.path.isdir(path):
    print("***Error***\n\n\nGive the correct destination path\n your path is not a directory. ")
    sys.exit(1)

s = int(input("Do you wanna use apache[1] or python-http[2] for hosting\nEnter your choice (1 or 2)"))
ss = int(input("Do you need to *localhost*[1] or *Internet*(uses ngrok)[2]"))
if s==1:
    apache.copy_html_files(path)
    apache.host_with_apache()
    if ss==2:
        apache.expose_with_ngrok()
elif s==2:
    server_thread = threading.Thread(target=htttp.host_with_python_http_server, args=(path,))
    server_thread.start()
    if ss==2:
        htttp.expose_with_ngrok()
else:
    print("enter the wrong choice")
    sys.exit(1)