%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : Création d'une registry privé sur Github Pages

<br>
Chart releaser : https://github.com/helm/chart-releaser-action


1- creation d'une branche gh-pages

2- changement de conf de pages > gh-pages

3- création d'un token 

4- ajout du secrets dans les variables de dépôt
		secrets.GITHUB_TOKEN

5- ajout d'un workflow 

6- vérification de action

7- ajout d'une chart fictive

8- update 

```
helm repo update
helm search repo xavki
```

9- modification d'une version

```
helm repo update
helm search repo xavki/xavki_api --versions
```

Rq : cf tags du repo

<br>
cat .github/workflows/action.yml 
name: Release Charts

on:
  push:
    branches:
      - main

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          fetch-depth: 0

      - name: Configure Git
        run: |
          git config user.name "$GITHUB_ACTOR"
          git config user.email "$GITHUB_ACTOR@users.noreply.github.com"

      - name: Install Helm
        uses: azure/setup-helm@v1
        with:
          version: v3.4.0

      - name: Run chart-releaser
        uses: helm/chart-releaser-action@v1.2.1
        env:
          CR_TOKEN: "${{ secrets.GITHUB_TOKEN }}"

