from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, TemplateView
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 
from django.urls import reverse
from django.shortcuts import redirect

from .models import UserFollow
from .forms import UserFollowForm


"""
Definition of views classes for the followup.
"""

class UserFollowView(LoginRequiredMixin, CreateView):
    """View for the UserFollows List ."""
    model = UserFollow
    template_name = "followup/userfollow.html"    
    fields = ["followed_user", ]

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("follow:follow")

    def get_context_data(self, **kwargs):
        """Affiche les utilisateurs suivis par l'utilisateur actuel."""
        context=  super().get_context_data(**kwargs)        
        # Récupérer les utilisateurs que vous suivez        
        followed_users = UserFollow.objects.filter(user=self.request.user).exclude(followed_user=self.request.user)        
        # Récupérer les utilisateurs qui vous suivent
        users_following = UserFollow.objects.filter(followed_user=self.request.user).exclude(user=self.request.user)         

        context.update(
            {
            # "form": form,
            "followed_users": followed_users,
            "users_following": users_following,
            }
                    )
        return context
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        if form.instance.followed_user == form.instance.user:
            messages.error(self.request, "Vous ne pouvez pas vous suivre vous-même.")
            return self.form_invalid(form)
        if UserFollow.objects.filter(user=form.instance.user, followed_user=form.instance.followed_user).exists():
            messages.error(self.request, f"Vous suivez déjà {form.instance.followed_user}.")
            return self.form_invalid(form)
        return super().form_valid(form)


class UserUnfollowView(LoginRequiredMixin, DeleteView):
    """Permet à un utilisateur de ne plus suivre un autre utilisateur."""

    model = UserFollow
    template_name = "followup/userunfollow.html"    

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("follow:follow")
  











# from django.shortcuts import render, redirect
# from django.views.generic import (ListView, DetailView, CreateView,
#                                   UpdateView, DeleteView, TemplateView
#                                   )
# from django.urls import reverse_lazy, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import TicketForm, ReviewForm, TicketCreateForm, ReviewCreateForm
# from .models import Ticket, Review

# """
# Definition of views classes for the flux.
# """
# class TicketIndexView(LoginRequiredMixin, ListView):
#     """View for the ticket index page."""
#     model = Ticket
#     template_name = "blogpost/ticket_index.html"
#     context_object_name = "tickets"


# class TikectDetailView(LoginRequiredMixin, DetailView):
#     """View for the ticket detail page."""
#     model = Ticket
#     template_name = "blogpost/ticket_detail.html"
#     context_object_name = "ticket"


# class TicketCreateView(LoginRequiredMixin, CreateView):
#     """View for the creation of a ticket."""
#     model = Ticket
#     template_name = "blogpost/ticket_create.html"
#     form_class = TicketForm

#     def get_initial(self):
#         """Return the initial data to use for forms on this view."""
#         initial = super().get_initial()
#         initial.update({
#         "title": "Entrez le titre ici",
#         "user": self.request.user,    
#         "description": "Entrez la description ici",  
#                 })
#         return initial
    
#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("flux:ticket-detail", kwargs={"slug": self.object.slug})
                     
    
#     def form_valid(self, form):
#         """If the form is valid, save the associated model."""        
#         form.instance.user = self.request.user
#         return super().form_valid(form)
 
        
# class TicketUpdateView(LoginRequiredMixin, UpdateView):
#     """View for the update of a ticket."""
#     model = Ticket
#     template_name = "blogpost/ticket_update.html"
#     form_class = TicketForm   
    
#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("flux:ticket-detail", kwargs={"slug": self.object.slug})
   

# class TicketDeleteView(LoginRequiredMixin, DeleteView):
#     """View for the deletion of a ticket."""
#     model = Ticket
#     template_name = "blogpost/ticket_delete.html"    

#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("flux:ticket-index")


# class ReviewIndexView(LoginRequiredMixin, ListView):
#     """View for the review index page."""    
#     template_name = "blogpost/review_index.html"
#     context_object_name = "reviews"

#     def get_context_data(self, **kwargs):
#         """Return the context data to use for forms on this view."""        
#         context = super().get_context_data(**kwargs)
#         context.update({"ticket": Ticket.objects.get(slug=self.kwargs["ticket_slug"])})        
#         # kwargs["ticket"] = Ticket.objects.get(slug=self.kwargs["ticket_slug"])      
#         # return super().get_context_data(**kwargs) 
#         return context
    
#     def get_queryset(self):
#         """Return the list of items for this view."""        
#         return Review.objects.filter(ticket__slug=self.kwargs["ticket_slug"])      


# class ReviewDetailView(LoginRequiredMixin, DetailView):
#     """View for the review detail page."""
#     model = Review
#     template_name = "blogpost/review_detail.html"
#     context_object_name = "review"
#     # slug_url_kwarg = "review_slug"
#     # pk_url_kwarg = "review_slug"
    

