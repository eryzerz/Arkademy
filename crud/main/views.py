from .forms import NameForm
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Name, Hobby, Category
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
# Create your views here.


class HomeListView(ListView):
    context_object_name="home_list"
    template_name='home.html'
    queryset=Name.objects.all()

    def get_context_data(self, **kwargs):
        context=super(HomeListView, self).get_context_data(**kwargs)
        context['hobby']=Hobby.objects.all()
        context['category']=Category.objects.all()

        return context

class NameCreateView(BSModalCreateView):
    template_name='create.html'
    form_class=NameForm
    success_message='Success: User was created'
    success_url=reverse_lazy('home')

class NameUpdateView(BSModalUpdateView):
    model=Name
    template_name='update.html'
    form_class=NameForm
    success_message='Success: User was updated'
    success_url=reverse_lazy('home')

class NameDeleteView(BSModalDeleteView):
    model=Name
    template_name='delate.html'
    success_message='Success: User was delated'
    success_url=reverse_lazy('home')
