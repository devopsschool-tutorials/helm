%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELMFILE : introduction et installation


<br>

Objectifs :

		* surcouche à helm (et plugins)

		* ajouter un fichier unique et descriptif

		* possibilité de templating sur le déploiement des release

		* meilleures gestion des values

		* gestion des dépendances facilités

		* utilisation d'un state (façon terraform)

		* réutilisation de blocs

		* gestion multi-environnement

---------------------------------------------------------------------------------

# HELMFILE : introduction et installation


<br>
* installation

```
sudo wget https://github.com/roboll/helmfile/releases/download/v0.139.9/helmfile_linux_amd64 -O /usr/local/bin/helmfile
sudo chmod +x /usr/local/bin/helmfile
```

Note : aussi via docker, arch via pacman, openSuse, windows, macOS

---------------------------------------------------------------------------------

# HELMFILE : introduction et installation


<br>

* rédaction d'un helmfile.yaml - ajout d'une chart

```
repositories:
- name: xavki
  url: https://priximmo.github.io/helmcharts/
```

<br>

* rédaction d'un helmfile.yaml - ajout d'une release

```
releases:
- name: redis-insight
  chart: xavki/xavki_redisinsight
```

---------------------------------------------------------------------------------

# HELMFILE : introduction et installation


<br>

* installation des repos

```
helmfile repos
```

<br>

* application du fichier 

```
helm plugin install https://github.com/databus23/helm-diff
helm diff
helmsync
```
