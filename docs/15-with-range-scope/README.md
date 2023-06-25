%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : With, Range et Scopes

<br>

WITH

* modification du scope

```
niveau1:
  niveau2:
    valeur1: "Hello"
    valeur2: "Xavki"
```

```
data:
  key1: {{ .Values.niveau1.niveau2.valeur1 }}
  key2: {{ .Values.niveau1.niveau2.valeur2 }}
```

--------------------------------------------------------------------

# HELM : With, Range et Define

<br>

* solution : changer de scope

```
{{- with .Values.niveau1.niveau2 }}
  key1: {{ .valeur1 }}
  key2: {{ .valeur2 }}
{{- end }}
```

--------------------------------------------------------------------

# HELM : With, Range et Define

<br>

* mais attention

```
{{- with .Values.niveau1.niveau2 }}
  key1: {{ .valeur1 }}
  key2: {{ .valeur2 }}
  key3: {{ .Release.Name }}
{{- end }}
```

<br>

* solution

```
{{ $release := .Release.Name }}
{{- with .Values.niveau1.niveau2 }}
  key1: {{ .valeur1 }}
  key2: {{ .valeur2 }}
  key3: {{ $release }}
{{- end }}
```

--------------------------------------------------------------------

# HELM : With, Range et Define

<br>

```
{{- range $key, $value := .Values.niveau1.niveau2 }}
  {{ $key }}: {{ $value }}
{{- end }}
```

<br>

* contenu d'un fichier .yml

```
data:
  myfile.yml: |
{{- range $key, $value := .Values.niveau1.niveau2 }}
    {{ $key }}: {{ $value }}
{{- end }}
```

--------------------------------------------------------------------

# HELM : With, Range et Define

<br>

* ajouter l'indentation souhaitée

```
data:
{{- range $index, $value := .Values.niveau1.niveau2 }}
{{ $index | indent 2 }}: {{ $value }}
{{- end }}
```

--------------------------------------------------------------------

# HELM : With, Range et Define

<br>

* même problème que sur les with (on est dans un scope)

```
{{- range $index, $value := .Values.niveau1.niveau2 }}
{{ $index | indent 2 }}: {{ $value }} - {{ .Release.Name }}
{{- end }}
```

<br>

* solution :

```
{{- $release := .Release.Name }}
{{- range $index, $value := .Values.niveau1.niveau2 }}
{{ $index | indent 2 }}: {{ $value }} - {{ $release }}
{{- end }}
```
