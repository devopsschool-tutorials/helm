%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : PLUGIN SECRETS

<br>

Objectif :

		* stocker un secret sur un dépôt git

		* et l'installer dans kub avec helm

<br>

* installer un plugin

```
helm plugin list
helm plugin install https://github.com/jkroepke/helm-secrets --version v3.8.1
```

----------------------------------------------------------------------------

# HELM : PLUGIN SECRETS


<br>

* génération d'une clef gpg

```
gpg --list-keys
gpg --gen-key
```

----------------------------------------------------------------------------

# HELM : PLUGIN SECRETS

<br>

* installation de sops pour générer le fichier de values avec le secret

```
wget https://github.com/mozilla/sops/releases/download/v3.7.0/sops_3.7.0_amd64.deb
sudo dpkg -i sops_3.7.0_amd64.deb
```

----------------------------------------------------------------------------

# HELM : PLUGIN SECRETS

* astuce/debug : installer le tty pour GPG

```
GPG_TTY=$(tty)
export GPG_TTY
```

The reason is gpg-agent is a daemon process that is used for managing the secret keys.

gpg-agent works as the backend for gpg and gpgsm. So suppose you have generated a key using gpg --gen-key and you are going to use those keys in your application(Kubernetes, helm chart, Linux bash script …etc), so eventually you will be needing gpg-agent for handling the keys and that is the reason why you need to tell gpg about the name of the terminal connected to standard input

----------------------------------------------------------------------------

# HELM : PLUGIN SECRETS


<br>

* génération du fichier de values

```
sops -p BDAB9680B14B8CEBEC8CC8F42513AE0ED0B65A16 secrets.yaml
```

----------------------------------------------------------------------------

# HELM : PLUGIN SECRETS

<br>

* test

```
helm create xavki
```

----------------------------------------------------------------------------

# HELM : PLUGIN SECRETS

```
apiVersion: v1
kind: Secret
metadata:
  name: mypassword
type: Opaque
data:
  mypassword: {{ .Values.mysecret | b64enc | quote }}
```

```
helm secrets install test xavki/ -f secrets.yaml -n default
kg secrets -n default mypassword -o jsonpath='{.data.mypassword}' | base64 -d
```
