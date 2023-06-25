%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : PREMIER TEMPLATE

<br>

Objectif ? créer des configmaps

<br>

* 1 chart = templates + values (default) + metadatas

<br>

* création d'un squelette de chart 

```
helm create xavki
```



-----------------------------------------------------------------------------------

# HELM : PREMIER TEMPLATE


<br>

* suppression de ce qui nous sert pas pour le moment

<br>

* exemple de configmap

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: xavki-cm
  namespace: default
data:
  key1: la valeur par défaut de ma clef1
  key2: la valeur de ma clef2
```

-----------------------------------------------------------------------------------

# HELM : PREMIER TEMPLATE


<br>

* factorisation de clefs :

```
cm:
  - key: "key1"
    data: "valeur de ma clef1 par défaut"
  - key: "key2"
    data: "valeur de am clef2 par défaut"
```

-----------------------------------------------------------------------------------

# HELM : PREMIER TEMPLATE


<br>

* adaptation du template :

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: xavki-cm
  namespace: default
data:
{{- range $cm := .Values.cm }}
  {{ $cm.key }}: {{ $cm.data }}
{{- end }}
```

-----------------------------------------------------------------------------------

# HELM : PREMIER TEMPLATE


<br>

* voir on peut surcharger via la CLI

```
helm upgrade xavki ./xavki/ --set cm[0].key="clef1",cm[0].data="data1"
```

<br>

* ou via un fichier spécifique de values

```
cm:
  - key: c1
    data: d1
  - key: c2
    data: d2
  - key: c3
    data: d3
```

-----------------------------------------------------------------------------------

# HELM : PREMIER TEMPLATE


<br>

* map de configmaps

```
configMaps:
  cm1:
    - key: "key1"
      data: "valeur de ma clef1 par défaut"
    - key: "key2"
      data: "valeur de am clef2 par défaut"
  cm2:
    - key: "key1"
      data: "valeur de ma clef1 par défaut"
    - key: "key2"
      data: "valeur de am clef2 par défaut"
```

-----------------------------------------------------------------------------------


# HELM : PREMIER TEMPLATE


<br>

* boucler des configmaps

```
{{- range $configMaps,$content := .Values.configMaps }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ $configMaps }}
  namespace: default
data:
{{- range $cm := $content }}
  {{ $cm.key }}: {{ $cm.data }}
{{- end }}
---
{{- end }}
```
