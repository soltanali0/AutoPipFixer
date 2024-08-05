import subprocess
import re
import argparse

def run_command_and_install_missing_packages(command):
    while True:
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(result.stdout)
            break 
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            match = re.search(r"ModuleNotFoundError: No module named '(\w+)'", e.stderr)
            if match:
                module_name = match.group(1)
                install_command = f"pip install {module_name} --break-system-packages"
                try:
                    subprocess.run(install_command, shell=True, check=True)
                    print(f"Installed missing module: {module_name}")
                except subprocess.CalledProcessError as install_error:
                    print(f"Failed to install module: {module_name}")
                    print(install_error.stderr)
                    break
            else:
                print("No ModuleNotFoundError found. Exiting...")
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a command and install missing Python packages if ModuleNotFoundError occurs.")
    parser.add_argument('-c', '--command', type=str, required=True, help='Command to run')
    args = parser.parse_args()
    
    run_command_and_install_missing_packages(args.command)
