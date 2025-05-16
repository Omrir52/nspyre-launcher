import subprocess
import tempfile

def create_temp_ps1(script_content):
    """Creates a temporary .ps1 file with the given content."""
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.ps1', mode='w', encoding='utf-8')
    temp.write(script_content)
    temp.close()
    return temp.name

def open_command_prompts():
    # Configuration
    env_name = "nspyre"
    python_path = r"C:\Users\USER\miniforge3\envs\nspyre\python.exe"
    inst_server = r"C:\Users\USER\Python\nspyre\template\src\template\drivers\local_inserv.py"
    gui_dir = r"C:\Users\USER\Python\nspyre\template\src\template\gui"
    gui_file = "app.py"

    # First tab: instrument server
    script1 = create_temp_ps1(f"""
conda activate {env_name}
{python_path} "{inst_server}"
""")

    # Second tab: data server
    script2 = create_temp_ps1(f"""
conda activate {env_name}
nspyre-dataserv
""")

    # Third tab: GUI (wait 5 seconds first)
    script3 = create_temp_ps1(f"""
Start-Sleep -Seconds 3
conda activate {env_name}
cd "{gui_dir}"
{python_path} "{gui_file}"
""")

    # Windows Terminal command
    wt_command = [
        "wt",
        "powershell", "-NoExit", "-File", script1,
        ";", "new-tab",
        "powershell", "-NoExit", "-File", script2,
        ";", "new-tab",
        "powershell", "-NoExit", "-File", script3,
    ]

    subprocess.Popen(wt_command)

if __name__ == "__main__":
    open_command_prompts()
