Stack com Zabbix Server versão 5.2.2
Grafana

Instalação em docker swarm
 -  Criar todos diretórios que estão em volumes e ajustar o path de acordo com seu ambiente especialmente se usar nfs ou algum mount volume.
 -  Se necessário trocar a senha do mysql
 -  fazer o deploy da stack (docker stack deploy -c docker-compose.yml infrasec)
 Senha padrão do zabbix usuário Admin senha zabbix
 Senha padrão do grafana usuário admin senha admin

 OBS: Caso o dashboard indique um erro no tipo de encoding, informando que precisa ser utf-8 basta parar os serviços com scale=0 entrar no container do banco e executar o script.sql