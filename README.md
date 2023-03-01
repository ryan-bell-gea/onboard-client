# onboard-client

## Goal
The goal of this project is to reduce the time and complexity of onboarding a new DLDP/Intern to a Smart Home rotation. This should be included in onboarding documentation.

## Current State
This is a Python script that sends a request to a public repository and scrapes a list of download URLs for applications that are needed for the rotation. It then downloads the files and calls an installation function/helper that is written for each one. It also sets JAVA_HOME and MAVEN_HOME environment variables. . 

## Limitations
- This is written for Windows machines only
- Installation helpers are currently limited to applications that can be silently installed from the command line
  - GUI installations are possible but would take a significant amount of work
- For each new software to be added, an installation helper must be written
- There is not a direct download link for Java 11 JDK because Oracle requires creation of an account to download
  - **Potential Solution:** Host these files in a GCP/AWS bucket and modify this project to download from that bucket. This would prevent link rot and make it easier to control the version of each application
  
## Next Steps
- Add applications to PATH
- Package as a standalone executable
- Get this whitelisted from DT Security - they have an ongoing project to remove local admin rights and every app that would need admin rights has to be approved through them. I'm working on testing with someone from that team
