%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : Dépendances & Variables


<br>

Objectifs :

		* partage de variable entre chart parent et enfants

<br>

2 types :

		* parent > enfants

		* enfants > parent

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

<br>

PARENT > ENFANTS

<br>

* values de la chart enfant :

```
redis_password: "mypassword"
redis_image: "redis:5.0.4"
redis_bck: true
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

<br>

* les définir dans les values Chart parent 

```
xavki_redis:
  redis_image: redis:5.0.3
  redis_password: "xavier"
  redis_bck: false
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

<br>

* variables global

		* chart parent

		* chart enfant

* utilisation

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  maclef: {{ .Values.global.maclef }}
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

* déclaration dans un values.yaml unique

```
global:
  maclef: "mavaleur"
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables



ENFANTS > PARENT

<br>

* values de l'enfant

```
cat enfant/values.yaml 
exports:
  enfant:
    password: "xavki"
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

<br>

* values du parent

```
dependencies:
- name: enfant
  version: "0.1.0"
  repository: "file://../enfant/"
  import-values:
  - enfant
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

<br>

* utilisation dans la chart parent

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  salad: {{ .Values.password }}
```

-----------------------------------------------------------------------

# HELM : Dépendances & Variables

* utilisation au niveau de l'enfant

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-cfgmap2
data:
  salad: {{ .Values.exports.enfant.password }}
```
