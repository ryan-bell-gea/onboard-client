choco upgrade -yr git
choco upgrade -yr wget
choco upgrade -yr curl
choco upgrade -yr python
choco upgrade -yr corretto11jdk
choco upgrade -yr maven
choco upgrade -yr intellijidea-community
choco upgrade -yr slack
choco upgrade -yr vscode
choco upgrade -yr postman

Write-Host "Verification is here: "
choco export