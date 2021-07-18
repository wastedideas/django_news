from django.shortcuts import render, HttpResponseRedirect
from django.views import generic, View
from app_news.models import New, Comment
from app_news.forms import NewCreate, UserComment


class NewsListView(generic.ListView):
    model = New
    template_name = 'news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(generic.DetailView):
    model = New
    template_name = 'news_detail.html'
    context_object_name = 'new_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments_form'] = UserComment()
        return context

    def post(self, request, pk):
        news = New(
            pk,
        )
        if self.request.user.is_authenticated:
            comment = Comment(
                new=news,
                comment_text=request.POST['comment_text'],
                user_name=request.user.username
            )
        else:
            comment = Comment(
                new=news,
                comment_text=request.POST['comment_text'],
                user_name=request.POST['user_name'] + ' (Анонимный пользователь)',
            )
        comment.save()
        return HttpResponseRedirect('/news')


class NewCreateView(View):
    def get(self, request):
        new_create = NewCreate()
        return render(
            request,
            'new_create.html',
            context={
                'new_create': new_create,
            },
        )

    def post(self, request):
        new_create = NewCreate(request.POST)
        if new_create.is_valid():
            New.objects.create(**new_create.cleaned_data)
            return HttpResponseRedirect('/news')
        return render(
            request,
            'new_create.html',
            context={
                'new_create': new_create,
            },
        )


class NewEditView(View):
    def get(self, request, new_id):
        new_edit = New.objects.get(id=new_id)
        new_edit_form = NewCreate(instance=new_edit)
        return render(
            request,
            'new_edit.html',
            context={
                'new_edit_form': new_edit_form,
                'new_id': new_id,
            },
        )

    def post(self, request, new_id):
        new_edit = New.objects.get(id=new_id)
        new_edit_form = NewCreate(
            request.POST,
            instance=new_edit,
        )
        if new_edit_form.is_valid():
            new_edit.save()
            return HttpResponseRedirect('/news')
        return render(
            request,
            'new_edit.html',
            context={
                'new_edit_form': new_edit_form,
                'new_id': new_id,
            },
        )
