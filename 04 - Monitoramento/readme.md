# Monitoramento do Jenkins com Prometheus e Grafana

O Prometheus é um sistema de monitoramento e alerta de código aberto, enquanto o Grafana é uma plataforma de análise e visualização de métricas de código aberto. Ambos podem ser usados juntos para monitorar o Jenkins.

## Parte 1: Instalação do Prometheus

### Etapa 1: Baixar o Prometheus

Você pode baixar a última versão do Prometheus do [site oficial](https://prometheus.io/download/). Supondo que você esteja usando um sistema baseado em Linux:

```bash
wget https://github.com/prometheus/prometheus/releases/download/v2.30.3/prometheus-2.30.3.linux-amd64.tar.gz
```

### Etapa 2: Extrair o arquivo baixado

```bash
tar xvzf prometheus-*.tar.gz
cd prometheus-*
```

### Etapa 3: Iniciar o Prometheus

```bash
./prometheus --config.file=prometheus.yml
```

O Prometheus agora deve estar rodando na porta 9090.

## Parte 2: Instalação do Grafana

### Etapa 1: Adicionar o repositório do Grafana

```bash
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
```

### Etapa 2: Atualizar a lista de pacotes

```bash
sudo apt-get update
```

### Etapa 3: Instalar o Grafana

```bash
sudo apt-get install grafana
```

### Etapa 4: Iniciar o Grafana

```bash
sudo service grafana-server start
```

O Grafana agora deve estar rodando na porta 3000.

## Parte 3: Integração do Jenkins com Prometheus

### Etapa 1: Instalar o plugin Prometheus Metrics no Jenkins

Vá para "Gerenciar Jenkins" > "Gerenciar Plugins" > "Disponíveis" e procure por "Prometheus Metrics". Instale o plugin.

### Etapa 2: Configurar o Prometheus para coletar métricas do Jenkins

Edite o arquivo de configuração do Prometheus (prometheus.yml) e adicione o Jenkins à seção `scrape_configs`:

```yaml
scrape_configs:
  - job_name: 'jenkins'
    metrics_path: '/prometheus/'
    static_configs:
    - targets: ['<jenkins_host>:<jenkins_port>']
```

Substitua `<jenkins_host>` e `<jenkins_port>` pelo host e porta onde o Jenkins está rodando.

Reinicie o Prometheus para que as mudanças tenham efeito.

## Parte 4: Visualizar as métricas do Jenkins no Grafana

### Etapa 1: Adicionar o Prometheus como fonte de dados no Grafana

1. Abra o Grafana (http://localhost:3000/) e faça login.
2. Vá para "Configuration" > "Data Sources" > "Add data source".
3. Selecione "Prometheus".
4. Insira a URL do Prometheus (por exemplo, http://localhost:9090) e clique em "Save & Test".

### Etapa 2: Criar um painel para visualizar as métricas do Jenkins

1. Vá para "Create" > "Dashboard".
2. Clique em "Add Query".
3. Selecione "Prometheus" como fonte de dados.
4. Insira sua consulta na caixa de consulta. Por exemplo, para visualizar a quantidade de jobs no Jenkins, você pode usar a métrica `jenkins_jobs_total`.
5. Clique em "Apply" para salvar o painel.

Agora você deve ser capaz de monitorar as métricas do Jenkins no Grafana.

**NOTA:** O processo acima assume que você está executando o Prometheus, o Grafana e o Jenkins no mesmo host. Se eles estiverem em hosts diferentes, ajuste os URLs e as portas de acordo. Lembre-se também de permitir o tráfego de rede entre os hosts conforme necessário.