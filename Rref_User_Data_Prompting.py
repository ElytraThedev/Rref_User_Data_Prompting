import os
import sys
import platform
import psutil
import socket
import locale
import getpass
import datetime
import threading
import shutil

def print_colored_info(label, info, color_code):
    print(f"\033[{color_code}m{label}: {info}\033[0m\n")

def get_detailed_user_info():
    color_codes = [31, 32, 33, 34, 35, 36, 37]  # ANSI color codes for red, green, yellow, blue, magenta, cyan, white
    color_index = 0

    def next_color():
        nonlocal color_index
        color = color_codes[color_index]
        color_index = (color_index + 1) % len(color_codes)
        return color

    print_colored_info("Username", getpass.getuser(), next_color())
    print_colored_info("System Name", platform.system(), next_color())
    print_colored_info("System Version", platform.version(), next_color())
    print_colored_info("Machine Type", platform.machine(), next_color())
    print_colored_info("Processor Information", platform.processor(), next_color())
    print_colored_info("CPU Count", os.cpu_count(), next_color())
    print_colored_info("Boot Time", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"), next_color())
    print_colored_info("Disk Usage", shutil.disk_usage("/"), next_color())
    print_colored_info("Memory Info", psutil.virtual_memory(), next_color())
    print_colored_info("Swap Memory Info", psutil.swap_memory(), next_color())
    print_colored_info("Network Interfaces", psutil.net_if_addrs(), next_color())
    print_colored_info("Network Connections", psutil.net_connections(), next_color())
    print_colored_info("Running Processes", [proc.info for proc in psutil.process_iter(['pid', 'name'])], next_color())
    print_colored_info("Logged In Users", psutil.users(), next_color())
    print_colored_info("Hostname", socket.gethostname(), next_color())
    print_colored_info("IP Address", socket.gethostbyname(socket.gethostname()), next_color())
    print_colored_info("Locale Information", locale.getdefaultlocale(), next_color())
    print_colored_info("Environment Variables", os.environ, next_color())
    print_colored_info("Python Version", sys.version, next_color())
    print_colored_info("Python Executable Path", sys.executable, next_color())
    print_colored_info("Platform Node", platform.node(), next_color())
    print_colored_info("Python Build Information", platform.python_build(), next_color())
    print_colored_info("Python Compiler Information", platform.python_compiler(), next_color())
    print_colored_info("Current Working Directory", os.getcwd(), next_color())
    print_colored_info("Home Directory", os.path.expanduser("~"), next_color())
    print_colored_info("Shell", os.environ.get("SHELL"), next_color())
    print_colored_info("System Architecture", platform.architecture(), next_color())
    print_colored_info("Python Path", sys.path, next_color())
    print_colored_info("Current Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), next_color())
    print_colored_info("CPU Times", psutil.cpu_times(), next_color())
    print_colored_info("Virtual Memory", psutil.virtual_memory(), next_color())
    print_colored_info("Swap Memory", psutil.swap_memory(), next_color())
    print_colored_info("Disk Partitions", psutil.disk_partitions(), next_color())
    print_colored_info("Disk IO Counters", psutil.disk_io_counters(), next_color())
    print_colored_info("Network IO Counters", psutil.net_io_counters(), next_color())
    print_colored_info("Network Stats", psutil.net_if_stats(), next_color())
    print_colored_info("Battery Status", psutil.sensors_battery(), next_color())
    print_colored_info("Number of Active Threads", threading.active_count(), next_color())
    print_colored_info("Thread Names", [t.name for t in threading.enumerate()], next_color())
    print_colored_info("Current Python Module", __name__, next_color())
    print_colored_info("Parent Process ID", os.getppid(), next_color())
    print_colored_info("Process ID", os.getpid(), next_color())
    print_colored_info("Uptime", datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time()), next_color())
    print_colored_info("Current Working Directory Contents", os.listdir(os.getcwd()), next_color())
    print_colored_info("Home Directory Contents", os.listdir(os.path.expanduser("~")), next_color())
    print_colored_info("Is Windows", os.name == 'nt', next_color())
    print_colored_info("Is Unix-like", os.name == 'posix', next_color())
    print_colored_info("Is MacOS", sys.platform == 'darwin', next_color())
    print_colored_info("System Platform", sys.platform, next_color())
    print_colored_info("File System Encoding", sys.getfilesystemencoding(), next_color())
    print_colored_info("Default Locale", locale.getdefaultlocale(), next_color())
    print_colored_info("Preferred Encoding", locale.getpreferredencoding(), next_color())
    print_colored_info("CPU Frequency", psutil.cpu_freq(), next_color())
    print_colored_info("Physical CPU Count", psutil.cpu_count(logical=False), next_color())
    print_colored_info("Logical CPU Count", psutil.cpu_count(logical=True), next_color())
    print_colored_info("CPU Stats", psutil.cpu_stats(), next_color())
    print_colored_info("CPU Percent Usage", psutil.cpu_percent(), next_color())
    print_colored_info("System Load Average (Windows)", "N/A", next_color())  # Not available on Windows
    print_colored_info("Python Executable", sys.executable, next_color())
    print_colored_info("Python Implementation", platform.python_implementation(), next_color())
    print_colored_info("Python Version Info", sys.version_info, next_color())
    print_colored_info("Current Python File", __file__, next_color())
    print_colored_info("Process Environment Variables", os.environ, next_color())
    print_colored_info("Process Priority", psutil.Process().nice(), next_color())
    print_colored_info("Process Status", psutil.Process().status(), next_color())
    print_colored_info("Process Memory Info", psutil.Process().memory_info(), next_color())
    print_colored_info("Process Open Files", psutil.Process().open_files(), next_color())
    print_colored_info("Process Connections", psutil.Process().connections(), next_color())
    print_colored_info("Process Threads", psutil.Process().threads(), next_color())
    print_colored_info("Process CPU Times", psutil.Process().cpu_times(), next_color())
    print_colored_info("Process CPU Affinity", psutil.Process().cpu_affinity(), next_color())
    print_colored_info("Process IO Counters", psutil.Process().io_counters(), next_color())
    print_colored_info("Process Creation Time", datetime.datetime.fromtimestamp(psutil.Process().create_time()).strftime("%Y-%m-%d %H:%M:%S"), next_color())
    print_colored_info("Process Memory Percent", psutil.Process().memory_percent(), next_color())
    print_colored_info("Process Name", psutil.Process().name(), next_color())
    print_colored_info("Process Executable", psutil.Process().exe(), next_color())
    print_colored_info("Process Command Line", psutil.Process().cmdline(), next_color())
    print_colored_info("Process PID", psutil.Process().pid, next_color())
    print_colored_info("Process Parent PID", psutil.Process().ppid(), next_color())
    print_colored_info("Process Username", psutil.Process().username(), next_color())
    print_colored_info("Process Children", psutil.Process().children(), next_color())
    print_colored_info("Process Suspend", "Supported (psutil.Process().suspend())", next_color())
    print_colored_info("Process Resume", "Supported (psutil.Process().resume())", next_color())
    print_colored_info("Process Kill", "Supported (psutil.Process().kill())", next_color())
    print_colored_info("Process Wait", "Supported (psutil.Process().wait())", next_color())
    print_colored_info("Process Is Running", psutil.Process().is_running(), next_color())
    print_colored_info("Process Is Stopped", psutil.Process().status() == psutil.STATUS_STOPPED, next_color())
    print_colored_info("Process Termination Status", "Supported (psutil.Process().terminate())", next_color())
    print_colored_info("Process Wait Timeout", "Supported (psutil.Process().wait(timeout=3))", next_color())
    print_colored_info("Process Terminate", "Supported (psutil.Process().terminate())", next_color())
    print_colored_info("Process Suspend", "Supported (psutil.Process().suspend())", next_color())

get_detailed_user_info()
