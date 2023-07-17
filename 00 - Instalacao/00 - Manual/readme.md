# Instalacao Manual

## Ubuntu

O ideal é seguir a [documentacao oficial](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu) 

### Instalacao do OpenJDK

```bash
sudo apt update
sudo apt install openjdk-17-jre
java -version
openjdk version "17.0.7" 2023-04-18
OpenJDK Runtime Environment (build 17.0.7+7-Debian-1deb11u1)
OpenJDK 64-Bit Server VM (build 17.0.7+7-Debian-1deb11u1, mixed mode, sharing)
```

### Instalacao do Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

### Trocando a porta

```bash
sudo sed 's/JENKINS_PORT=8080/JENKINS_PORT=8081/g' /lib/systemd/system/jenkins.service 
```

### Manipulando o servico

```bash
sudo systemctl daemon-reload # Caso voce tenha alterado a porta
sudo systemctl enable jenkins # Habilitar o serviço no boot do SO
sudo systemctl restart jenkins # Reiniciar o serviço
```

## Desbloqueando o Jenkins

1. Execute o comando cat /var/jenkins_home/secrects/initialAdminPassword
2. Copie a saida
3. Abra seu navegar e entre em http://localhost:8080 
4. Cole no campo destacado `Administrator Password`