%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : RECHERCHE CHARTS


<br>

* trouver une chart sur le hub

```
helm search hub wordpress
helm search hub --max-col-width=0 wordpress
```

en format yaml :

```
helm search hub --output yaml wordpress
```

---------------------------------------------------------------------

## AJOUT D'UN DEPOT

<br>

* recherche sur les dépôts installés

```
helm search repo wordpress
helm repo add bitnami https://charts.bitnami.com/bitnami
```

<br>

* mettre à jour

```
helm update repo
helm repo list
```

<br>

* recherche sur les dépôts locaux 

```
helm search repo wordpress
helm search repo --versions wordpress
```

--------------------------------------------------------------------

## CONSULTATION CHART & INSTALLATION

<br>

* consultation chart

```
helm show chart bitnami/wordpress
helm show readme bitnami/wordpress
helm show values bitnami/wordpress
helm show all bitnami/wordpress
```
Rq : --version

<br>

* installation (attention toujours comprendre)

```
helm install mywp bitnami/wordpress
helm uninstall mywp
```
