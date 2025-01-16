import subprocess


def open_command_prompts():
    """
    Opens three command prompt windows which open theinsrument server, dataserver, and run nspyre.
    """
    # Path to the Python interpreter of the virtual environment
    python_interpreter = "C:\\Users\\USER\\anaconda3\\envs\\nspyre\\python.exe"

    # Name of environment with nspyre
    environment_name = "nspyre"

    # Path to conda.bat
    conda_bat_path = "C:\\Users\\USER\\anaconda3\\condabin\\conda.bat"

    # Path to instrument server
    inst_serv_path = "C:\\Users\\USER\\anaconda3\\envs\\nspyre\\Lib\\site-packages\\nspyre\\nspyre_template\\src\\template\\drivers\\local_inserv.py"

    # Path to gui file
    app_gui_name = "app.py"

    # Path to gui directory
    gui_directory_path = "C:\\Users\\USER\\anaconda3\\envs\\nspyre\\Lib\\site-packages\\nspyre\\nspyre_template\\src\\template\\gui"

    # Commands to run
    commands = [
        f"{python_interpreter} {inst_serv_path}",
        f"call {conda_bat_path} activate {
            environment_name} && {"nspyre-dataserv"}",
        f"cd {gui_directory_path} && {python_interpreter} {app_gui_name}"
    ]

    for command in commands:
        # Open a new command prompt window and run the specified command
        subprocess.Popen(["cmd.exe", "/K", command],
                         creationflags=subprocess.CREATE_NEW_CONSOLE)


if __name__ == "__main__":
    open_command_prompts()
