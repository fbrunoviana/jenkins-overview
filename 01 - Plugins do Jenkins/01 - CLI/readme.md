## Parte 2: Linha de Comando (CLI)

Antes de começar, certifique-se de que você tem o Jenkins CLI configurado corretamente. 

### Etapa 1: Listar plugins

Para listar todos os plugins instalados no seu servidor Jenkins, use o seguinte comando:

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins
```

### Etapa 2: Instalar/Atualizar plugins

Para instalar ou atualizar um plugin, você precisa do arquivo .hpi ou .jpi do plugin. Uma vez que você tem o arquivo, use o seguinte comando:

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin <caminho_para_o_arquivo_plugin>
```

Substitua `<caminho_para_o_arquivo_plugin>` pelo caminho do arquivo .hpi ou .jpi.

### Etapa 3: Remover plugins

Para remover um plugin, use o seguinte comando:

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ uninstall-plugin <nome_do_plugin>
```

Substitua `<nome_do_plugin>` pelo nome do plugin que deseja remover.

Em todos os comandos, substitua `http://localhost:8080/` pelo URL do seu servidor Jenkins se estiver usando um servidor remoto.

Depois de instalar, atualizar ou remover plugins, você deve reiniciar o Jenkins para que as mudanças tenham efeito. Para fazer isso a partir da CLI, use o seguinte comando:

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```

Esse comando fará o Jenkins terminar de forma segura todos os trabalhos em execução antes de reiniciar.
