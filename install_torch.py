import subprocess
import time
import sys

def install():
    # Use the CPU-specific index to avoid huge GPU binaries
    command = [
        sys.executable,
        "-m", "pip",
        "install",
        "--default-timeout=1000",
        "torch",
        "--index-url", "https://download.pytorch.org/whl/cpu"
    ]

    max_retries = 20
    attempt = 0

    while attempt < max_retries:
        attempt += 1
        print(f"Attempt {attempt}/{max_retries}: Installing torch...")

        try:
            # We use subprocess.run to wait for the command to finish
            result = subprocess.run(command, check=True)
            print("SUCCESS: Torch installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("Network timeout or error. Retrying in 10 seconds...")
            time.sleep(10)

    print("FAILED: Maximum retries reached. Please check your internet connection.")
    return False

if __name__ == "__main__":
    install()
