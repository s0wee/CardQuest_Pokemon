from django.shortcuts import render
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'base'  # The name used in the template for the list of objects
    template_name = "base.html"   # The template file to be rendered

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'  # The name used in the template for the list of objects
    template_name = "trainers.html"  # The template file to be rendered
    paginate_by = 15  # Number of items to display per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        qs = super(TrainerList, self).get_queryset(*args, **kwargs)
        return qs
    
class PokemonList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon'  # The name used in the template for the list of objects
    template_name = "pokemon-card.html"  # The template file to be rendered
    paginate_by = 15  # Number of items to display per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'  # The name used in the template for the list of objects
    template_name = "collection.html"  # The template file to be rendered
    paginate_by = 15  # Number of items to display per page