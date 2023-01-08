from django.shortcuts import render
import os
import pyttsx3

# coloquei import os pra usar esse recurso de text-to-speech

# https://www.google.com/search?q=csv+acentua%C3%A7%C3%A3o&sxsrf=AOaemvKCedXcl4oWC79sxXucm25UqAXLNA%3A1642467061067&source=hp&ei=9Q7mYczgAffY1sQP1suV4AY&iflsig=ALs-wAMAAAAAYeYdBTy0N9YxnRB9KHYuDkuE8HpaWvMT&ved=0ahUKEwiMr-nNirr1AhV3rJUCHdZlBWwQ4dUDCAY&uact=5&oq=csv+acentua%C3%A7%C3%A3o&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeOgQIIxAnOgsIABCABBCxAxCDAToICC4QsQMQgwE6CwguEIAEEMcBEKMCOg4ILhCABBCxAxDHARCjAjoICAAQgAQQsQM6DgguEIAEELEDEMcBENEDOggILhCABBCxAzoFCAAQgAQ6CAgAELEDEIMBOgUILhCABDoLCC4QgAQQsQMQgwE6CAgAEBYQChAeOgQIABANOgYIABANEB46CAgAEA0QBRAeUABYzy5g9kNoBHAAeACAAZwBiAGiFJIBBDAuMTiYAQCgAQE&sclient=gws-wiz
from django.shortcuts import render, redirect
# from django.http import HttpResponse

from django.db import connection
from random import randint
from .models import dictclass
from .forms import DictForm, DictForm2, ImageForm, MudarTabelaForm, DictForm_Busca, DictForm_Novo, DictForm_suaresposta

# importei esse gtts agora... É só digitar e ele mesmo vai pedir pra instalar
### chamar depois ###
from gtts import gTTS
# from gtts import *

import sqlite3
from django.shortcuts import render

### chamar depois ###
#from django.conf import settings

### chamar depois ###
#from django.core.files.storage import FileSystemStorage

### alterei 1 ###
from django.db.models import Count

#from time import sleep

from django.http import HttpResponse

from django.db import connection

#import datetime
#import csv
#from django.contrib.auth.views import LogoutView
#from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

def Entrada(request):
    return render(request, "dictapp/Entrada.html")

# @login_required
def Entrada_Iniciar(request):

    if request.POST.get('comecar_sessao_ale'):
        banquinho = 'db_ale_01__'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ale', pk=n_primeiro)

    if request.POST.get('comecar_sessao_ing'):
        banquinho = 'db_ing_01__'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ing', pk=n_primeiro)

    """
    if request.POST.get('testar_uploader'):
        banquinho = 'db_ale_01__'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'core/simple_upload.html')
    """
    return render(request, "dictapp/Entrada_iniciar.html")

# @staff_member_required
def Entrada_configuracoes(request):
    """"
    if request.POST.get('editar_eprogModel'):
        return redirect('url_Editar_EprogModel', pk=1)

    if request.POST.get('editar_calculosModel'):
        return redirect('url_Editar_CalculosModel', pk=1)

    if request.POST.get('editar_procedimentoModel'):
        return redirect('url_Editar_ProcedimentoModel', pk=1)

    if request.POST.get('editar_sessaoModel'):
        return redirect('url_Editar_SessaoModel', pk=1)

    if request.POST.get('reset_eprogModel'):
        return redirect('url_Reset_EprogModel')

    if request.POST.get('reset_calculosModel'):
        return redirect('url_Reset_CalculosModel')

    if request.POST.get('reset_procedimentoModel'):
        return redirect('url_Reset_procedimentoModel')

    if request.POST.get('reset_sessaoModel'):
        return redirect('url_Reset_SessaoModel', pk=1)
    """

    return render(request, "dictapp/Entrada_configuracoes.html")

# @staff_member_required
def Entrada_relatorios(request):
    """
    user = request.user
    banquinho = str(user)
    if request.POST.get('export'):
        #listax = SessaoModel.objetos.using(banquinho).all()
        #listax = SessaoModel.objetos.using(banquinho).values()
        listax= SessaoModel.objetos.using(banquinho).values_list(
            'Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent', )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(['Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent'])
        for item in listax:
            print(item)
            writer = csv.writer(response)
            writer.writerow([item])
        return response
        """
    return render(request, "dictapp/Entrada_relatorios.html")

