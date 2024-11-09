# Implémentation du backend en Nestjs

Nest est un framework backend pour javascript, qui est très orienté objet.

Vous remarquerez que l'implémentation est donc très proche de nos backend python en OOP.

A quelques différences près, l'architecture est la même, donc si vous pouvez vous repérer dans le projet Flask ou FastAPI,
vous pouvez naturellement vous repérer dans celui en Nest. La différence étant la syntaxe et parfois quelques spécificités liées au framework.

Ici les modules sont dans le dossier framework car contrairement à Flask, Nestjs propose de réaliser pour nous l'injection de dépendance, mais cela à un "coût", il faut utiliser les décorateurs prévus à cet effet.

Pour le reste, les dossiers domains, infra et services ressemblent beaucoup à ce que nous avons implémenté en Python.

Je ne vous demande pas de comprendre l'entièreté du code du premier coup, simplement de voir qu'une fois que vous avez compris comment architecturer, vous pouvez passer d'un langage ou framework à un autre sans éprouver de difficulté.
