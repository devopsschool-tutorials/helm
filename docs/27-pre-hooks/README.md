%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : HOOKS - Pre & Post

<br>

* pre/post action :
			* pre/post-install
			* pre/post-delete
			* pre/post-upgrade
			* pre/post-rollback
			* test

* sous forme d'annotations dans les templates

```
    "helm.sh/hook": post-install
```

------------------------------------------------------------------------------

# HELM : HOOKS - Pre & Post


<br>

* possiblité d'ordonner les hooks

```
    "helm.sh/hook-weight": "0"
```

* règles de gestion des ressources

```
    "helm.sh/hook-delete-policy": hook-succeeded
```

		* before-hook-creation
		* hook-succeeded
		* hook-failed

Example : ajout d'un backup du redis avant upgrade

------------------------------------------------------------------------------

# HELM : HOOKS - Pre & Post


* création d'un répertoire de stockage des backups

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-bck
spec:
  storageClassName: redis-bck
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.12.20
    path: "/srv/redis-bck/"
```

------------------------------------------------------------------------------

# HELM : HOOKS - Pre & Post


<br>

* création d'une storageclass spécifique

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: redis-bck
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```

------------------------------------------------------------------------------

# HELM : HOOKS - Pre & Post


<br>

* adapter le fichier de values

```
redis_PersistentVolumeClaim_Bck:
  enabled: true
  name: redis-bck
  storageClassName: redis-bck
  size: "1Gi"
```

------------------------------------------------------------------------------

# HELM : HOOKS - Pre & Post



<br>

* création d'un job : cf fichier joint

* création du pvc : cf fichier joint


