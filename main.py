import os
import re

resp = os.popen("netsh wlan show profiles")

text = resp.read()

router_names = re.findall("All User Profile\s+\: (.+)", text)

routers = {}

for router_name in router_names:
    resp = os.popen('netsh wlan show profile "{}" key=clear'.format(router_name))
    text = resp.read()
    password_regex = re.search("Key Content\s+\: (\w+)", text)

    if password_regex:
        password = password_regex.group(1)
        routers[router_name] = password

with open("passwords.txt", 'a') as file:
    for name, password in routers.items():
        file.write(name + " : " + password + "\n")