%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : ORGANISATION & DIRECTORIES


<br>
## REPERTOIRES


* Configuration

```
$HOME/.config/helm/
```

Note : configuration des dépôts installés
	* mis à jour `helm repo add`
	* bitnami https://charts.bitnami.com/bitnami

<br>

* cache

```
$HOME/.cache/helm/
```

Note : cache des dépôts installés
	* mis à jour : `helm repo update`

<br>

* datas

```
$HOME/.local/share/helm/
```

Note : stockage des plugins helm
	* mis à jour par `helm install plugin`

--------------------------------------------------------------------------

## VARIABLES D'ENVIRONNEMENT


<br>

* Reprise des variables XDG (standard) :
		* $XDG_DATA_HOME
		* $XDG_CONFIG_HOME
		* $XDG_CACHE_HOME

<br>

* $KUBECONFIG : localisation du kubeconfig (.kube/config)

<br>

* $HELM_KUBECONTEXT : contexte du kubeconfig

<br>

* $HELM_CACHE_HOME : localisation du cache

<br>

* $HELM_CONFIG_HOME : répertoire contenant les configuration

<br>

* $HELM_DATA_HOME : stockage des plugins

<br>

* $HELM_NAMESPACE : namespace utilisé par Helm

--------------------------------------------------------------------------

## VARIABLES D'ENVIRONNEMENT

<br>

* $HELM_MAX_HISTORY : définition de la longueur de l'historique

<br>

* $HELM_DEBUG : activer le mode debug (true/false)

<br>

* $HELM_DRIVER : manière de stoccker dans k8s (configmap, secrets, memory, postgres)

<br>

* $HELM_DRIVER_SQL_CONNECTION_STRING : en cas de stockage SQL

<br>

* $HELM_REGISTRY_CONFIG : chemin pour le fichier des registries

--------------------------------------------------------------------------

## VIA LA CLI

<br>

* --debug : activation du mode debug

<br>

* --kubeconfig : localisation du kubeconfig

<br>

* --namespace, -n : namespace de helm

<br>

* --kube-context : contexte à utiliser

<br>

* --repository-config : configuration des dépôts (url/noms)

<br>

* --repository-cache : localisation du cache

