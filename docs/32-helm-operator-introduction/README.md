%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : HELM-OPERATOR - Intro et Installation

<br>

Objectifs :

		* déployer directement dans les cluster

		* chart source + values > 1 manifest

		* possibilité de synchronisation (ex : fluxcd)

		* publique ou privée repo

		* git ou repo helm

		* interaction avec la CLI Helm

<br>

En résumé :

		* avant :   client Helm > cluster k8s > dépôts charts

		* après :   kubectl apply -f hr > helm operator > dépôts charts


---------------------------------------------------------------------------------------


# HELM : HELM-OPERATOR - Intro et Installation


<br>

* récupérer la chart du helm-operator pour découvrir les values

```
helm repo add fluxcd https://charts.fluxcd.io
helm update
helm fetch fluxcd/helm-operator
tar -xzvf helm-operator-1.2.0.tgz
```

<br>

* préparation

```
kubectl create ns flux
ssh-keygen -q -N "" -f ./identity
kubectl -n flux create secret generic helm-ssh --from-file=./identity
ssh-keyscan github.com
```

---------------------------------------------------------------------------------------


# HELM : HELM-OPERATOR - Intro et Installation


<br>

* exemple de values

```
    helm:
      versions: v3
    replicaCount: 1
    createCRD: false
    image:
      repository: fluxcd/helm-operator
      tag: 1.2.0
    pullPolicy: IfNotPresent
    git:
      ssh:
        secretName: "helm-ssh"
        known_hosts: ""
    statusUpdateInterval: 60s
```

<br>

* lancement de l'installation

```
helm install -n flux helm-operator fluxcd/helm-operator -f hr-values.yaml
```
