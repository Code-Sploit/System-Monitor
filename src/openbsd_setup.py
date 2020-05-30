import os

glances = input(str("Glances Support [ False | True ]: "))
glances = str(glances)
glances = glances.upper()

vtop = input(str("Vtop Support [ False | True ]: "))
vtop = str(vtop)
vtop = vtop.upper()

dnstop = input(str("Dnstop Support [ False | True ]: "))
dnstop = str(dnstop)
dnstop = dnstop.upper()

netstat = input(str("Netstat Support [ False | True ]: "))
netstat = str(netstat)
netstat = netstat.upper()

if (glances == "TRUE"):
    print("Enabeling glances support...")
    os.system("pkg_add -D snap py3-pip")
    os.system("pip3.7 install glances")
    with open("./generated","a") as f:
        f.write("tmux new-session -s control -d glances")
if (vtop == "TRUE"):
    print("Enabeling vtop support...")
    os.system("pkg_add -D snap node")
    os.system("npm install -g vtop")
    with open("./generated","a") as f:
        f.write("\n\n")
        f.write("tmux split-window -v vtop")
if (dnstop == "TRUE"):
    print("Enabeling dnstop support...")
    os.system("pkg_add -D snap dnstop gnuwatch")
    interface = input(str("What is your wireless interface: "))
    interface = str(interface)
    with open("./generated","a") as f:
        f.write("\n\n")
        f.write("tmux resize-pane -L 10")
        f.write("\n\n")
        f.write("tmux split-pane -h dnstop" + interface + " -l 3")

if (netstat == "TRUE"):
    print("Enabeling netstat support...")
    with open("./i3-show-netstat","w") as f:
        f.write("netstat -na -f inet | grep -v udp | grep -v Active | grep -v ip | grep -v Proto")
    with open("./generated","a") as f:
        f.write("\n\n")
        f.write("tmux split-pane -h gnuwatch i3-show-netstat")

with open("./generated","a") as f:
    f.write("\n\n")
    f.write("tmux resize-pane -L 21")
    f.write("\n\n")
    f.write("tmux attach -t control")

os.system("mv ./i3-show-netstat /usr/bin/")
os.system("mv ./generated /usr/bin/control_sys")
os.system("chmod 755 /usr/bin/control_sys")
os.system("chmod 755 /usr/bin/i3-show-netstat")
print("Done installing!")
print("\nYour command was saved as /usr/bin/control_sys. You can run it using control_sys")
