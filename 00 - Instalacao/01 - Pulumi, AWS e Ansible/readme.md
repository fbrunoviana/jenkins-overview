# Instalando o Jenkins com Pulumi, AWS e Ansible

Está instalacao busca automatizar o processo de instalacao do Jenkins.

Para uma melhor explicacão sobre o pulumi, acesse: [Pulumi Essencials](https://github.com/fbrunoviana/pulumiEssentials) [Documentacao](https://www.pulumi.com/docs/clouds/aws/)

## Pulumi

No arquivo \_\_\_main.py\_\_\_, coloque em key_name o nome do par de chaves do seu projeto.

```bash
pulumi up
```

Ao ser perguntando:

Do you want to perform this update?  [Use arrows to move, type to filter]
> yes
  no
  details

Seu resultado deverá ser parecido com o [meu resultado](https://app.pulumi.com/fbrunoviana/01-PulumiAWSeAnsible/dev/updates/1)

Teste o seu acesso ssh, no meu caso foi com o comando:

``` bash
sudo chown root: homologacao.pem 
sudo chmod 0644 homologacao.pem      
ssh -i homologacao.pem ubuntu@52.91.45.113
```

## Ansible

Certifique-se de criar o seu arquivo de inventario e insira manualmente o ip do seu servidor.
```bash
cat ansible/inventario

[jenkins]
host01 ansible_host={ IP do servidor }
```

Certifique-se que voce tem o ansible instalado na sua maquina.
```bash
ansible --version
```

Para instalar: 
```bash
cd ansible
ansible-playbook main.yaml
```

Copie a saida e 

```bash
=> {
    "admin_password_output.stdout": "xxxxxxxxx"
}
```
## Pós instalacao

Verifique novamente qual a url do Jenkins

```bash
cd ..
pulumi stack output
```

Cole no campo destacado `Administrator Password`