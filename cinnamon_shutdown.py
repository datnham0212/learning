# combined_script.py
import os
import subprocess

def initiate_shutdown(superuser, password):
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', f'echo {password} | sudo -S -u {superuser} shutdown -h now'])

def create_shutdown_shortcut(superuser, password, shortcut_path=None):
    script_content = f"""
import subprocess

def initiate_shutdown():
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', f'echo {password} | sudo -S -u {superuser} shutdown -h now'])

if __name__ == "__main__":
    initiate_shutdown()
"""
    shortcut_name = 'Shutdown'

    script_path = os.path.join(shortcut_path or os.path.expanduser('~/Desktop'), f"{shortcut_name}_script.py")
    shortcut_path = os.path.join(shortcut_path or os.path.expanduser('~/Desktop'), f"{shortcut_name}.desktop")

    # Save the script content to a new file
    with open(script_path, 'w') as script_file:
        script_file.write(script_content)

    # Make the script file executable
    os.chmod(script_path, 0o755)

    # Create the desktop shortcut
    with open(shortcut_path, 'w') as shortcut_file:
        shortcut_file.write(f'[Desktop Entry]\nName={shortcut_name}\nExec=python3 {script_path}\nType=Application\n')

    # Make the shortcut file executable
    os.chmod(shortcut_path, 0o755)

if __name__ == "__main__":
    superuser = 'oem'  # Replace with your superuser username
    password = 'your_password'  # Replace with your actual password
    create_shutdown_shortcut(superuser, password)
    initiate_shutdown(superuser, password)
