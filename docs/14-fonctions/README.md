%title: Helm
%author: xavki
%Vidéos: [Helm]()
%blog: [Xavki Blog](https://xavki.blog)

# HELM : Fonctions 

<br>

PRINT...

```
print "Hello " .Values.var1 " !!!"
```

<br>

TRIM

```
trim "   Salut    "
trimAll "+" "+10"
trimPrefix "+" "+200"
trimSuffix "." "200."
```

-------------------------------------------------------------

# HELM : Fonctions 

<br>

LOWER/UPPER

```
lower "HELLO"
upper "hello"
title "hello xavki"
```

<br>

REPEAT

```
repeat 3 "xavki"	
```

-------------------------------------------------------------

# HELM : Fonctions 

<br>

SUBSTRING/TRUNC/INITIALS

```
substr 0 5 "hello xavki"
trunc 5 "hello xavki"
initials "Hello Xavki"
```

<br>

NOSPACE

```
nospace "h e l l o x a v k i"
```

-------------------------------------------------------------

# HELM : Fonctions 

<br>

RAND

```
randAlphaNum uses 0-9a-zA-Z
randAlpha uses a-zA-Z
randNumeric uses 0-9
randAscii uses all printable ASCII characters
```

```
randNumeric 3
```

-------------------------------------------------------------

# HELM : Fonctions 

<br>

CONTAINS/PREFIX

```
contains "xav" "xavki"
hasPrefix "xav" "xavier"
```

<br>

QUOTE/SQUOTE

```
quote .Values.var1
squote .Values.var1
```

-------------------------------------------------------------

# HELM : Fonctions 

<br>

CAT

```
cat "Hello "  "Xavki"  "!!!"
```

<br>

INDENT/NINDENT

```
indent 4 .Values.var1
nindent 4 .Values.var1
```

<br>

REPLACE

```
"Hello-Xavki" | replace "-" " "
```

-------------------------------------------------------------

# HELM : Fonctions 

<br>

SNAKECASE/CAMELCASE/KEBABCASE/SWAPCASE

```
snakecase "FirstName"
camelcase "http_server"
kebabcase "FirstName"
swapcase "This Is A.Test"
```

<br>

SHUFFLE

```
shuffle "hello"
```
