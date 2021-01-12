$Firewalls = get-content .\cadastro.csv
$Date = Get-Date -Format “dd-MM-yyyy”
$Username = “usuário”
$Password = 'Mudar@123'
$BackupPath = “\\172.17.17.2\Departamentos\Tecnologia\Backup”
New-Item $BackupPath\$Date\ -type directory
Start-Transcript -path $BackupPath\$Date\$Date.log -append -IncludeInvocationHeader

foreach ($Firewall in $Firewalls){

echo y | .\pscp.exe -l $Username -pw $Password -P 5500 -v “$Firewall::fgt-config” $BackupPath\$Date\ | out-host -verbose
rename-item -path $BackupPath\$Date\fgt-config -newname $BackupPath\$Date\$Firewall-$Date.conf

}

Stop-Transcript
Select-String -Path "$BackupPath\$Date\$Date.log" -Pattern "Failed to connect" > $BackupPath\$Date\resultado.txt