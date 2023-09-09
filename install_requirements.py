import subprocess

def install_requirements(requirements_file="requirements.txt"):
    try:
        # Install requirements from the requirements.txt file
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print("Requirements successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing requirements: {e}")
    except FileNotFoundError:
        print("The 'pip' command was not found. Please ensure that Python pip is installed.")

if __name__ == "__main__":
    install_requirements()
