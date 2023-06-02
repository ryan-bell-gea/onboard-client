$batfile = choco.bat
Write-Host "Beginning the onboarding process. Please do not close this terminal until it is complete."
Write-Host "Installing Chocolatey, a universal package manager for Windows."

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

Write-Host "Chocolatey installation complete!"
Start-Process $batfile -Verb RunAs