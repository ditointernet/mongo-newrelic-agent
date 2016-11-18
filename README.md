# MongoDB NewRelic Agent
Imagem do __Docker__ para monitoramento de instâncias do __MongoDB__ através do __NewRelic__.

A imagem utiliza um [plugin](https://github.com/MeetMe/newrelic-plugin-agent) para realizar o monitoramento.

## Utilização
Para utilizar a imagem basta configurar algumas variáveis de ambiente ao iniciar o container:

- `MONGO_NEWRELIC_AGENT_LICENSE_KEY` - chave do NewRelic
- `MONGO_NEWRELIC_AGENT_NAME` - nome da instância do MongoDB (é o que vai ser listado na interface do NewRelic)
- `MONGO_NEWRELIC_AGENT_HOST` - hostname/IP da instância do MongoDB
- `MONGO_NEWRELIC_AGENT_PORT` - porta da conexão com a instância do MongoDB
- `MONGO_NEWRELIC_AGENT_DATABASES` - nome das databases que serão monitoradas na instância do MongoDB

## Exemplo
Para utilizar com o `docker-compose`:

```
mongo_newrelic_agent:
  image: ditointernet/dito-mongo-newrelic-agent:v1.0.0
  environment:
    - MONGO_NEWRELIC_AGENT_LICENSE_KEY=suachaveaqui
    - MONGO_NEWRELIC_AGENT_NAME=nomedainstancia
    - MONGO_NEWRELIC_AGENT_HOST=mongo
    - MONGO_NEWRELIC_AGENT_PORT=27017
    - MONGO_NEWRELIC_AGENT_DATABASES=dadosa,dadosb
  links:
    - mongo
```
