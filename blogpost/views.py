from django.shortcuts import redirect, render
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, TemplateView
                                  )
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TicketForm, ReviewForm, TicketCreateForm, ReviewCreateForm
from .models import Ticket, Review

"""
Definition of views classes for the flux.
"""


class TicketlistView(LoginRequiredMixin, ListView):
    """View for the ticket list page."""
    model = Ticket
    template_name = "blogpost/ticket_list.html"
    context_object_name = "tickets"


class TikectDetailView(LoginRequiredMixin, DetailView):
    """View for the ticket detail page."""
    model = Ticket
    template_name = "blogpost/ticket_detail.html"
    context_object_name = "ticket"


class TicketCreateView(LoginRequiredMixin, CreateView):
    """View for the creation of a ticket."""
    model = Ticket
    template_name = "blogpost/ticket_create.html"
    form_class = TicketForm

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        # print(self.object)   # self.object est une instance du modèle Ticket
        # print(type(self.object))  # self.object est une instance de <class 'blogpost.models.Ticket'>
        return reverse("flux:ticket-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        """
        Avant que le formulaire ne soit validé et que l'instance de modèle ne
        soit sauvegardée, l'attribut user de l'instance est défini sur
        l'utilisateur actuellement connecté (self.request.user). Cela permet
        de lier l'instance de modèle à l'utilisateur qui a soumis le formulaire.
        """
        form.instance.user = self.request.user  # form.instance est une instance du modèle Ticket
        # form.save().user = self.request.user    # form.save() est également une instance du modèle Ticket
        # print(type(form.instance)) # form.instance est une instance de <class 'blogpost.models.Ticket'>
        # print(form.instance)
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    """View for the update of a ticket."""
    model = Ticket
    template_name = "blogpost/ticket_update.html"
    form_class = TicketForm

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("flux:ticket-detail", kwargs={"slug": self.object.slug})


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    """View for the deletion of a ticket."""
    model = Ticket
    template_name = "blogpost/ticket_delete.html"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("flux:ticket-list")


class ReviewlistView(LoginRequiredMixin, ListView):
    """View for the review list page."""
    template_name = "blogpost/review_list.html"
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        """Return the context data to use for forms on this view."""
        context = super().get_context_data(**kwargs)
        context.update({"ticket": Ticket.objects.get(slug=self.kwargs["ticket_slug"])})
        return context

    def get_queryset(self):
        """Return the list of items for this view."""
        return Review.objects.filter(ticket__slug=self.kwargs["ticket_slug"])


class ReviewDetailView(LoginRequiredMixin, DetailView):
    """View for the review detail page."""
    model = Review
    template_name = "blogpost/review_detail.html"
    context_object_name = "review"
    # slug_url_kwarg = "review_slug"
    # pk_url_kwarg = "review_id"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """View for the creation of a review."""
    model = Review
    template_name = "blogpost/review_create.html"
    form_class = ReviewForm

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("flux:ticket-review-detail", kwargs={"ticket_slug": self.object.ticket.slug, "slug": self.object.slug})

    def get_context_data(self, **kwargs):
        """Return the context data to use for forms on this view."""
        context = super().get_context_data(**kwargs)
        context.update({"ticket": Ticket.objects.get(slug=self.kwargs["ticket_slug"])})
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        form.instance.ticket = Ticket.objects.get(slug=self.kwargs["ticket_slug"])
        # print(type(form.instance)) # form.instance est une instance du modèle Review
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """View for the update of a review."""
    model = Review
    template_name = "blogpost/review_update.html"
    form_class = ReviewForm

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("flux:ticket-review-detail", kwargs={"ticket_slug": self.object.ticket.slug, "slug": self.object.slug})


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """View for the deletion of a review."""
    model = Review
    template_name = "blogpost/review_delete.html"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("flux:ticket-review-list", kwargs={"ticket_slug": self.object.ticket.slug})


# Avec la classe CreateView
class TicketReviewCreateAIOView(LoginRequiredMixin, CreateView):
    """View for the creation of a review and ticket all in one."""
    model = Ticket
    template_name = "blogpost/ticket_review_create_aio.html"
    form_class = TicketForm

    def get_context_data(self, **kwargs):
        """Return the context data to use for forms on this view."""
        context = super().get_context_data(**kwargs)
        context.update({"form_review": ReviewForm()})
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        ticket = form.save()
        form_review = ReviewForm(self.request.POST)
        form_review.instance.user = self.request.user
        form_review.instance.ticket = ticket
        form_review.save()
        return redirect(reverse("flux:ticket-list"))


# Avec la classe TemplateView
class TicketReviewCreateAIOView1(LoginRequiredMixin, TemplateView):
    """View for the creation of a review and ticket all in one."""
    template_name = "blogpost/ticket_review_create_aio.html"

    def get_context_data(self, **kwargs):
        """Return the context data to use for forms on this view."""
        context = super().get_context_data(**kwargs)
        context.update({"form_ticket": TicketForm(), "form_review": ReviewForm()})
        return context

    def post(self, request, *args, **kwargs):
        """Handle POST requests: create a ticket and a review."""
        form_ticket = TicketCreateForm(request.POST, request.FILES)
        form_review = ReviewCreateForm(request.POST)
        if not form_ticket.is_valid() and not form_review.is_valid():
            context = {"form_ticket": form_ticket,
                       "form_review": form_review
                       }
            return self.render_to_response(context)
        # si tout va bien, créer le ticket et la review)
        form_ticket.instance.user = self.request.user
        ticket = form_ticket.save()
        form_review.instance.user = self.request.user
        form_review.instance.ticket = ticket
        form_review.save()
        return redirect(reverse("flux:ticket-list"))


# Avec les Vues basées sur les fonctions
def ticket_review_all_in_one_view(request):
    """    View for the creation of review by zero page.
    """
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        form_1 = ReviewForm(request.POST)
        if form.is_valid() and form_1.is_valid():
            form.save()
            form_1.save()
        return redirect(request.path)
    else:

        form = TicketForm()
        form_1 = ReviewForm()
    return render(request, "blogpost/review_by_0.html", {"form": form, "form_1": form_1})