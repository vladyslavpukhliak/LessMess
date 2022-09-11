import winreg as reg
import os

# Set the path of the context menu (right-click menu)
# Change the name of your project
projectname = input("Enter a project name:")
key_path = r'Directory\\Background\\shell\\' + projectname + '\\'

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
# Change the function of your script
reg.SetValue(key, '', reg.REG_SZ,
             f'{input("Enter the application function:")}')

# create inner key
key1 = reg.CreateKey(key, r"command")
# change the name of your script
reg.SetValue(key1, '', reg.REG_SZ,
             f'"{input("Enter application path:")}"')