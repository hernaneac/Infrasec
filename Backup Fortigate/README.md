Script em powershell para backup de firewalls fortigate.

Instruções
1 - Criar um arquivo cadastro.csv com os ips de todos os firewalls na mesma pasta onde está o script (OBS Esse arquivo pode ser alimentado automaticamente por exemplo, exportando os dados dos hosts cadastrados no zabbix)

2 - baixar o arquivo pscp.exe de putty.org e colocar na mesma pasta do script.

3 - Mudar as variáveis abaixo de acordo com seu ambiente

$Username = “usuário”
$Password = 'Mudar@123'
$BackupPath = “\\172.17.17.2\Backup”

4 - Caso use uma porta não padrão para o SSH mude parametro "-P 5500" da linha 11 para a porta que vc usa, ou apague essa opção se for porta padrão

é um script bem simples mas funciona perfeitamente, qq sugestão para melhorar ele estou à disposição.