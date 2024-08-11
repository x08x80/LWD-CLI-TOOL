import os
import subprocess
import shutil

def copy_html_files(html_path):
    # Define the destination directory for Apache
    apache_html_dir = "/var/www/html"
    
    # Clean the Apache HTML directory
    for filename in os.listdir(apache_html_dir):
        file_path = os.path.join(apache_html_dir, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    # Copy the user's HTML files to the Apache directory
    if os.path.isdir(html_path):
        shutil.copytree(html_path, apache_html_dir, dirs_exist_ok=True)
    else:
        shutil.copy2(html_path, apache_html_dir)
    print(f"HTML files copied to {apache_html_dir}.")

def host_with_apache():
    """
    This function starts the Apache server to host the website on localhost.
    """
    try:
        # Start Apache server
        subprocess.run(["sudo", "systemctl", "start", "apache2"], check=True)
        print("Apache server started. The website is now hosted on http://localhost.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Apache server: {e}")

def expose_with_ngrok():
    """
    This function exposes the Apache server to the internet using Ngrok.
    """
    try:
        print("Starting Ngrok to expose the website to the internet...")
        os.system("ngrok http 80")  # Expose port 80, where Apache is serving
    except Exception as e:
        print(f"Failed to start Ngrok: {e}")