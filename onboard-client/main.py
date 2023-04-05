import helpers
import requests
import ctypes
import sys

baseUrl = "https://raw.githubusercontent.com/"
grabPath = "ryan-bell-gea/onboarding.v1/main/README.md"
urls = []

# hit the GH repo and download the contents as a list of strings, each string being one line of the README
contentsList = requests.get(baseUrl+grabPath).text.splitlines()

# pull urls from each line and split filename from url, download each and place in User's Downloads/Onboarding/
for url in contentsList:
    if url.startswith("source"):
        url = url.split("=")[1]
        name = url.rsplit('/',1)[-1]
        pack = (name, url)
        urls.append(pack)

# hit each link from the GH README and download the file
for x in urls:
    helpers.url_response(x)

helpers.git_install()
helpers.slack_install()
# helpers.python_install() -- this is not ready
# helpers.java_install() -- need to update for msi install
helpers.maven_install()

# need elevated permissions for setting env vars
if helpers.is_admin():
    helpers.set_java_env()
    helpers.set_maven_env()
else:
    # prompt user to elevate
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, " ".join(sys.argv), None, 1)
    helpers.set_java_env()
    helpers.set_maven_env()

# install after java and maven env vars are set - do not need elevation
helpers.intellij_install()
