# combined_script.py
import os
import subprocess

def initiate_shutdown():
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'shutdown -h now'])

def create_shutdown_shortcut(shortcut_path=None):
    script_content = """
import subprocess

def initiate_shutdown():
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'shutdown -h now'])

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
    create_shutdown_shortcut()
    initiate_shutdown()
