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
            background-image: url("{% static 'img/backgroundmain.jpg' %}"); 
            background-size: cover; 
            background-position: center; 
            background-repeat: no-repeat; 
            background-attachment: fixed;
            padding-top: 70px; /* Espacio para el header fijo */
        }

        #button {
            padding: 15px 30px;
            font-size: 20px;
            background-color: #ff5733;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
        }

        #button:hover {
            background-color: #ff3319;
        }
    </style>
    <title>ByteSize</title>
</head>

<body>
    <a id="button" href="url 'noticias'">Ir a otra página</a>
</body>

</html>
                        """
    )