import os
import sys
import subprocess
import venv

venv_name = "text_processor_venv"


def create_virtual_environment(venv_name):
    print(f"Creating virtual environment in {venv_name}...")
    subprocess.run([sys.executable, "-m", "venv", venv_name])


def activate_virtual_environment(venv_name):
    activate_script = "activate.bat" if os.name == "nt" else "activate"
    activate_path = os.path.join(
        venv_name, "Scripts" if os.name == "nt" else "bin", activate_script
    )
    subprocess.run(activate_path, shell=True)


def install_packages(venv_dir):
    print("Installing required packages...")
    pip_exe = (
        os.path.join(venv_dir, "bin", "pip")
        if sys.platform != "win32"
        else os.path.join(venv_dir, "Scripts", "pip.exe")
    )
    subprocess.run([pip_exe, "install", "-r", "requirements.txt"])


def download_nltk_data(venv_dir):
    print("Downloading NLTK data...")
    python_exe = (
        os.path.join(venv_dir, "bin", "python")
        if sys.platform != "win32"
        else os.path.join(venv_dir, "Scripts", "python.exe")
    )
    subprocess.run([python_exe, "-m", "nltk.downloader", "stopwords", "wordnet"])


def start_text_processor_app(venv_dir):
    print("Starting the Text Processor application...")
    app_exe = (
        os.path.join(venv_dir, "bin", "python")
        if sys.platform != "win32"
        else os.path.join(venv_dir, "Scripts", "python.exe")
    )
    subprocess.run([app_exe, "app.py"])


def main():
    create_virtual_environment(venv_name)
    activate_virtual_environment(venv_name)
    install_packages(venv_name)
    download_nltk_data(venv_name)
    start_text_processor_app(venv_name)


if __name__ == "__main__":
    main()
