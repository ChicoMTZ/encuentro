from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from actividades.forms import *
from django.http import JsonResponse, HttpResponseBadRequest


@login_required()
def profileAddLike(request):
    profile = request.user.forum_user_profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.likes.add(speech)
    return JsonResponse({'messages': "Me gusta confirmado"})


@login_required()
def matricularse(request):
    profile = request.user.forum_user_profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.add(speech)
    return JsonResponse({'messages': "Matricula confirmada"})


@login_required()
def deleteMatricularse(request):
    profile = request.user.forum_user_profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.remove(speech)
    return JsonResponse({'mensaje': "Matricula eliminada"})


@login_required()
def deleteRecurso(request):
    user = request.user
    idRecurso = request.POST['id_recurso']
    recurso = get_object_or_404(SpeechResource, pk=idRecurso)
    if user != recurso.speech.user:
        return HttpResponseBadRequest()
    else:
        recurso.recurso.delete()
        recurso.delete()
    return JsonResponse({'mensaje': "Recurso eliminado"})
