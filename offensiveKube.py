import os
import sys
import docker
import inquirer

templates = ['nmap', 'metasploit', 'other']
client = docker.from_env()


def selectcontainer():
    select = ""

    print ("Select template from the options below:")

    for value in templates:
        print (value)

    while select not in templates:
            select = input()
    return select

def buildcontainer(img):
    (
    os.system("docker build -t offensive:"+image+" "+image+"/.")
    )

def runcontainer(name):
    (
    client.containers.run("offensive:"+name, detach=True,
                                            stdin_open = True,
                                                tty = True)
    )




image = selectcontainer()
buildcontainer(image)

#runcontainer("nmap")
#client.containers.get("nmap")
os.system("docker run -it offensive:"+image)