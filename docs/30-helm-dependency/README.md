%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : Dependency - update, build et principes


<br>

* 2 types de sources :

		* `https://...` : charts de repositories distants

		* `file://` : fichiers et répertoires locaux

<br>

* mise en place :

```
dependencies:
- name: xavki_redis
  version: "0.3.0"
  repository: "file://../xavki_redis/"
  #condition: redis.enabled
```

------------------------------------------------------------------------

# HELM : Dependency - update, build et principes

<br>

* liste des dépendances

```
helm dependency list <chart>
```

------------------------------------------------------------------------

# HELM : Dependency - update, build et principes


<br>

* chargement des dépendances

```
helm dependency update <chart>
```

<br>

* réutilisation du Chart.lock

```
helm dependency build <chart>
```
