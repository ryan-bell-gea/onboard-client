import requests
import os
import subprocess
import re
import zipfile


def url_response(url):
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/"
    newDir = "Onboarding"
    dirPath = os.path.join(parentPath, newDir)
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

    name, url = url
    downPath = os.path.join(parentPath, newDir, name)
    try:
        r = requests.get(url, stream=True)
        with open(downPath, 'wb') as f:
            for ch in r:
                f.write(ch)
    except Exception as e:
        print(e)


def java_install():
    
    # command = 'curl -L -o "corretto-jdk-17.0.6.msi" https://corretto.aws/downloads/latest/amazon-corretto-17-x64-windows-jdk.msi'
    # command2 = 'msiexec /i "corretto-jdk-17.0.6.msi" /passive /norestart'
    # subprocess.run(command)
    # subprocess.run(command2)
    
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/"
    newDir = "Onboarding"
    dirPath = os.path.join(parentPath, newDir)
    os.chdir(dirPath)
    pattern = '\"(\d+\.\d+\.\d+).*\"'

    # check if java 11 is already installed 
    check = subprocess.run("java -version", capture_output=True, text=True).stderr
    version = re.search(pattern, check).groups()[0]

    if "11.0" not in version:
        # do not uncomment until ready to install
        # subprocess.run("jdk-11_windows-x64_bin.exe /s")
        set_java_env()
        if 'java version "' in subprocess.run("java -version", capture_output=True, text=True).stderr:
            print("Java has been installed successfully")
    if "11.0" in version:
        print("Java is already installed")


def maven_install():
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/Onboarding/"
    newDir = "C:/Program Files/Maven/"
    if not os.path.exists(newDir):
        os.mkdir(newDir)
    for x in os.listdir(parentPath):
        if "apache-maven" in x:
            presentDir = os.path.join(parentPath, x)
    with zipfile.ZipFile(presentDir, 'r') as zip_ref:
        zip_ref.extractall(newDir)

    check = subprocess.run("mvn -version", capture_output=True, text=True, shell=True).stdout.splitlines()[0]
    if "Apache Maven 3" not in check:
        print("Maven is not present")
        set_maven_env()
    if "Apache Maven 3" in check:
        print("Maven is present")


def git_install():
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/Onboarding/"
    for x in os.listdir(parentPath):
        if "Git-" in x:
            command = x + " /VERYSILENT /NORESTART"
    if "git version 2" not in subprocess.run("git version", capture_output=True, text=True).stdout:
        subprocess.run(command)
        print("Git has been installed")
    elif "git version 2" in subprocess.run("git version", capture_output=True, text=True).stdout:
        print("Git is already installed")


def slack_install():
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/Onboarding/"
    checkPath = "C:/Users/" + username + "/AppData/Local/slack/slack.exe"
    command = os.path.join(parentPath, "SlackSetup.exe") + " -s"
    if not os.path.exists(checkPath):
        subprocess.run(command)
        print("Slack has been installed")
    elif os.path.exists(checkPath):
        print("Slack is already installed")


def intellij_install():
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/Onboarding/"
    checkPath = "C:/Program Files/JetBrains/IntelliJ"
    for x in os.listdir(parentPath):
        if "ideaIC-" in x:
            command = x + " /S"
    if not os.path.exists(checkPath):
        subprocess.run(command)
        print("IntelliJ has been installed")
    elif os.path.exists(checkPath):
        print("IntelliJ is already installed")


def python_install():
    username = os.getlogin()
    parentPath = "C:/Users/" + username + "/Downloads/Onboarding/"
    checkPath = "C:/Users/" + username + "/AppData/Local/Programs/Python/"
    for x in os.listdir(parentPath):
        if "python-3" in x:
            command = x + " /quiet"  # todo: figure out how to add this to PATH - cannot be done via installer switches
    if not os.path.exists(checkPath):
        subprocess.run(command)
        print("Python has been installed")
    elif os.path.exists(checkPath):
        print("Python is already installed")


def set_java_env():
    java_dir = "C:/Program Files/Java/"
    var_name = "JAVA_HOME "
    command_prefix = 'setx '
    command_suffix = '" /m'
    java_check = "echo %JAVA_HOME%"
    
    java_res = subprocess.run(java_check, capture_output=True, shell=True, text=True).stdout

    if java_res == "%JAVA_HOME%":  # set JAVA_HOME if it doesn't already exist
        for x in os.listdir(java_dir):  # grab the full path name of jdk directory
            if "jdk-11" in x:
                target = os.path.join(java_dir, x)
        
        command = command_prefix + var_name + ' "' + target + command_suffix
        subprocess.run(command)
        print("JAVA_HOME has been created")
    
    elif "jdk-11" in java_res:
        print("JAVA_HOME already exists")


def set_maven_env():
    mvn_dir = "C:/Program Files/Maven/"
    var_name = "MAVEN_HOME "
    command_prefix = 'setx '
    command_suffix = '" /m'
    java_check = "echo %JAVA_HOME%"
    maven_check = "echo %MAVEN_HOME%"
    
    java_res = subprocess.run(java_check, capture_output=True, shell=True, text=True).stdout
    maven_res = subprocess.run(maven_check, capture_output=True, shell=True, text=True).stdout
    
    if java_res == "%JAVA_HOME%":
        print("JAVA_HOME is not set")
        print("MAVEN_HOME could not be set")
    
    elif "jdk" in java_res:
        if maven_res == "%MAVEN_HOME%":  # set MAVEN_HOME if it doesn't already exist
            for x in os.listdir(mvn_dir):  # grab the full path name of apache-maven directory
                if "apache-maven" in x:
                    target = os.path.join(mvn_dir, x)
            
            command = command_prefix + var_name + ' "' + target + command_suffix
            subprocess.run(command)
            print("MAVEN_HOME has been created")
        
        elif "apache-maven" in maven_res:
            print("MAVEN_HOME already exists")
   
            
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def set_test_env():
    var_name = "TEST_HOME "
    test_dir = "C:/Program Files/Test/"
    command_prefix = 'setx '
    command_suffix = '" /m'
    if os.environ.get(var_name) is None:  # set TEST_HOME if it doesn't already exist
        for x in os.listdir(test_dir):  # loop through and grab the full path name of test-directory
            if "test-directory" in x:
                target = os.path.join(test_dir, x)
        command = command_prefix + var_name + ' "' + target + command_suffix
        subprocess.run(command)
        if os.environ.get(var_name) is None:
            print("TEST_HOME could not be created")
        elif os.environ.get(var_name) is not None:
            print("TEST_HOME has been created")
    elif os.environ.get(var_name) is not None:
        print("TEST_HOME already exists")
