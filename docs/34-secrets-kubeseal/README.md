%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : SECRETS & KUBESEAL

<br>

Objectif ?

		* stocker des secrets dans un dépôt git

Attention > ne règle pas le pb des secrets dans kub

Doc : https://fluxcd.io/docs/guides/sealed-secrets/

<br>

Principe ?

		* controller > génération de certificats pub/privé

		* controller > transforme un sealed-secret en secret k8s

		* client > génération du sealed-secret

		* stockage du sealed-secret sur un dépôt sans risque

-------------------------------------------------------------------------------------------

# HELM : SECRETS & KUBESEAL


<br>

* installation du client

```
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.16.0/kubeseal-linux-amd64 -O kubeseal
sudo install -m 755 kubeseal /usr/local/bin/kubeseal
```

-------------------------------------------------------------------------------------------

# HELM : SECRETS & KUBESEAL


<br>

* installation du controller

```
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.16.0/controller.yaml
kubectl logs -n kube-system sealed-secrets-controller-7bdbc75d47-mclzp
```

```
kubeseal --fetch-cert
```

Attention : vérifier la durée du cert

```
openssl x509 -enddate -noout -in cert.pem
```

-------------------------------------------------------------------------------------------

# HELM : SECRETS & KUBESEAL


<br>

* exemple création d'un secret

```
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: redis
type: Opaque
data:
  username: eGF2a2kK
  password: bXlwYXNzd29yZAo=
```

-------------------------------------------------------------------------------------------

# HELM : SECRETS & KUBESEAL


<br>

* génération du sealed-secret

```
kubeseal --cert cert.pem -o yaml --scope strict < secrets.yaml > sealed.yaml
```

scope : strict / namespace / cluster

<br>

* check

```
kubectl get sealedsecret -n redis mysecret -o yaml
kubectl get secrets -n redis mysecret -o yaml
```


