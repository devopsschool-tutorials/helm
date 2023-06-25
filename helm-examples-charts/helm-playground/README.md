# Helm playground

Following https://helm.sh/docs/chart_template_guide/getting_started/ and other bits of playing around.

```shell
# Install the chart (run minikube first and make sure kubectl/kubectx points to it)
helm install release-name . # release-name can be whatever

# Uninstall first if you want to install using the same release name
helm uninstall release-name

# Dry run
helm install test-test --dry-run --debug .

# Just the templating bit, without any k8s interaction
helm template
```
