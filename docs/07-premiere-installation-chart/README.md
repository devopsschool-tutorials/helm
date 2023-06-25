%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : PREMIER CHART


<br>

3 méthodes pour déployer des charts :

		* la CLI (à éviter à tout prix)

		* le values.yaml (c'est mieux ;) )

		* les HelmReleases (ah ça c'est bien)


<br>

* exemple de wordpress > persistence des datas (fichiers/db)

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART

<br>

* 1. nfs (ou autre)

```
sudo mkdir -p /srv/wordpress/{db,files}
sudo chmod 777 -R /srv/wordpress/
sudo apt-get install nfs-kernel-server
ou sudo yum -y install nfs-utils rpcbind
sudo vim /etc/exports
/srv/wordpress/db 192.168.7.0/24(rw,sync,no_root_squash)
/srv/wordpress/files 192.168.7.0/24(rw,sync,no_root_squash)
sudo systemctl restart nfs rpcbind
sudo exportfs -a
# test sudo mount -t nfs 192.168.7.120:/srv/wordpress/db /tmp
```

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART

<br>

NFS > PV > PVC > montage

Rq : utilsiation des StorageClass (c'est mieux)


* pv de mariadb

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mariadb-pv
spec:
  storageClassName: mariadb
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
    - ReadOnlyMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.7.120
    path: "/srv/wordpress/db"
```

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART

<br>

* pv de wordpress

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: wordpress-pv
spec:
  storageClassName: wordpress
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
    - ReadOnlyMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.7.120
    path: "/srv/wordpress/files"
```

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART

<br>

* pvc de wordpress

```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: wordpress-wordpress
spec:
  storageClassName: wordpress
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART


<br>

* pvc de mariadb

```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: data-wordpress-mariadb-0
spec:
  storageClassName: mariadb
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART

<br>

* définition des variables par la CLI (à éviter) : cf fichier joint


---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART

<br>

* par le fichier values :

```
ingress:
  enabled: true
  hostname: wordpress.kub
mariadb:
  mariadbRootPassword: secretpassword
  primary:
    persistence:
      existingClaim: wordpress-mysql
persistence:
  existingClaim: wordpress-wordpress
service:
  type: NodePort
wordpressPassword: adminpassword
wordpressUsername: admin
```

```
helm install mywp --values values.yaml bitnami/wordpress
```

---------------------------------------------------------------------------------------------------

# HELM : PREMIER CHART


<br>

* consulter les values, notes... manifests

```
helm get values <mywp>
helm get notes <mywp>
helm get manifests <mywp>
```
Rq : --all (y compris les valeurs par défaut)



