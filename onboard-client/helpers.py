import requests
import os
import subprocess
import re
import zipfile

def url_response(url):
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/"
    newDir = "Onboarding"
    dirPath = os.path.join(parentPath,newDir)
    if os.path.exists(dirPath) == False:
        os.mkdir(dirPath)
    
    name, url = url
    downPath = os.path.join(parentPath,newDir,name)
    try:
        r = requests.get(url, stream = True)
        with open(downPath, 'wb') as f:
            for ch in r:
                f.write(ch)
    except Exception as e:
        print(e)

def java_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/"
    newDir = "Onboarding"
    dirPath = os.path.join(parentPath,newDir)
    os.chdir(dirPath)
    pattern = '\"(\d+\.\d+\.\d+).*\"'

    # check if java 11 is already installed 
    check = subprocess.run("java -version", capture_output=True, text=True).stderr
    version = re.search(pattern, check).groups()[0]

    if "11.0" not in version:
        # do not uncomment until ready to install
        # subprocess.run("jdk-11_windows-x64_bin.exe /s")
        set_env("JAVA_HOME")
        if 'java version "' in subprocess.run("java -version", capture_output=True, text=True).stderr:
            print("Java has been installed successfully")
    if "11.0" in version:
        print("Java is already installed")

def maven_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    newDir = "C:/Program Files/Maven/"
    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
    for x in os.listdir(parentPath):
        if "apache-maven" in x:
            presentDir = os.path.join(parentPath, x)
    with zipfile.ZipFile(presentDir, 'r') as zip_ref:
        zip_ref.extractall(newDir)
    
    check = subprocess.run("mvn -version", capture_output=True, text=True, shell=True).stdout.splitlines()[0]
    if "Apache Maven 3" not in check:
        print("Maven is not present")
        set_env("MAVEN_HOME")
    if "Apache Maven 3" in check:
        print("Maven is present")
        
def git_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    for x in os.listdir(parentPath):
        if "Git-" in x:
            command = x + " /VERYSILENT /NORESTART"
    # subprocess.run(command) ------- uncomment when ready to install
    if "git version 2" in subprocess.run("git version", capture_output=True, text=True).stdout:
        print("Git is installed")
        
def slack_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    checkPath = "C:/Users/"+username+"/AppData/Local/slack/slack.exe"
    command = os.path.join(parentPath, "SlackSetup.exe") + " -s"
    if os.path.exists(checkPath) == False:
        subprocess.run(command)
        print("Slack has been installed")
    elif os.path.exists(checkPath) == True:
        print("Slack is already installed")
        
def intellij_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    checkPath = "C:/Program Files/JetBrains/"
    for x in os.listdir(parentPath):
        if "ideaIC-" in x:
            command = x + " /S"
    if os.path.exists(checkPath) == False:
        subprocess.run(command)
        print("IntelliJ has been installed")
    elif os.path.exists(checkPath) == True:
        print("IntelliJ is already installed")
        
def python_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    checkPath = "C:/Users/"+username+"/AppData/Local/Programs/Python/"
    for x in os.listdir(parentPath):
        if "python-3" in x:
            command = x + " /quiet" # todo: figure out how to add this to PATH - cannot be done via installer switches
    if os.path.exists(checkPath) == False:
        subprocess.run(command)
        print("Python has been installed")
    elif os.path.exists(checkPath) == True:
        print("Python is already installed")
        
def set_java_env():
    var_name = "JAVA_HOME"
    java_dir = "C:/Program Files/Java/"
    if os.environ.get(var_name) == None: # set JAVA_HOME if it doesn't already exist
        for x in os.listdir(java_dir): # loop through and grab the full path name of jdk directory
            if "jdk-11" in x:
                target = os.path.join(java_dir, x)
        os.environ[var_name] = target
        print("JAVA_HOME has been created")
    elif os.environ.get(var_name) != None:
        print("JAVA_HOME already exists")
      
def set_maven_env():
    var_name = "MAVEN_HOME"      
    if os.environ.get("JAVA_HOME") == None: # if JAVA_HOME does not exist, create it
        print("JAVA_HOME is not set")
        print("MAVEN_HOME is not set")
    elif os.environ.get("JAVA_HOME") != None: # if JAVA_HOME does exist
        mvn_dir = "C:/Program Files/Maven/"
        if os.environ.get(var_name) == None: # set MAVEN_HOME if it doesn't already exist
            for x in os.listdir(mvn_dir): # loop through and grab the full path name of apache-maven directory
                if "apache-maven" in x:
                    target = os.path.join(mvn_dir, x)
            os.environ[var_name] = target
            print("MAVEN_HOME has been created")
        elif os.environ.get(var_name) != None:
            print("MAVEN_HOME already exists")