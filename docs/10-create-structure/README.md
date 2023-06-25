%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : CREATE & STRUCTURE

<br>

Objectif ? structure d'une chart

<br>

* 1 chart = templates + values (default) + metadatas

<br>

* création d'un squelette de chart 

```
helm create xavki
```

-----------------------------------------------------------------------------------

# HELM : CREATE & STRUCTURE

<br>

* structure sous forme d'arborescence

```
└── xavki
    ├── charts
    ├── Chart.yaml
    ├── templates
    │   ├── deployment.yaml
    │   ├── _helpers.tpl
    │   ├── hpa.yaml
    │   ├── ingress.yaml
    │   ├── NOTES.txt
    │   ├── serviceaccount.yaml
    │   ├── service.yaml
    │   └── tests
    │       └── test-connection.yaml
    └── values.yaml
```

-----------------------------------------------------------------------------------

# HELM : CREATE & STRUCTURE


<br>

* Chart.yaml (obligatoire) : 
			* metadatas de la chart
			* version de la chart
			* version de l'applicatif
			* type de chart : application / library

<br>

* values.yaml (non obligatoire) : 
			* valeurs par défaut des variables
			* int, string, list, maps...
			* éventuellement : values.schema.json

<br>

* charts (non obligatoire) : 
			* définir les charts dont dépendent notre chart
			* construit se lon le fichier Chart.lock

-----------------------------------------------------------------------------------

# HELM : CREATE & STRUCTURE

<br>

* README.md (non obligatoire) :
			* documentation de notre chart
			* objectif
			* liste des values et leur valeurs par défaut
			* exemple...

<br>

* LICENSE (non obligatoire) :
			* définir la licence de votre chart

<br>

* .helmignore (non obligatoire) :
			* fichiers non pris en compte par la chart

-----------------------------------------------------------------------------------

# HELM : CREATE & STRUCTURE

<br>

* templates (obligatoire) :
			* répertoire contenant les templates
			* et quelques autres fichiers en lien avec les templates

<br>

* <ressources>.yaml : 
			* templates GO des ressources déployées

<br>

* NOTES.txt :
			* output à la fin de l'exécution de la chart

-----------------------------------------------------------------------------------

# HELM : CREATE & STRUCTURE

<br>

* \_helpers.tpl :
			* précalculs de variables et valeurs



