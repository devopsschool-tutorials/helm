%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : Création d'une registry privé sur Github Pages

<br>

1 - Création d'un dépôt sur Github
		et activation de pages sur la branche

<br>

2 - Ajout du dépôt localement

git clone git@github.com:priximmo/myhelmrepo.git

<br>

3 - Copie des charts
			* push

------------------------------------------------------------------------------

# HELM : Création d'une registry privé sur Github Pages


<br>

4 - Création répertoires de releases

<br>

5 - Génération des packages

```
helm package charts/{xavki_api,xavki_redis,xavki_redisinsight}
```

Option : --destination releases/

<br>

6 - Génération du fichier d'index des charts

```
helm repo index <répertoire de mon dépôt
```

Puis push

------------------------------------------------------------------------------

# HELM : Création d'une registry privé sur Github Pages

<br>

7 - Test ajout du dép^ot

```
helm repo add xavki https://priximmo.github.io/myhelmrepo
```

<br>

8 - Test  

```
helm search repo xavki
```

