# onboard-client

## Goal
The goal of this project is to reduce the time and complexity of onboarding a new DLDP/Intern to a Smart Home rotation. This should be included in onboarding documentation.

## Current State
This is a Python script that sends a request to a public repository and scrapes a list of download URLs for applications that are needed for the rotation. It then downloads the files and calls an installation function/helper that is written for each one. It also sets JAVA_HOME and MAVEN_HOME environment variables.

## Limitations
- This is written for Windows machines only
- Installation helpers are currently limited to applications that can be silently installed from the command line
  - GUI installations are possible but would take a significant amount of work
- For each new software to be added, an installation helper must be written
  
## Next Steps
- **research Chef for deployment**
- Add applications to PATH
- Finish writing installers
- Add update capability for existing installations
- Package as a standalone executable
- Get this whitelisted from DT Security - they have an ongoing project to remove local admin rights and every app that would need admin rights has to be approved through them. I'm working on testing with someone from that team

## Instructions
1. Install Python >3.9 and add it to your PATH
2. If you have git installed, clone this repository to your machine. If not, download as a zip file and unzip the contents to a user-level directory (C:/Users/<yourSSO>/)
3. Open command prompt as an Administrator and navigate into the `onboard-client` directory
4. Run `pip install -r requirements.txt`
5. Run `python main.py`
