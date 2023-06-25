%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : La Force de Helm démo !!!

<br>

Exemple :

		* deployment nginx

		* configmap index.html

		* service

		* ingress

----------------------------------------------------------

# HELM : La Force de Helm démo !!!

<br>

SANS HELM

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mynginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mynginx
  template:
    metadata:
      labels:
        app: mynginx
    spec:
      containers:
        - name: mynginx
          image: nginx
          ports:
          - containerPort: 80
          volumeMounts:
            - name: html
              mountPath: "/usr/share/nginx/html/"
              readOnly: true
      volumes:
        - name: html
          configMap:
            name: mynginx
```

----------------------------------------------------------

# HELM : La Force de Helm démo !!!

<br>

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: mynginx
data:
  index.html: |
    my Home Page !!!
```

```
apiVersion: v1
kind: Service
metadata:
  name: mynginx
  labels:
    app: mynginx
spec:
  ports:
    - port: 80
  selector:
    app: mynginx
  clusterIP: None
```

----------------------------------------------------------

# HELM : La Force de Helm démo !!!

<br>

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mynginx
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: mynginx.kub
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mynginx
            port:
              number: 80
```

----------------------------------------------------------

# HELM : La Force de Helm démo !!!

<br>

AVEC HELM... sinon on boss ;)

```
helm create mynginx
%s/mynginx/{{ .Release.Name }}/g
```

```
helm install mynginx2 mynginx/
helm install mynginx3 mynginx/
helm install mynginx4 mynginx/
```
