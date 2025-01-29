# Backend #


## Run ##

All Commands are available on Makefile ( make help )
```shell
1) create virtual enviroment
2) create .env.local
3) make upgrade-pip
4) make install
5) make start (MySQL)
6) make migrations
6) make migrate
7) make run
```

### Software ##
- Python 3.10
- MySQL
- MongoDB
- Docker

 ### Rodar os Testes
```shell
1) make test
```


## Deploy ##

Todos os comandos estão disnponíveis no Makefile
```shell
1) make login
2) make image-build
3) make image-run
4) make image-push

```

### Doc
http://<ip>:<port>/redoc<br>
http://<ip>:<port>/docs<br>


### Todo
1) Escrever mais testes nas camadas internas ( Helpers )
2) Organizar .envs por ambiente
3) Finalizar o pipeline
4) Adicionar % de taxas numa coluna do DB.

