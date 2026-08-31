import subprocess


def get_disk_usage() -> str:
    result = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"Command failed: {result.stderr.strip()}"

    return result.stdout.strip()
