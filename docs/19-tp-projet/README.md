%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : TP Projet API - Préparation

<br>

API > Redis < Redis Insight

Helm :

		* déploiements

		* dépendances

----------------------------------------------------------------

# HELM : TP Projet API - Préparation


<br>

Docker compose :

		* Redis

		* API Python : FastApi...

		* Redis Insight

----------------------------------------------------------------

# HELM : TP Projet API - Préparation

<br>

Images docker : 

		* Redis > DockerHub

		* Redis Insight > DockerHub

		* Api Python > Dockerfile > DockerHub

----------------------------------------------------------------

# HELM : TP Projet API - Préparation

<br>

```
└── project
    ├── xavki_api
    │   ├── Chart.yaml
    │   ├── templates
    │   │   ├── deployment.yaml
    │   │   ├── _helpers.tpl
    │   │   ├── ingress.yaml
    │   │   ├── secrets.yaml
    │   │   └── service.yaml
    │   └── values.yaml
    └── xavki_redis
        ├── Chart.yaml
        ├── templates
        │   ├── config.yaml
        │   ├── deployment.yaml
        │   ├── _helpers.tpl
        │   ├── NOTES.txt
        │   └── service.yaml
        └── values.yaml
    ...
```