def Entrada_sobre(request):
    return render(request, "dictapp/Entrada_sobre.html")


### alterei 1 ###
def Entrada_Iniciar(request):
    # objetinho = dictclass.objetos.using('db_ale_01__').get(pk=1)
    # objetinho.qualtabela2 = 'db_ale_01__'
    # objetinho.save()

    # if request.POST.get('comecar_sessao'):
    #    return redirect('url_sessao_testar', pk=n_rand)

    if request.POST.get('comecar_sessao_ale'):
        banquinho = 'db_ale_01__'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ale', pk=n_primeiro)

    ### chamar depois ###

    ### alterei 1 ###
    if request.POST.get('comecar_sessao_ing'):
        banquinho = 'db_ing_01__'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ing', pk=n_primeiro)

    ### chamar depois ###
    """
    if request.POST.get('testar_uploader'):
        banquinho = 'db_ale_01__'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'core/simple_upload.html')
        # return redirect('url_principal_ale', pk=n_primeiro)
    """

    return render(request, "dictapp/Entrada_iniciar.html")


def principal_ale(request, pk):
    data = {}
    banquinho = 'db_ale_01__'
    objetinho = dictclass.objetos.using(banquinho).get(pk=1)
    objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_linhaum.qualtabela2
    qualtabela_x = str(qualtabela_a)

    ### alterei 1 ###
    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        print('esse pk NÃO existe')
        return redirect('url_principal_ale', pk=1)
    ###################################################################

    obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
    n_primeiro = obj_primeiro.id
    campo = 'id'
    obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
    valor_ultimo = getattr(obj_ultimo, campo)
    total = valor_ultimo
    obj_atual = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj_atual, campo)
    n = valor_campo
    # n = valor_campo + 1
    # if n > total:
    #   n = n_primeiro

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=n)

    ### fim de Verificando se o pk (de objetinho) existe ou reposicionando ###

    objetinho_novo_linhaum = dictclass.objetos.using(qualtabela_x).get(pk=1)
    form_busca = DictForm_Busca(request.POST or None, instance=objetinho_novo_linhaum)
    # objetinho = dictclass.objetos.using(banquinho).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    objsuaresp = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    objsuaresp.suaresposta1 = ''
    x = objsuaresp.suaresposta1
    objsuaresp.save()

    campo = 'id'
    obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo
    ### chamar depois ###
    # Para usar no pythonanywhere
    frasex = obj.frase
    tts = gTTS(text=frasex, lang='de')
    tts.save('ale.mp3')


    """
    # para usar no desktop
    # caminho = os.path.join(settings.BASE_DIR, "media/")
    # frasex = obj.frase
    # tts = gTTS(text=frasex, lang='de')
    # tts.save(caminho + "ale.mp3")
    """

    campo = 'id'
    obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo

    if request.POST.get('Sair'):
        return redirect('url_entrada')

    if request.POST.get('Testar_pyttsx3'):
        ### chamar depois ###
        # https://pypi.org/project/pyttsx3/
        objetinho_provis = dictclass.objetos.using('db_ale_01__').get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        qualtabela_x = str(qualtabela_a)
        print('qual tabela é: ', qualtabela_x)
        objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)
        form = DictForm(request.POST or None, instance=objetinho)

        engine = pyttsx3.init()
        engine.say("Pasta. I wish I could have some pasta tonight, but I am really fat")
        engine.runAndWait()
        for voice in engine.getProperty('voices'):
            print(voice)


        return redirect('url_principal_ale', pk=pk)

    ### chamar depois ###
    #if request.POST.get('Upload'):
    #    # fazer o logout aqui:
    #    return redirect('url_sessao_upload_ale', pk=pk)

    ### chamar depois ###
    #if request.POST.get('qualtabela'):
    #   return redirect('url_sessao_tabela_ale', pk=pk)

    if request.POST.get('Novo'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        objeto_ultimo = dictclass.objetos.using(qualtabela_a).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = dictclass.objetos.using(qualtabela_a).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Ordem = pk_next
        objeto_novo.palavra = ''
        objeto_novo.palavratrad = ''
        objeto_novo.frase = ''
        objeto_novo.frasetrad = ''
        objeto_novo.frase2 = ''
        objeto_novo.frasetrad2 = ''
        objeto_novo.frase3 = ''
        objeto_novo.frasetrad3 = ''
        objeto_novo.figura1 = '/static/dictapp/img/vazio.jpg'
        objeto_novo.som1 = '/static/dictapp/sons/vazio.mp3'
        objeto_novo.save()
        return redirect('url_editar_ale', pk=pk_next)

    if request.POST.get('Editar'):
        objetinho_provis = dictclass.objetos.using('db_ale_01__').get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        qualtabela_x = str(qualtabela_a)
        print('qual tabela é: ', qualtabela_x)
        objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)

        form = DictForm(request.POST or None, instance=objetinho)
        return redirect('url_editar_ale', pk=pk)

    if request.POST.get('Excluir'):
        # excluir registro ale
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        if not pk == 1:
            objetinho.delete()
            print('apagando mais uma vez')
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        total = dictclass.objetos.using(qualtabela_a).count()

        ### Verificando se o pk existe ou reposicionando ###
        n = 1
        pk = 1
        print('tentando arrumar o id de novo')
        while n <= total:
            if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                n = n + 1
                pk = pk + 1
            else:
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk + 1)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                pk = pk + 1

        ### deletando o último registro, que está duplicado ###
        obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
        obj_ultimo.delete()

        return redirect('url_principal_ale', pk=1)

    if request.POST.get('primeiro'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ale', pk=n_primeiro)

    if request.POST.get('proximo'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        # user = request.user
        # banquinho = str(user)
        obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = n_primeiro

        return redirect('url_principal_ale', pk=n)

    if request.POST.get('anterior'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = n_primeiro

        return redirect('url_principal_ale', pk=n)

    if request.POST.get('Sortear_AlePort'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        ### Verificando se o pk (de objetinho) existe ou reposicionando ###
        if dictclass.objetos.using(qualtabela_a).filter(pk=n_rand).exists():
            print('esse pk existe')
        else:
            print('esse pk NÃO existe')
            return redirect('url_principal_ale', pk=1)
        ###################################################################
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou
        return redirect('url_sessao_testar_ale', pk=n_rand)

    if request.POST.get('Sortear_PortAle'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou

        return redirect('url_sessao_testar_port_ale', pk=n_rand)

    if request.POST.get('Sortear_Audio'):
        # objetX = EprogModel.objetos.using(banquinho).get(pk=pk)
        # objetX.SuaResposta = ''
        # objetX.save()
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou

        return redirect('url_sessao_testar_audio_ale', pk=n_rand)

    if request.POST.get('Sortear_Figura'):
        # objetX = EprogModel.objetos.using(banquinho).get(pk=pk)
        # objetX.SuaResposta = ''
        # objetX.save()
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou

        return redirect('url_sessao_testar_figura_ale', pk=n_rand)

    if request.POST.get('ultimo'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        qualtabela_x = str(qualtabela_a)
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        # form = DictForm(request.POST or None, instance=objetinho)

        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_principal_ale', pk=n)

    if request.POST.get('audio_f1'):
        os.system('ale.mp3')
        return redirect('url_principal_ale', pk=n)

    if request.POST.get('Correta'):
        banquinho = 'db_ale_01__'
        objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_linhaum.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        objetinho_novo_linhaum = dictclass.objetos.using(qualtabela_x).get(pk=1)
        objetinho.SuaResposta = ''
        objetinho.Acertou = '1'
        objetinho.Jafoi = '1'
        objetinho.save()
        if objetinho.id == 1:
            objetinho_novo_linhaum.Acertou = '1'
            objetinho_novo_linhaum.Jafoi = '1'
            objetinho_novo_linhaum.save()
        tcorretas = dictclass.objetos.using(qualtabela_a).filter(Acertou='1').count()
        objetinho_novo_linhaum.Corretas = str(tcorretas)
        objetinho_novo_linhaum.save()
        campo = 'id'

        obj_ult = dictclass.objetos.using(qualtabela_a).last()
        total_rec = getattr(obj_ult, campo)
        tporcentagem = int((tcorretas / total_rec) * 100)
        objetinho_novo_linhaum.Porcentagem = str(tporcentagem) + '%'
        objetinho_novo_linhaum.save()

        if tcorretas == total_rec:
            return redirect('url_parabens_view')

        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Incorreta'):
        banquinho = 'db_ale_01__'
        objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_linhaum.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        objetinho.SuaResposta = ''
        objetinho.Acertou = '0'
        objetinho.Jafoi = '1'
        objetinho.save()
        if objetinho.id == 1:
            objetinho_linhaum.Acertou = '0'
            objetinho_linhaum.Jafoi = '1'
            objetinho_linhaum.save()

        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('salvar_editados'):
        data = {}
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        form2 = DictForm2(request.POST or None, instance=objetinho)
        # form3 = DictForm_Novo(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        # if form3.is_valid():
        #    form3.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('busquei'):
        data = {}
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        form = DictForm(request.POST or None, instance=objetinho)
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        if form.is_valid():
            form.save()
        x_busca = objetinho.suaresposta2
        try:
            objetinho_buscado = dictclass.objetos.using(qualtabela_a).get(palavra=x_busca)
            pk_novo = objetinho_buscado.pk
            return redirect('url_principal_ale', pk=pk_novo)
        except:
            return redirect('url_principal_ale', pk=1)

    if request.POST.get('Resetar_idpk'):
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        total = dictclass.objetos.using(qualtabela_a).count()
        print('Quantos registros: ', total)

        ### Verificando se o pk existe ou reposicionando ###
        n = 1
        pk = 1
        while n <= total:
            if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                n = n + 1
                pk = pk + 1
            else:
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk + 1)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                pk = pk + 1

        ### deletando o último registro, que está duplicado ###
        obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
        obj_ultimo.delete()

        return redirect('url_principal_ale', pk=1)

    if request.POST.get('Resetar_Corretas'):
        banquinho = 'db_ale_01__'
        objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_linhaum.qualtabela2
        objetinho_novo_linhaum = dictclass.objetos.using(qualtabela_a).get(pk=1)
        objeto_tudo = dictclass.objetos.using(qualtabela_a).all()
        objetinho_novo_linhaum.Corretas = '0'
        objetinho_novo_linhaum.Porcentagem = '0'
        objetinho_novo_linhaum.save()

        for item in objeto_tudo:
            item.Acertou = '0'
            item.Jafoi = '0'
            item.save()

        return redirect('url_principal_ale', pk=1)

    context = {
        'objetinho': objetinho,
        ### alterei 1 ###
        'form': form,
        'form_busca': form_busca,
        'objetinho_linhaum': objetinho_linhaum,
        'objetinho_novo_linhaum': objetinho_novo_linhaum
    }

    return render(request, 'dictapp/principal_ale.html', context)


def editar_ale(request, pk):
    data = {}
    banquinho = 'db_ale_01__'

    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2
    qualtabela_x = str(qualtabela_a)
    objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        # return redirect('url_Entrada_Iniciar')
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    return render(request, 'dictapp/Editar_ale.html', data)


def sessao_testar_ale(request, pk):
    data = {}
    banquinho = 'db_ale_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2

    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        return redirect('url_principal_ale', pk=1)

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_ale.html", context)


def sessao_testar_port_ale(request, pk):
    data = {}
    banquinho = 'db_ale_01__'

    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2
    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_port_ale.html", context)

def sessao_testar_audio_ale(request, pk):
    ### chamar depois ###
    """
    data = {}
    banquinho = 'db_ale_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2

    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        return redirect('url_principal_ale', pk=1)

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    campo = 'id'
    obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo
    frasex = obj.frase
    caminho = os.path.join(settings.BASE_DIR, "media/")
    frasex = obj.frase
    tts = gTTS(text=frasex, lang='de')
    tts.save(caminho + "ale.mp3")

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }

    return render(request, "dictapp/sessao_testar_audio_ale.html", context)
    """
    return render(request, "dictapp/sessao_testar_audio_ale.html", pk=1)


def sessao_testar_figura_ale(request, pk):
        data = {}
        banquinho = 'db_ale_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        ### Verificando se o pk (de objetinho) existe ou reposicionando ###
        if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
            print('esse pk existe')
            # n = n + 1
        else:
            return redirect('url_principal_ale', pk=1)

        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

        form = DictForm(request.POST or None, instance=objetinho)
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if request.POST.get('Resposta'):
            form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
            if form3.is_valid():
                form3.save()
            return redirect('url_principal_ale', pk=pk)

        if request.POST.get('Sair'):
            return redirect('url_Entrada_Iniciar')

        context = {
            "form": form,
            "form2": form2,
            "objetinho": objetinho,
        }
        return render(request, "dictapp/sessao_testar_figura_ale.html", context)

def parabens_view(request):
    if request.POST.get('Voltar'):
        return redirect('url_Entrada_Iniciar')
    return render(request, "dictapp/Parabens.html")

def sessao_upload_ale(request, pk):
    banquinho = 'db_ale_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2
    qualtabela_x = str(qualtabela_a)

    objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)

    # https: // stackoverflow.com / questions / 4526273 / what - does - enctype - multipart - form - data - mean

    if request.POST.get('Voltar'):
        #return redirect('url_Entrada_Iniciar')
        return redirect('url_principal_ale', pk=pk)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            instance = form.save()
            caminho = instance.image.name
            caminho_mesmo = instance.image.path
            objetinho.figura1 = '/media/' + caminho
            objetinho.save()
            return render(request, 'dictapp/sessao_upload_ale.html',
                          {'form': form, 'objetinho': objetinho, 'img_obj': img_obj})
    else:
        form = ImageForm()

    context = {
        'form': form,
        'objetinho': objetinho,
    }

    return render(request, 'dictapp/sessao_upload.html', context)

def sessao_upload_ing(request, pk):
    banquinho = 'db_ing_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2
    qualtabela_x = str(qualtabela_a)

    objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)

    # https: // stackoverflow.com / questions / 4526273 / what - does - enctype - multipart - form - data - mean

    if request.POST.get('Voltar'):
        #return redirect('url_Entrada_Iniciar')
        return redirect('url_principal_ing', pk=pk)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            instance = form.save()
            caminho = instance.image.name
            caminho_mesmo = instance.image.path
            objetinho.figura1 = '/media/' + caminho
            objetinho.save()
            return render(request, 'dictapp/sessao_upload_ing.html',
                          {'form': form, 'objetinho': objetinho, 'img_obj': img_obj})
    else:
        form = ImageForm()

    context = {
        'form': form,
        'objetinho': objetinho,
    }

    return render(request, 'dictapp/sessao_upload_ing.html', context)

def sessao_tabela_ale(request, pk):
    data = {}
    banquinho = 'db_ale_01__'

    # objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    # qualtabela_a = objetinho_provis.qualtabela
    # qualtabela_x = str(qualtabela_a)
    # banquinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)

    objetinho = dictclass.objetos.using(banquinho).get(pk=1)
    form = MudarTabelaForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        return redirect('url_Entrada_Iniciar')
    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    context = {
        'form': form,
        'objetinho': objetinho,
    }

    return render(request, 'dictapp/sessao_tabela_ale.html', context)

def criar(request):
    data = {}
    form = DictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "dictapp/Entrada_iniciar.html")
    data['form'] = form
    # return render(request, 'dictapp/form2.html', data)
    return render(request, 'dictapp/principal_vazio.html', data)

def editar_ing(request, pk):
    data = {}
    banquinho = 'db_ing_01__'

    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2
    qualtabela_x = str(qualtabela_a)
    objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        return redirect('url_Entrada_Iniciar')
    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    return render(request, 'dictapp/Editar_ing.html', data)

def sessao_testar_port_ing(request, pk):
    data = {}
    banquinho = 'db_ing_01__'

    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2
    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_port_ing.html", context)

def sessao_testar_figura_ing(request, pk):
    data = {}
    banquinho = 'db_ing_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2

    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        return redirect('url_principal_ing', pk=1)

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_figura_ing.html", context)

def sessao_testar_audio_ing(request, pk):
    ### chamar depois ###
    """
    data = {}
    banquinho = 'db_ing_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2

    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        return redirect('url_principal_ing', pk=1)

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    campo = 'id'
    obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo
    frasex = obj.frase
    caminho = os.path.join(settings.BASE_DIR, "media/")
    frasex = obj.frase
    tts = gTTS(text=frasex, lang='de')
    tts.save(caminho + "ing.mp3")

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }

    return render(request, "dictapp/sessao_testar_audio_ing.html", context)
    """
    return render(request, "dictapp/sessao_testar_audio_ing.html", pk=1)

def sessao_testar_ing(request, pk):
    data = {}
    banquinho = 'db_ing_01__'
    objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_provis.qualtabela2

    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        return redirect('url_principal_ing', pk=1)

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form3 = DictForm_suaresposta(request.POST or None, instance=objetinho)
        if form3.is_valid():
            form3.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_ing.html", context)

def sessao_tabela_ing(request, pk):
    banquinho = 'db_ing_01__'

    objetinho = dictclass.objetos.using(banquinho).get(pk=1)
    form = MudarTabelaForm(request.POST or None, instance=objetinho)
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        return redirect('url_Entrada_Iniciar')
    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    context = {
        'form': form,
        'objetinho': objetinho,
    }

    return render(request, 'dictapp/sessao_tabela_ing.html', context)


def principal_ing(request, pk):
    data = {}
    banquinho = 'db_ing_01__'
    objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
    qualtabela_a = objetinho_linhaum.qualtabela2
    qualtabela_x = str(qualtabela_a)

    ### Verificando se o pk (de objetinho) existe ou reposicionando ###
    if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
        print('esse pk existe')
        # n = n + 1
    else:
        print('esse pk NÃO existe')
        return redirect('url_principal_ing', pk=1)
    ###################################################################

    obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
    n_primeiro = obj_primeiro.id
    campo = 'id'
    obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
    valor_ultimo = getattr(obj_ultimo, campo)
    total = valor_ultimo
    obj_atual = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj_atual, campo)
    n = valor_campo
    # n = valor_campo + 1
    # if n > total:
    #   n = n_primeiro

    objetinho = dictclass.objetos.using(qualtabela_a).get(pk=n)

    ### fim de Verificando se o pk (de objetinho) existe ou reposicionando ###

    objetinho_novo_linhaum = dictclass.objetos.using(qualtabela_x).get(pk=1)
    form_busca = DictForm_Busca(request.POST or None, instance=objetinho_novo_linhaum)
    # objetinho = dictclass.objetos.using(banquinho).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    objsuaresp = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    objsuaresp.suaresposta1 = ''
    x = objsuaresp.suaresposta1
    objsuaresp.save()

    campo = 'id'
    obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo
    # parei aqui

    ### chamar depois ###
    # Para usar no pythonanywhere
    # frasex = obj.frase
    # tts = gTTS(text=frasex, lang='de')
    # tts.save('ing.mp3')

    """
    caminho = os.path.join(settings.BASE_DIR, "media/")
    frasex = obj.frase
    tts = gTTS(text=frasex, lang='en')
    tts.save(caminho + "ing.mp3")
    """

    campo = 'id'
    obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo

    if request.POST.get('Sair'):
        return redirect('url_entrada')

    if request.POST.get('Upload'):
        # fazer o logout aqui:
        return redirect('url_sessao_upload_ing', pk=pk)

    if request.POST.get('qualtabela'):
        return redirect('url_sessao_tabela_ing', pk=pk)

    if request.POST.get('Novo'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        objeto_ultimo = dictclass.objetos.using(qualtabela_a).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = dictclass.objetos.using(qualtabela_a).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Ordem = pk_next
        objeto_novo.palavra = ''
        objeto_novo.palavratrad = ''
        objeto_novo.frase = ''
        objeto_novo.frasetrad = ''
        objeto_novo.frase2 = ''
        objeto_novo.frasetrad2 = ''
        objeto_novo.frase3 = ''
        objeto_novo.frasetrad3 = ''
        objeto_novo.figura1 = '/static/dictapp/img/vazio.jpg'
        objeto_novo.som1 = '/static/dictapp/sons/vazio.mp3'
        objeto_novo.save()
        return redirect('url_editar_ing', pk=pk_next)

    if request.POST.get('Editar'):
        data = {}
        objetinho_provis = dictclass.objetos.using('db_ing_01__').get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        qualtabela_x = str(qualtabela_a)
        print('qual tabela é: ', qualtabela_x)
        objetinho = dictclass.objetos.using(qualtabela_x).get(pk=pk)

        form = DictForm(request.POST or None, instance=objetinho)
        return redirect('url_editar_ing', pk=pk)

    if request.POST.get('Excluir'):
        # excluir registro ing
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        if not pk == 1:
            objetinho.delete()
            print('apagando mais uma vez')
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        total = dictclass.objetos.using(qualtabela_a).count()

        ### Verificando se o pk existe ou reposicionando ###
        n = 1
        pk = 1
        print('tentando arrumar o id de novo')
        while n <= total:
            if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                n = n + 1
                pk = pk + 1
            else:
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk + 1)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                pk = pk + 1

        ### deletando o último registro, que está duplicado ###
        obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
        obj_ultimo.delete()

        return redirect('url_principal_ing', pk=1)

    if request.POST.get('primeiro'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ing', pk=n_primeiro)

    if request.POST.get('proximo'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        # user = request.user
        # banquinho = str(user)
        obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = n_primeiro

        return redirect('url_principal_ing', pk=n)

    if request.POST.get('anterior'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = n_primeiro

        return redirect('url_principal_ing', pk=n)

    if request.POST.get('Sortear_ingPort'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        ### Verificando se o pk (de objetinho) existe ou reposicionando ###
        if dictclass.objetos.using(qualtabela_a).filter(pk=n_rand).exists():
            print('esse pk existe')
        else:
            print('esse pk NÃO existe')
            return redirect('url_principal_ing', pk=1)
        ###################################################################
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou
        return redirect('url_sessao_testar_ing', pk=n_rand)

    if request.POST.get('Sortear_Porting'):
        # objetX = EprogModel.objetos.using(banquinho).get(pk=pk)
        # objetX.SuaResposta = ''
        # objetX.save()
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou

        return redirect('url_sessao_testar_port_ing', pk=n_rand)

    if request.POST.get('Sortear_Audio'):
        # objetX = EprogModel.objetos.using(banquinho).get(pk=pk)
        # objetX.SuaResposta = ''
        # objetX.save()
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou

        return redirect('url_sessao_testar_audio_ing', pk=n_rand)

    if request.POST.get('Sortear_Figura'):
        # objetX = EprogModel.objetos.using(banquinho).get(pk=pk)
        # objetX.SuaResposta = ''
        # objetX.save()
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
        SeAcertou = obj_sorteio.Acertou
        while SeAcertou == '1':
            n_rand = randint(1, total)
            obj_sorteio = dictclass.objetos.using(qualtabela_a).get(pk=n_rand)
            SeAcertou = obj_sorteio.Acertou

        return redirect('url_sessao_testar_figura_ing', pk=n_rand)

    if request.POST.get('ultimo'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        qualtabela_x = str(qualtabela_a)
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        # form = DictForm(request.POST or None, instance=objetinho)

        campo = 'id'
        obj = dictclass.objetos.using(qualtabela_a).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_principal_ing', pk=n)

    if request.POST.get('audio_f1'):
        os.system('ing.mp3')
        return redirect('url_principal_ing', pk=n)

    if request.POST.get('Correta'):
        banquinho = 'db_ing_01__'
        objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_linhaum.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        objetinho_novo_linhaum = dictclass.objetos.using(qualtabela_x).get(pk=1)
        objetinho.SuaResposta = ''
        objetinho.Acertou = '1'
        objetinho.Jafoi = '1'
        objetinho.save()
        if objetinho.id == 1:
            objetinho_novo_linhaum.Acertou = '1'
            objetinho_novo_linhaum.Jafoi = '1'
            objetinho_novo_linhaum.save()
        tcorretas = dictclass.objetos.using(qualtabela_a).filter(Acertou='1').count()
        objetinho_novo_linhaum.Corretas = str(tcorretas)
        objetinho_novo_linhaum.save()
        campo = 'id'

        obj_ult = dictclass.objetos.using(qualtabela_a).last()
        total_rec = getattr(obj_ult, campo)
        tporcentagem = int((tcorretas / total_rec) * 100)
        objetinho_novo_linhaum.Porcentagem = str(tporcentagem) + '%'
        objetinho_novo_linhaum.save()

        if tcorretas == total_rec:
            return redirect('url_parabens_view')

        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Incorreta'):
        banquinho = 'db_ing_01__'
        objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_linhaum.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        objetinho.SuaResposta = ''
        objetinho.Acertou = '0'
        objetinho.Jafoi = '1'
        objetinho.save()
        if objetinho.id == 1:
            objetinho_linhaum.Acertou = '0'
            objetinho_linhaum.Jafoi = '1'
            objetinho_linhaum.save()

        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('salvar_editados'):
        data = {}
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        form2 = DictForm2(request.POST or None, instance=objetinho)
        # form3 = DictForm_Novo(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        # if form3.is_valid():
        #    form3.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('busquei'):
        data = {}
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2

        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        form = DictForm(request.POST or None, instance=objetinho)
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        if form.is_valid():
            form.save()
        x_busca = objetinho.suaresposta2
        try:
            objetinho_buscado = dictclass.objetos.using(qualtabela_a).get(palavra=x_busca)
            pk_novo = objetinho_buscado.pk
            return redirect('url_principal_ing', pk=pk_novo)
        except:
            return redirect('url_principal_ing', pk=1)

    if request.POST.get('Resetar_idpk'):
        banquinho = 'db_ing_01__'
        objetinho_provis = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_provis.qualtabela2
        objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
        obj_primeiro = dictclass.objetos.using(qualtabela_a).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        total = dictclass.objetos.using(qualtabela_a).count()
        print('Quantos registros: ', total)

        ### Verificando se o pk existe ou reposicionando ###
        n = 1
        pk = 1
        while n <= total:
            if dictclass.objetos.using(qualtabela_a).filter(pk=pk).exists():
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                n = n + 1
                pk = pk + 1
            else:
                objetinho = dictclass.objetos.using(qualtabela_a).get(pk=pk + 1)
                objetinho.Ordem = n
                objetinho.id = objetinho.Ordem
                objetinho.save()
                pk = pk + 1

        ### deletando o último registro, que está duplicado ###
        obj_ultimo = dictclass.objetos.using(qualtabela_a).last()
        obj_ultimo.delete()

        return redirect('url_principal_ing', pk=1)

    if request.POST.get('Resetar_Corretas'):
        banquinho = 'db_ing_01__'
        objetinho_linhaum = dictclass.objetos.using(banquinho).get(pk=1)
        qualtabela_a = objetinho_linhaum.qualtabela2
        objetinho_novo_linhaum = dictclass.objetos.using(qualtabela_a).get(pk=1)
        objeto_tudo = dictclass.objetos.using(qualtabela_a).all()
        objetinho_novo_linhaum.Corretas = '0'
        objetinho_novo_linhaum.Porcentagem = '0'
        objetinho_novo_linhaum.save()

        for item in objeto_tudo:
            item.Acertou = '0'
            item.Jafoi = '0'
            item.save()

        return redirect('url_principal_ing', pk=1)

        context = {
        'form': form,
        'form_busca': form_busca,
        'objetinho': objetinho,
        'objetinho_linhaum': objetinho_linhaum,
        'objetinho_novo_linhaum': objetinho_novo_linhaum}
    return render(request, 'dictapp/principal_ing.html', context)

def Entrada_login(request):
    usuario = request.user
    if request.POST.get('Visitante'):
        request.user = User.objects.get(username='visitante')
        usuario = User(username='visitante')
        u = User.objects.get(username='visitante')
        u.save()

    context = {
        "user": usuario
    }

    return render(request, "dictapp/Entrada_login.html", context)