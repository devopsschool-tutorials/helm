%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : Force restart

<br>

avant de conmmencer : template de la conf

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-conf-{{ .Release.Name }}
data:
  default.conf: |
    server {
      listen       {{ .Values.port }};
      listen  [::]:{{ .Values.port }};
      server_name  localhost;
      location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        #add_header X-myheader xavki;
      }
      error_page   500 502 503 504  /50x.html;
      location = /50x.html {
        root   /usr/share/nginx/html;
      }
    }
```

---------------------------------------------------

# HELM : Force restart

<br>

* deployment

```
          ports:
          - containerPort: {{ .Values.port }}
          volumeMounts:
            - name: html
              mountPath: "/usr/share/nginx/html/"
              readOnly: true
            - name: conf
              mountPath: "/etc/nginx/conf.d/"
              readOnly: true
      volumes:
        - name: html
          configMap:
            name: {{ .Release.Name }}
        - name: conf
          configMap:
            name: nginx-conf-{{ .Release.Name }}
```

---------------------------------------------------

# HELM : Force restart

<br>

Mettre à jour aussi :
	* deployment
	* service
	* ingress

---------------------------------------------------

# HELM : Force restart

<br>

* service

```
spec:
  ports:
    - port: {{ .Values.port }}
```

<br>

* ingress

```
            port:
              number: {{ .Values.port }}
```

<br>

* test :
		* changement de port
		* activation/desactivation du custom header

---------------------------------------------------

# HELM : Force restart



<br>

* forcer la modification du deployment

```
  annotations:
   checksum/configmap: {{ include (print $.Template.BasePath "/conf_nginx.yaml") . | sha256sum }}
```

<br>

* pour le faire à chaque update

```
  annotations:
    rand/roll: {{ randAlphaNum 5 | quote }}
```


