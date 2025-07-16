from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def gabinete(request):
    return render(request, 'gabinete.html')

def hd(request):
    return render(request, 'hd.html')

def memoria(request):
    return render(request, 'memoria.html')

def meus_anuncios(request):
    return render(request, 'meus-anuncios.html')

def novo_anuncio(request):
    return render(request, 'novo_anuncio.html')

def perifericos(request):
    return render(request, 'perifericos.html')

def suporte_manutencao(request):
    return render(request, 'suporte_manutencao.html')

def pontos_de_coleta(request):
    return render (request, 'pontos _de_coleta.html')