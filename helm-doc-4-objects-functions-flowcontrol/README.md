# helm-tutorial
Tutorial for helm charts

## 1. Install the prerequisites
* [Install Docker Desktop](https://docs.docker.com/desktop/windows/install/)
* Install Brew
```bash    
    # Install Brew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Install Homebrew's dependencies
    sudo apt-get install build-essential
    brew install gcc

    # Verify brew
    brew doctor
```

## 2. Install helm CLI
```bash

    # Install helm
    brew install helm
```

## 3. Objects
1. Release: This object describes the release itself. It has several objects inside of it:
    * Release.Name: The release name
    * Release.Namespace: The namespace to be released into (if the manifest doesn’t override)
    * Release.IsUpgrade: This is set to true if the current operation is an upgrade or rollback.
    * Release.IsInstall: This is set to true if the current operation is an install.
    * Release.Revision: The revision number for this release. On install, this is 1, and it is incremented with each upgrade and rollback.
    * Release.Service: The service that is rendering the present template. On Helm, this is always Helm
1. Values: Values passed into the template from the values.yaml file and from user-supplied files. By default, Values is empty.
    * Values value can come from multiple places like,
        * The values.yaml file in the chart
        * If this is a subchart, the values.yaml file of a parent chart
        * A values file if passed into helm install or helm upgrade with the -f flag (helm install -f myvals.yaml ./mychart)
        * Individual parameters passed with --set (such as helm install --set foo=bar ./mychart)
    * Order of precedence from low to high is,
        * Current chart's values.yaml
        * Parent chart's value.yaml
        * User-supplied value file
        * Values passed in by --set parameter
1. Chart: The contents of the Chart.yaml file. Any data in Chart.yaml will be accessible here. For example {{ .Chart.Name }}-{{ .Chart.Version }} will print out the mychart-0.1.0.
    * The available fields are listed in the Charts Guide
1. Files: This provides access to all non-special files in a chart. While you cannot use it to access templates, you can use it to access other files in the chart. See the section Accessing Files for more.
    * Files.Get is a function for getting a file by name (.Files.Get config.ini) 

    Example:
    ```yaml
    # 1
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: {{ .Release.Name }}-configmap
    data:
        {{- $files := .Files }}
        {{- range tuple "config1.toml" "config2.toml" "config3.toml" }}
        {{ . }}: |-
            {{ $files.Get . }}
        {{- end }}
    
    # 2
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: {{ .Release.Name }}-configmap
    data:
        {{ $currentScope := .}}
        {{ range $path, $_ :=  .Files.Glob  "**.yaml" }}
            {{- with $currentScope}}
                {{ .Files.Get $path }}
            {{- end }}
        {{- end }}
    
    # 3
    apiVersion: v1
    kind: ConfigMap
    metadata:
    name: conf
    data:
        token: |-
            {{ (.Files.Glob "foo/*").AsConfig | b64enc | indent 2 }}
        some-file.txt: {{ range .Files.Lines "foo/bar.txt" }}
            {{ . }}{{ end }}
    ```

    * Files.GetBytes is a function for getting the contents of a file as an array of bytes instead of as a string. This is useful for things like images.
    * Files.Glob is a function that returns a list of files whose names match the given shell glob pattern.
    * Files.Lines is a function that reads a file line-by-line. This is useful for iterating over each line in a file.
    * Files.AsSecrets is a function that returns the file bodies as Base 64 encoded strings.
    * Files.AsConfig is a function that returns file bodies as a YAML map.
1. Capabilities: This provides information about what capabilities the Kubernetes cluster supports.
    * Capabilities.APIVersions is a set of versions.
    * Capabilities.APIVersions.Has $version indicates whether a version (e.g., batch/v1) or resource (e.g., apps/v1/Deployment) is available on the cluster.
    * Capabilities.KubeVersion and Capabilities.KubeVersion.Version is the Kubernetes version.
    * Capabilities.KubeVersion.Major is the Kubernetes major version.
    * Capabilities.KubeVersion.Minor is the Kubernetes minor version.
    * Capabilities.HelmVersion is the object containing the Helm Version details, it is the same output of helm version
    * Capabilities.HelmVersion.Version is the current Helm version in semver format.
    * Capabilities.HelmVersion.GitCommit is the Helm git sha1.
    * Capabilities.HelmVersion.GitTreeState is the state of the Helm git tree.
    * Capabilities.HelmVersion.GoVersion is the version of the Go compiler used.
1. Template: Contains information about the current template that is being executed
    * Template.Name: A namespaced file path to the current template (e.g. mychart/templates/mytemplate.yaml)
    * Template.BasePath: The namespaced path to the templates directory of the current chart (e.g. mychart/templates).

## 4. Functions
Template functions follow the syntax functionName arg1 arg2.... In the snippet below, quote .Values.favorite.drink calls the quote function and passes it a single argument.
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ quote .Values.favorite.drink }}
  food: {{ quote .Values.favorite.food }} 
```

Few of the built-in functions
* quote: quote argument1
* default: default <default-value> <value>
* repeat: repeat <number>
* upper: upper <value>
* operators: eq, ne, lt, gt, and, or, etc.

## 5. Pipelines
In this example, instead of calling quote ARGUMENT, we inverted the order. We "sent" the argument to the function using a pipeline | .Values.favorite.drink | quote. Using pipelines, we can chain several functions together.
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | quote }}
  food: {{ .Values.favorite.food | upper | quote }}
```

