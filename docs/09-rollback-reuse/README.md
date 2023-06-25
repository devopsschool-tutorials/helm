%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : ROLLBACK & VALUES & STOCKAGE

<br>

3 méthodes pour déployer des charts :

		* la CLI (à éviter à tout prix)

		* le values.yaml (c'est mieux ;) )

		* les HelmReleases (ah ça c'est bien)

<br>

* upgrade (10.10.2)

```
helm upgrade -n wp mywp bitnami/wordpress --values values.yaml --version 10.4.6
```

-----------------------------------------------------------------------------------------

# HELM : ROLLBACK & VALUES


<br>

* consultation de l'historique (cf revision)

```
helm history -n wp mywp
helm history -n wp mywp -o yaml
helm history -n wp mywp --max 2
```

Status :
		* deployed
		* superseded
		* failed
		* unknown

-----------------------------------------------------------------------------------------

# HELM : ROLLBACK & VALUES


<br>

* rollback vers une version spécifique

```
helm rollback -n wp mywp 2
```

Rq : toujours en avançant

<br>

* ne pas refaire le fichier de values

```
helm upgrade -n wp mywp bitnami/wordpress --reuse-values --version 10.10.1
```

-----------------------------------------------------------------------------------------

# HELM : ROLLBACK & VALUES

<br>
* consulter les valeurs des révisions

```
helm get values -n wp mywp --revision 3
```

<br>

* reset des values

```
helm upgrade -n wp mywp bitnami/wordpress --reset-values --version 10.10.2
```

-----------------------------------------------------------------------------------------

# HELM : ROLLBACK & VALUES


<br>

* helmrelease = secrets

<br>

```
kg secrets sh.helm.release.v1.mywp.v7 -n wp 
-o jsonpath='{.data.release}' | 
base64 --decode | 
base64 --decode | 
gzip -d | jq
```

ou encore

```
kubectl get secret sh.helm.release.v1.mywp.v4 -n wp
-o go-template='{{.data.release | base64decode | base64decode}}' | 
gzip -d | jq
```
