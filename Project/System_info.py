import getpass
import os
import platform
import socket
import psutil
import tkinter as tk

# Get Username
username = getpass.getuser()

# Get Home Directory
home_directory = os.path.expanduser("~")

# Get System Information
system_info = platform.uname()

# Get Current Working Directory
current_directory = os.getcwd()

# Get Environment Variables
user_profile = os.getenv("USERPROFILE")  # Windows
user_home = os.getenv("HOME")  # Unix-like systems
user_name = os.getenv("USERNAME")  # Windows

# Get Host Name
host_name = socket.gethostname()

# Get Hardware details
processor = platform.processor()
virtual_memory = psutil.virtual_memory()
total_memory = virtual_memory.total / 1024 ** 3
available_memory = virtual_memory.available / 1024 ** 3

# Get disk partitions
disk_partitions = psutil.disk_partitions()

# Display Information
root = tk.Tk()

# Get screen size (dimensions)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Get screen resolution (DPI)
screen_resolution = root.winfo_fpixels('1i')  # Pixels per inch

# Write Details to File
with open("system_info.txt", "w") as file:
    file.write(f"Username: {username}\n")
    file.write(f"Home Directory: {home_directory}\n")
    file.write(f"System Information: {system_info}\n")
    file.write(f"Current Working Directory: {current_directory}\n")
    file.write(f"User Profile: {user_profile}\n")
    file.write(f"User Home: {user_home}\n")
    file.write(f"User Name: {user_name}\n")
    file.write(f"Host Name: {host_name}\n")
    file.write("\n")
    file.write(f"System Hardware\n")
    file.write(f" Processor: {processor}\n")
    file.write(f" Total Memory: {total_memory:.2f} GB\n")
    file.write(f" Available Memory: {available_memory:.2f} GB\n")

    file.write("\nDisk Information:\n")
    for partition in disk_partitions:
        try:
            partition_info = psutil.disk_usage(partition.mountpoint)
            total_size_gb = partition_info.total / 1024 ** 3
            used_space_gb = partition_info.used / 1024 ** 3
            free_space_gb = partition_info.free / 1024 ** 3
            file.write(f" Partition: {partition.device}\n")
            file.write(f"   Mountpoint: {partition.mountpoint}\n")
            file.write(f"   Total Size: {total_size_gb:.2f} GB\n")
            file.write(f"   Used Space: {used_space_gb:.2f} GB\n")
            file.write(f"   Free Space: {free_space_gb:.2f} GB\n")
            file.write(f"   Usage Percentage: {partition_info.percent}%\n\n")
        except PermissionError:
            file.write(f"Partition: {partition.device} - Not accessible\n\n")
            continue

    file.write(f"\nScreen Information:\n")
    file.write(f" Screen Size: {screen_width} x {screen_height} pixels\n")
    file.write(f" Screen Resolution: {screen_resolution:.2f} DPI\n")

root.quit()

print("System information written to system_info.txt")
