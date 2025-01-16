Omri Raz, January 2025

To create your own executable for nspyre, please follow the instructions below.

1. Edit nspyre_launcher.py and update paths and names to the ones you use on your computer.

2. Make sure pyinstaller is installed on an environment on your computer. It does not need to be installed in the same environment as nspyre. If it is not installed, run the following command: 

pip install pyinstaller

3. Navigate to the nspyre_launcher folder and run the following command in the environment which has pyinstaller installed: 

pyinstaller --onefile --icon=favicon.ico --name=nspyre nspyre_launcher.py

4. Copy or move the executable for the dist folder to your Desktop or wherever you want to open the executable from
