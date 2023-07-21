# Backup e Restore no Jenkins

O backup regular do seu servidor Jenkins é crucial para evitar perdas de dados em caso de falha de hardware ou corrupção de dados.

## Parte 1: Diretórios principais

O Jenkins armazena todas as suas configurações, logs e artefatos de build no diretório "JENKINS_HOME". Este é o diretório mais importante para fazer backup.

Por padrão, "JENKINS_HOME" está localizado em `~/.jenkins/` (para instalações baseadas em WAR) ou `/var/lib/jenkins/` (para instalações baseadas em RPM/DEB). Este diretório inclui o seguinte:

- `config.xml` (configuração global do Jenkins)
- `jobs/` (diretórios de jobs, cada um contendo configurações e históricos de builds)
- `nodes/` (configurações dos agentes)
- `plugins/` (plugins instalados e suas configurações)
- `secrets/` (chaves de criptografia e credenciais armazenadas)

## Parte 2: Plugins Importantes

O plugin "thinBackup" é um dos mais populares para backups no Jenkins. Ele fornece uma interface simples para agendar e restaurar backups.

Para instalar o plugin "thinBackup":

1. Vá para "Gerenciar Jenkins" > "Gerenciar Plugins" > "Disponíveis".
2. Pesquise "thinBackup" e instale-o.

Uma vez instalado, você pode configurá-lo em "Gerenciar Jenkins" > "ThinBackup" > "Settings".

## Parte 3: Shell Script para Backup

Para backup manual ou através de scripts, você pode usar um simples shell script. Aqui está um exemplo de script para backup do diretório "JENKINS_HOME":

```bash
#!/bin/bash

JENKINS_HOME=/var/lib/jenkins
BACKUP_DIR=/path/to/backup
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/jenkins_home_$(date +"%Y%m%d_%H%M%S").tar.gz -C / $JENKINS_HOME
```

Este script cria um arquivo tarball comprimido do diretório "JENKINS_HOME" com um timestamp no nome do arquivo.

## Restore

Para restaurar o Jenkins a partir de um backup, pare o serviço Jenkins, descomprima o arquivo de backup para o diretório original "JENKINS_HOME" e reinicie o Jenkins.

Exemplo:

```bash
sudo service jenkins stop
sudo tar -xzf /path/to/backup/jenkins_home.tar.gz -C /
sudo service jenkins start
```

**NOTA**: Lembre-se de ajustar os caminhos para os seus ambientes e lembre-se de testar seus backups e processos de Restore regularmente para garantir que eles estão funcionando corretamente.