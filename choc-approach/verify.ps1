Write-Host "Is Git installed?"
Test-Path -Path "C:\Program Files\Git"
Write-Host "Is WGET installed?"
Test-Path -Path "C:\ProgramData\chocolatey\lib\Wget\tools" 
Write-Host "Is CURL installed?"
Test-Path -Path "C:\ProgramData\chocolatey\lib\curl\tools"
Write-Host "Is Python installed?"
Test-Path -Path "C:\ProgramData\chocolatey\lib\python3"
Write-Host "Is Java installed?"
Test-Path -Path "C:\Program Files\Amazon Corretto"
Write-Host "Is Maven installed?"
Test-Path -Path "C:\ProgramData\chocolatey\lib\maven"
Write-Host "Is IntelliJ installed?"
Test-Path -Path "C:\Program Files\JetBrains"
Write-Host "Is Slack installed?"
Test-Path -Path "C:\Users\runneradmin\AppData\Local\Slack"
Write-Host "Is VS Code installed?"
Test-Path -Path "C:\Program Files\Microsoft VS Code"
Write-Host "Is Postman installed?"
Test-Path -Path "C:\Users\runneradmin\AppData\Local\Postman"

Write-Host "Choco Installed Packages: "
choco export