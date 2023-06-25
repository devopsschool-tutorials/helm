%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : DEFINITIONS & CONCEPTS


<br>

## Chart

<br>

		* package helm

<br>

		* fichiers format yaml

<br>

		* templates go des manifests

<br>

		* paramètres = values

<br>

		* metadata

------------------------------------------------------------------------


## Repositories

<br>

		* publics/privés :	

				* https://artifacthub.io/ - anciennement hub.helm.sh
	
				* https://prometheus-community.github.io/helm-charts/

<br>

				* dépôts github/gitlab

------------------------------------------------------------------------

## Release

<br>

		* une instanciation de la chart dans kubernetes 

<br>

		* combinaison des éléments : version, values, templates

------------------------------------------------------------------------

## Custom Resource Definition - CRD K8S

<br>

		* créer votre propre objet dans l'API kubernetes
				`kubectl get crd`

<br>

		* autonomie pour créer/déployer d'autres objets (deployment, services...)

<br>

		* étendre les capacités de kubernetes et simplifier son utilisation

------------------------------------------------------------------------

## HelmRelease

<br>

		* CRD spécifique à helm 

<br>

		* définie la chart à utiliser dans kub et ses valeurs notamment

<br>

		* elle se nomme HelmRelease
				`kubectl get hr`

<br>

## Helm Operator

<br>

		* opérateur dans kub > un exécutant

<br>

		* capable de manipuler et éxecuter les HelmRelease

------------------------------------------------------------------------

## Templates

<br>

		* des manifestes de ressources k8s templatisés

<br>

		* format GO template

<br>

		* récupère les metadatas, les values pour créer les manifests appliqués

------------------------------------------------------------------------

## Versions
		
<br>

		* appVersion : la version de l'applicatif déployé

<br>

		* version : version de la chart

<br>

		* on peut changer de version de chart sans changer de appVersion (ex : values)

------------------------------------------------------------------------

## Values

<br>

		* Eléments déclaratifs centrals

<br>

		* Liste des valeurs pour les principales variables des templates

<br>

		* toutes les variables du format yaml (string, int, bloc, liste...)

------------------------------------------------------------------------

## EN RESUME

<br>

		> association templates et values

<br>

		> version de chart et version d'application

<br>

		> système autonome via CRD/Operator possible