# class ReviewCreateView(LoginRequiredMixin, CreateView):
#     """View for the creation of a review."""
#     model = Review
#     template_name = "blogpost/review_create.html"
#     form_class = ReviewForm

#     def get_initial(self):
#         """Return the initial data to use for forms on this view."""
#         initial = super().get_initial()
#         initial.update({
#             "headline": "Entrez le titre ici",
#             "ticket": Ticket.objects.get(slug=self.kwargs["ticket_slug"]),
#             "user": self.request.user,
#             "body": "Entrez le commentaire ici",
#             "rating": 0,
#         })
#         return initial
#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("flux:ticket-review-detail", kwargs={"ticket_slug": self.object.ticket.slug, "slug": self.object.slug})

#     def get_context_data(self, **kwargs):
#         """Return the context data to use for forms on this view.""" 
#         context = super().get_context_data(**kwargs)
#         context.update({"ticket": Ticket.objects.get(slug=self.kwargs["ticket_slug"])})       
#         return context
    
#     def form_valid(self, form):
#         """If the form is valid, save the associated model."""
#         form.instance.user = self.request.user
#         form.instance.ticket = Ticket.objects.get(slug=self.kwargs["ticket_slug"])
#         # print(type(form.instance)) # form.instance est une instance du modèle Review
#         return super().form_valid(form)


# class ReviewUpdateView(LoginRequiredMixin, UpdateView):
#     """View for the update of a review."""
#     model = Review
#     template_name="blogpost/review_update.html"
#     form_class = ReviewForm

#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("flux:ticket-review-detail", kwargs={"ticket_slug": self.object.ticket.slug, "slug": self.object.slug})

    
# class ReviewDeleteView(LoginRequiredMixin, DeleteView):
#     """View for the deletion of a review."""
#     model = Review
#     template_name = "blogpost/review_delete.html"
    
    
#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("flux:ticket-review-index", kwargs={"ticket_slug": self.object.ticket.slug})


# class TicketReviewAllInOneView(LoginRequiredMixin, TemplateView):
#     """View for the creation of a review and ticket all in one."""
#     template_name = "blogpost/ticket_review_create_aio.html"

#     def get_context_data(self, **kwargs):
#         """Return the context data to use for forms on this view."""
#         context = super().get_context_data(**kwargs)
#         context.update({"form_ticket": TicketCreateForm(), "form_review": ReviewCreateForm()})
#         return context

#     def post(self, request, *args, **kwargs):
#         """Handle POST requests: create a ticket and a review."""
#         form_ticket = TicketCreateForm(request.POST, request.FILES)
#         form_review = ReviewCreateForm(request.POST)
#         if not form_ticket.is_valid() and not form_review.is_valid():
#             context = {"form_ticket": form_ticket, "form_review": form_review}
#             return self.render_to_response(context)
#         form_ticket.instance.user = self.request.user
#         ticket = form_ticket.save()
#         form_review.instance.user = self.request.user
#         form_review.instance.ticket = ticket
#         form_review.save()
#         return redirect(reverse("flux:ticket-index"))
    
#     # def get_success_url(self):
#     #     """Return the URL to redirect to after processing a valid form."""
#     #     return reverse("flux:ticket-detail", kwargs={"slug": self.ticket.slug})


# # class ReviewAIO(TemplateView):

# #     template_name = 'ma_page.html'

# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['form_ticket'] = TicketCreateForm()
# #         context['form_review'] = ReviewCreateForm()
# #         return context

# #     def post(self, request, *args, **kwargs):
# #         form_ticket = TicketCreateForm(request.POST, request.FILES)
# #         form_review = ReviewCreateForm(request.POST)
# #         if not form_ticket.is_valid() and not form_review.is_valid():
# #             context = {
# #                 'form_ticket': form_ticket,
# #                 'form_review': form_review
# #             }
# #             return self.render_to_response(context)
# #         # si tout va bien, créer le ticket et la review
# #         form_ticket.user = self.request.user
# #         ticket = form_ticket.save()
# #         # Continue...
# #         form_review.user = self.request.user
# #         form_review.ticket = ticket
# #         form_review.save()
        

# #         return redirect(reverse('flow'))





# # def review_by_0_view(request):
# #     """    View for the creation of review by zero page.
# #     """
# #     if request.method == "POST":    
# #         form = TicketForm(request.POST)
# #         form_1 = ReviewForm(request.POST)        
# #         if form.is_valid() and form_1.is_valid():
# #             form.save()
# #             form_1.save()
# #         return redirect(request.path)
# #     else:
# #         init_values = {
# #             "user": request.user if request.user.is_authenticated else None,            
# #         }            
# #         form = TicketForm(initial=init_values)
# #         form_1 = ReviewForm(initial=init_values)
# #     return render(request, "blogpost/review_by_0.html", {"form": form, "form_1": form_1})
