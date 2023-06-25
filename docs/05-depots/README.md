%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : DEPOTS


<br>

## DEPOTS

* 1 dépôt = 1 à plusieurs charts

* publics ou non (dépôts git)

* structure d'un dépôt

* officiel : https://artifacthub.io/packages/search?kind=0

* système de vérification (signature avec clef gpg)


---------------------------------------------------------------------------------------

## COMPOSITION


<br>

* la structure du dépôt

```
charts/

	* index.yaml #public plutôt

	* mychart.tar.gz

	* mychart.tar.gz.prov # yamls et vérification (signature GPG)

	* mysecondchart/
			...
```

* utiliser la vérification

```
helm install --verify ....
```

---------------------------------------------------------------------------------------

## COMPOSITION


<br>

* index.yaml

```
apiVersion: v1
entries:
  alpine:
    - created: 2016-10-06T16:23:20.499814565-06:00
      description: this is a chart for my deployment
      digest: 99c76e403d752c84ead610644d4b1c2f2b453a74b921f422b9dcb8a7c8b559cd
      home: https://xavki.blog
      name: mychart
      sources:
      - https://github.com/helm/helm
      urls:
      - https://technosophos.github.io/tscharts/alpine-0.2.0.tgz
      version: 0.2.0
```


---------------------------------------------------------------------------------------

## RECHERCHE


<br>

* liste des dépôts installés localement

```
helm repo list
```

<br>

* recherche sur le helm hub de dépôts

```
helm search hub prometheus
```

---------------------------------------------------------------------------------------

## INSTALLATION

<br>

* installation d'un dépôt localement

```
helm repo install <nom> <url>
helm repo add bitnami https://charts.bitnami.com/bitnami
```

---------------------------------------------------------------------------------------

## RECHERCHE


<br>

* update du cache

```
helm repo update
```


<br>

* recherche sur les dépôts locaux

```
helm search repo wordpress
helm search repo wordpress --versions
```

