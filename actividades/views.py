# -*- coding: utf-8 -*-
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from actividades.forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseBadRequest


@method_decorator(login_required, name='dispatch')
class foro(ListView):
    template_name = 'foro/foro.html'

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(foro, self).get(request, *arg, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return Topic.objects.filter(sites=get_current_site(self.request)).order_by('-date_created')


@method_decorator(login_required, name='dispatch')
class foro_topic(ListView):

    template_name = 'foro/foro_topic.html'
    context_object_name = 'topic_list'

    def get_queryset(self, *args, **kwargs):
        self.editor = self.kwargs['slug']
        return Speech.objects.filter(topic__slug=self.editor, topic__sites=get_current_site(self.request)).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super(foro_topic, self).get_context_data(**kwargs)
        try:
            context['topic'] = Topic.objects.get(slug=self.editor, sites=get_current_site(self.request))
        except ObjectDoesNotExist:
            raise Http404
        return context

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(foro_topic, self).get(request, *arg, **kwargs)


@method_decorator(login_required, name='dispatch')
class foro_detail(ListView):

    template_name = 'foro/foro_detail.html'
    context_object_name = 'speech_details'

    def get_queryset(self, *args, **kwargs):
        self.editor = self.kwargs['slug']
        self.detalles = self.kwargs['slug1']
        return Speech.objects.get(topic__slug=self.editor, slug=self.detalles, topic__sites=get_current_site(self.request))

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(foro_detail, self).get(request, *arg, **kwargs)


@method_decorator(login_required, name='dispatch')
class foro_types(ListView):

    template_name = 'foro/foro_types.html'
    context_object_name = 'foro_types'

    def get_queryset(self, *args, **kwargs):
        self.types = self.kwargs['slug']
        return Speech.objects.filter(speech_type__slug= self.types, topic__sites=get_current_site(self.request))

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(foro_types, self).get(request, *arg, **kwargs)


@method_decorator(login_required, name='dispatch')
class insert_speech(SuccessMessageMixin, CreateView):
    template_name = 'foro/insert_speech.html'
    model = Speech
    form_class = InsertSpeech
    success_url = '/activity/'
    success_message = "La actividad fue creada. Necesita la aprobación de un administrador"

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        try:
            self.speech_slug = get_object_or_404(Speech, slug=self.kwargs['slug'])
        except Http404:
            self.topic_slug = get_object_or_404(Topic, slug=self.kwargs['slug'])
        return super(insert_speech, self).get(request, *arg, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.topic_slug = get_object_or_404(Topic, slug=self.kwargs['slug'])
        form.instance.topic = self.topic_slug
        form.instance.slug = slugify(form.instance.user.username + ' ' + form.instance.title)
        form.instance.sites = get_current_site(self.request)
        try:
            return super(insert_speech, self).form_valid(form)
        except IntegrityError:
            messages.add_message(self.request, messages.WARNING, 'Ya usted creo una actividad con el mismo título')
            return redirect('Insert_Speech', slug=self.kwargs['slug'])


@method_decorator(login_required, name='dispatch')
class subirRecurso(CreateView):
    model = SpeechResource
    fields = ('recurso', )
    template_name = 'foro/subir_recurso.html'

    def form_valid(self, form):
        form.instance.speech = get_object_or_404(Speech, pk=self.kwargs['speech_id'])
        form.instance.user = self.request.user
        form.instance.sites = get_current_site(self.request)
        return super(subirRecurso, self).form_valid(form)

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(subirRecurso, self).get(request, *arg, **kwargs)


@method_decorator(login_required, name='dispatch')
class createProfile(SuccessMessageMixin, CreateView):
    template_name = 'usuarios_foro/create_profile.html'
    model = Forum_User_Profile
    form_class = EditProfileForm
    success_url = '/activity/'
    success_message = "La perfil fue creado con éxito"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.sites = get_current_site(self.request)
        return super(createProfile, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    form_class = EditProfileForm
    template_name = 'usuarios_foro/my_edit_profile.html'
    success_url = "/"
    model = Forum_User_Profile


@method_decorator(login_required, name='dispatch')
class view_profile_forum(DetailView):
    template_name = 'usuarios_foro/view_profile.html'
    model = Forum_User_Profile

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(view_profile_forum, self).get(request, *arg, **kwargs)