## 6. Flow control
```yaml
# 1. if/else: for creating conditional blocks 
# Syntax:
{{ if PIPELINE }}
    # Do something
{{ else if OTHER PIPELINE }}
    # Do something else
{{ else }}
    # Default case
{{ end }}

# Example:
apiVersion: v1
kind: ConfigMap
metadata:
    name: {{ .Release.Name }}-configmap
data:
    myvalue: "Hello World"
    drink: {{ .Values.favorite.drink | default "tea" | quote }}
    food: {{ .Values.favorite.food | upper | quote }}
    {{- if .Values.favoriteFood | lower | eq "burger" }}
    food: "burger"
    {{- end }} 

# Note: 
{{- (with the dash and space added) indicates that whitespace should be chomped left, while -}} means whitespace to the right should be consumed. Be careful! Newlines are whitespace!


# 2. with: to specify a scope
# Syntax:
{{ with PIPELINE }}
  # restricted scope
{{ end }}

# Example:
apiVersion: v1
kind: ConfigMap
metadata:
    name: {{ .Release.Name }}-configmap
data:
    myvalue: "Hello World"
    {{- with .Values.favorite }}
    drink: {{ .drink | default "tea" | quote | upper }}
    {{- if .food | lower | eq "burger" }}
    food: "burger"
    {{- else }}
    food: "sandwich"
    releaseName: {{ $.Release.Name }} # 
    {{- end }}
    {{- end }}

# Note:
# To access Release object that's outside the current scope, we have used $ which is mapped to root scope. Or the releaseName could have been moved after with end.
# Or we can use template variables as shown below, 

apiVersion: v1
kind: ConfigMap
metadata:
    name: {{ .Release.Name }}-configmap
data:
    myvalue: "Hello World"
    {{- $relname := .Release.Name -}}
    {{- with .Values.favorite }}
    drink: {{ .drink | default "tea" | quote | upper }}
    {{- if .food | lower | eq "burger" }}
    food: "burger"
    {{- else }}
    food: "sandwich"
    releaseName: {{ $relname }}
    {{- end }}
    {{- end }}


# 3. range: which provides a "for each"-style loop
# Example:
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  toppings: |-
    {{- range $index, $topping := .Values.pizzaToppings }}
      {{ $index }}: {{ $topping }}
    {{- end }}
  sizes: |-
    {{- range tuple "small" "medium" "large" }}
    - {{ . | title | quote }}
    {{- end }}

# Note:
# Please note the use of,
# |- above; it's used to denote multiline string in yaml
# tuple, to create a list of various data type elements
# Also, alternate forms,
# {{- range $key, $val := .Values.favorite }}
# {{- range .Values.pizzaToppings }}



# In addition to these, it provides a few actions for declaring and using named template segments:
# 1. define: declares a new named template inside of your template
# Syntax:
{{- define "MY.NAME" }}
  # body of template here
{{- end }}

#Example:
{{/* Generate basic labels */}}
{{- define "mychart.labels" }}
  labels:
    generator: helm
    date: {{ now | htmlDate }}
{{- end }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
  {{- template "mychart.labels" . }} # '.' is the root level scope; we could have also passed .Values or .Values.favorite, etc.
data:
  myvalue: "Hello World"
  {{- range $key, $val := .Values.favorite }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}

# Note:
# Usually define are placed in partial files, usually _helpers.tpl

# We can also use include like below to get the define included in multiple places with indent and as a part of a pipeline. This is recommended approach.
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
  labels:
{{ include "mychart.app" . | indent 4 }}
data:
  myvalue: "Hello World"
  {{- range $key, $val := .Values.favorite }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}
{{ include "mychart.app" . | indent 2 }}
```

## 7. NOTES.txt
At the end of a helm install or helm upgrade, Helm can print out a block of helpful information for users. This information is highly customizable using templates.

To add installation notes to your chart, simply create a templates/NOTES.txt file. This file is plain text, but it is processed like as a template, and has all the normal template functions and objects available.

Example: 
```yaml
Thank you for installing {{ .Chart.Name }}.
Your release is named {{ .Release.Name }}.

To learn more about the release, try:
  $ helm status {{ .Release.Name }}
  $ helm get all {{ .Release.Name }}
```

## 8. CLI Commands
```bash

    # Create a helm chart(This will create a folder called mychart in the project with all default helm files)
    # Some of the files created are,
    # NOTES.txt: The "help text" for your chart. This will be displayed to your users when they run helm install.
    # deployment.yaml: A basic manifest for creating a Kubernetes deployment
    # service.yaml: A basic manifest for creating a service endpoint for your deployment
    # _helpers.tpl: A place to put template helpers that you can re-use throughout the chart
    helm create mychart

    # Set proper permissions for kube config
    chmod 600 <Path to kube config file>

    # We can delete all the above-created default helm files and create the needed from scratch. In production, you might not want to do this!
    rm -rf mychart/templates/*

    # Create a template for configMap
    # configMap: In Kubernetes, a ConfigMap is simply an object for storing configuration data. Other things, like pods, can access the data in a ConfigMap.
    # .yaml for YAML files and .tpl for helpers are recommended
    vim mychart/templates/configMap.yaml

    # Add the below configuration into the configMap.yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: mychart-configmap
    data:
        myvalue: "Hello World"


    # Install the helm chart
    helm install full-coral ./mychart

    # To view the installed template
    helm get manifest full-coral

    # To uninstall our release
    helm uninstall full-coral

    # To do a dry run with the debug information, without the actual installation
    heml install --debug --dry-run --disable-openapi-validation full-coral ./mychart
```