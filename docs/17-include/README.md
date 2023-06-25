%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : Include & Helpers

<br>

```
{{ include template <scope> }}
```

<br>

```
{{- define "mycharts.mylabels" -}}
env: prod
app: mynginx
{{- end }}
```

```
metadata:
  name: mynginx
  labels:
{{ include "mychart.mylabels" . | indent 4 }}
```

---------------------------------------

# HELM : Include & Helpers

<br>

```
{{- define "mychart.mylabels" -}}
labels:
  env: {{ .Values.env }}
  app: {{ .Release.Name }}
{{- end }}
```

```
metadata:
{{ include "mychart.mylabels" . | indent 2}}
```

---------------------------------------

# HELM : Include & Helpers


<br>

```
{{- define "mychart.mylabels" -}}
name: {{ .Release.Name }}
labels:
  env: {{ .Values.env }}
  app: {{ .Release.Name }}
{{- end }}
```

