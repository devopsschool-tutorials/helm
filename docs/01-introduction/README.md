%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : INTRODUCTION


<br>

## Projet

<br>

		* projet CNCF

<br>

		* helm = gouvernail (référence à k8s)

<br>

		* supporté par : google, microsoft, bitnami, IBM...

<br>

		* Github https://github.com/helm/helm
		* Site : https://helm.sh/

<br>

		* langage : GO (6000 commits / +700 dev)

-------------------------------------------------------------------------------------

## Pourquoi ?


<br>

* outil de templating

<br>

* ère des micro-services : instanciation forte 
	(applications similaires, adaptation variables, process d'information)
		 entrée1 > processus-1 > sortie1
		 entrée2 > processus-2 > sortie2
		 entrée3 > processus-3 > sortie3

<br>

* moins d'adhérence entre ces micro-services (micro-rollback, micro-versions...)

----------------------------------------------------------------------

# Exemple


<br>

		* exemple : wordpress
	
<br>

	>> création d'une première instance
			> pvc + deployment mysql + deployment wordpress + services...

<br>

	>> itération d'une deuxième instance
			> coppier/coller des fichiers ? adaptation de certaines variables

<br>

	>> blocs cohérents = objectif de création de stack (ex monitoring k8s)

<br>

	>> coordination des unes par rapport aux autres (versions communes à l'ensemble)

<br>

	>> partage de variables communes (ex : nom instance, ports...)

Rq : similarités avec le gestionnaire de paquets (dépôts, versions, cli...)

----------------------------------------------------------------------

## Intérêts

<br>

		* orchestration et déploiement dans kubernetes

<br>

		* versionning

<br>

		* dépôts de ressources cohérentes (ex: Wordpress)
			> pvc, deployments wp, mysql, services...

<br>

		* évolution v2 à v3 :
			* suppression du mode client/serveur (tiller)
			* changement des commandes
			* changements de certains fichiers (Charts.yaml)

<br>

		* fichiers au format yaml (attention extension)

<br>

		* HelmRelease = Custom Resource Definition dans k8s

<br>

		* augmentation de ses capacités avec la combinaison à d'autres outils (ex : flux)


----------------------------------------------------------------------

## EN RESUME

<br>

		> facilite les déploiements dans k8s

<br>

		> génération de templates

<br>

		> dépôts/versionning

<br>

		= gain d'efficacité

Attention : ça devient un savoir-faire
