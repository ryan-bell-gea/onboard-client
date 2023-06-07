# onboard-client

## Goal
The goal of this project is to reduce the time and complexity of onboarding a new DLDP/Intern to a Smart Home rotation. This should be included in onboarding documentation.

## Current State
This is a collection of Powershell scripts that will automate the download and installation of several applications that are required for this role. The first script, `ignition.ps1`, downloads and installs Chocolatey. Chocolatey is like Homebrew for Windows. The second script, `takeoff.ps1`, uses Chocolatey to download and install everything. The `onboard-client` directory can be ignored, that was the original approach but has been succeeded by `choc-approach`.

## Limitations
- This is written for Windows machines only

## Instructions for Use
1. Open Powershell as administrator
2. Navigate to the `choc-approach` directory
3. Run `Set-ExecutionPolicy Bypass -Scope Process -Force; .\ignition.ps1`
4. Open a new Powershell session as administrator
5. In that new window, navigate to the `choc-approach` directory and run `Set-ExecutionPolicy Bypass -Scope Process -Force; .\takeoff.ps1`

## What's Included
- Chocolatey
- Git
- wget
- curl
- Python
- Corretto 11 JDK (sets JAVA_HOME)
- Maven
- IntelliJ IDEA Community Edition
- Slack
- VS Code
- Postman