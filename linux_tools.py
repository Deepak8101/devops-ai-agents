import subprocess


def run_command(command):

    return subprocess.run(
        command,
        shell=False,
        capture_output=True,
        text=True
    )


def get_hostname():

    result = run_command(
        ["hostname"]
    )

    return result.stdout.strip()


def get_disk_usage():

    result = run_command(
        ["df", "-h"]
    )

    return result.stdout


def get_memory_usage():

    result = run_command(
        ["free", "-m"]
    )

    return result.stdout


def get_uptime():

    result = run_command(
        ["uptime"]
    )

    return result.stdout

def collect_system_info():

    return {

        "hostname": get_hostname(),

        "disk": get_disk_usage(),

        "memory": get_memory_usage(),

        "uptime": get_uptime()

    }
