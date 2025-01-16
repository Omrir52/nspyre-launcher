import subprocess
import os

def open_command_prompts():
    """
    Opens three command prompt windows which open theinsrument server, dataserver, and run nspyre.
    """
    # Path to the Python interpreter of the virtual environment
    python_interpreter = "C:\\Users\\omrir\\anaconda3\\envs\\nspyre\\python.exe" 
    
    # Name of environment with nspyre
    environment_name = "nspyre"
    
    # Path to instrument server
    inst_serv_path = "C:\\Users\\omrir\\anaconda3\\envs\\nspyre\\Lib\\site-packages\\nspyre\\nspyre_template\\src\\template\\drivers\\local_inserv.py"
    
    # Path to gui file
    app_gui_path = "C:\\Users\\omrir\\anaconda3\\envs\\nspyre\\Lib\\site-packages\\nspyre\\nspyre_template\\src\\template\\gui\\app.py"  

    # Commands to run
    commands = [
        f"{python_interpreter} {inst_serv_path}",  
        ## replace omrir with your username, you need to run the conda.bat file
        f"call {"C:\\Users\\omrir\\anaconda3\\condabin\\conda.bat"} activate {environment_name} && {"nspyre-dataserv"}",  
        f"{python_interpreter} {app_gui_path}"
        ]

    for command in commands:
        # Open a new command prompt window and run the specified command
        subprocess.Popen(["cmd.exe", "/K", command], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    open_command_prompts()
