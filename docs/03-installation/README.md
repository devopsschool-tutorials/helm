%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)


# HELM : INSTALLATION


<br>

SUR LINUX

<br>

* Via le script get-helm.sh

```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

<br>

* via le dépôt apt

```
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt install -y apt-transport-https 
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt update
sudo apt install helm
```

<br>

* via snap (ubuntu)

```
sudo snap install helm --classic
```

--------------------------------------------------------------------------------------

## AUTOCOMPLETE


<br>

* création de l'alias h

```
alias h='helm'
```

<br>

* sourcing du script d'autocomplete

```
source <(helm completion bash)
```

<br>

* autocomplete pour l'alias h

```
complete -o default -F __start_helm h
```

--------------------------------------------------------------------------------------

## AUTRES OS


<br>

SUR MACOS

```
brew install helm
```

<br>

SUR WINDOWS

```
choco install kubernetes-helm
```

<br>

SUR FREEBSD

```
pkg install helm
```
