%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : CONDITIONS 

<br>

IF / ELSE

```
{{ if condition }}
{{ else if condition }}
{{ else }}
{{ end }}
```

```
{{- if .Values.var1 }}
  key: "set"
{{- else }}
  key: "not set"
{{- end }}
```

Note : condition = true/false

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

False :
		* false
		* 0 numérique
		* nil or empty or null
		* collections vides : map, slice, tuple, dict , array


------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

TESTS LOGIQUES

* retourne des true/false

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* AND : et

```
and .Values.key1 .Values.key2
and (test1) (test2)
{{- if and (test1) (test2) }}
```

```
{{- if and .Values.var1 .Values.var2 }}
  key: "set"
{{- else }}
  key: "not set"
{{- end }}
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* OR : ou

```
or .Values.key1 .Values.key2
or (test1) (test2)
```

```
{{- if or .Values.var1 .Values.var2 }}
  key: "set"
{{- else }}
  key: "not set"
{{- end }}
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS

<br>

* NOT : négation

```
not .Values.key1
not (test1)
```

```
{{- if and (not .Values.var1) (not .Values.var2) }}
  key: "set"
{{- else }}
  key: "not set"
{{- end }}
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* EQ : compare deux variables/formules

```
eq .Values.key1 value
```

* exemple (integer)

```
{{- if eq .Values.var1 0.0 }}
  key: "zero"
{{- else if eq .Values.var1 1.0 }}
  key: "un"
{{- else }}
  key: "autre"
{{- end }}
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* NE : non égale

```
ne .Values.key1
ne (test1)
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* LT : plus petit que strictement

* LE : plus petit ou égal à

* GT : plus grand 

* GE : plus grand ou égal

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* DEFAULT : si valeur vide set une autre valeur

```
default "valeur par défaut" .Values.key1
```

```
data:
  key: {{- default "valeur par défaut" .Values.var3 }}
```

Note : sont des valeurs vides
		* numérique : 0
		* string : ""
		* liste []
		* dict : {}
		* boolean : false
		* nil ou null

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS

<br>

* EMPTY : retourne true sur valeur vide

```
empty .Values.key1
```

<br>

* REQUIRED : vérifie les pré-requis

```
metadata:
  name: {{ required "Name of ConfigMap is required" .Values.configName }}
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* FAIL : retourne un texte sous forme d'erreur

fail "Ceci est une erreur"

```
{{- if eq .Values.var1 0.0 }}
  key: "zero"
{{- else if eq .Values.var1 1.0 }}
  key: "un"
{{- else }}
{{- fail "Invalid value for var1" }}
{{- end }}
```

------------------------------------------------------------------------------

# HELM : CONDITIONS ET OPERATEURS


<br>

* COALESCE : retourne la première valeur non vide d'une liste

```
coalesce 0 1 2
```

<br>

* TERNARY : retourne première valeur sur true sinon seconde

```
ternary "valeur1" "valeur2" (test)
(test) | ternary "valeur1" "valeur2"
```

```
data:
  key: {{ ternary "zero" "autre" ( eq .Values.var1 0.0 ) }}
```
