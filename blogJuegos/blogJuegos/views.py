from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: black;
            color: white;
        }
    </style>
    <title>Document</title>
</head>

<body>
<h1> BIENVENIDOS AL PROYECTO DEL BLOG DE VIDEOJUEGOS DEL GRUPO 9 DE LA COMISIÓN 5 </h1>
<p>Esto es párrafo</p>
<ul>
    <li>Por favor coloca /posts en la url para acceder</li>
    
</ul
</body>

</html>
                        """
    )