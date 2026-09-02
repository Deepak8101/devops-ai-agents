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


def get_memory_usage() -> str:
    result = subprocess.run(
        ["free", "-h"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"Command failed: {result.stderr.strip()}"

    return result.stdout.strip()


def get_processes(sort_by: str) -> str:

    if sort_by == "cpu":
        command = ["ps", "aux", "--sort=-%cpu"]

    elif sort_by == "memory":
        command = ["ps", "aux", "--sort=-%mem"]

    else:
        return f"Invalid sort_by value: {sort_by}"

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"Command failed: {result.stderr.strip()}"

    return result.stdout.strip()
