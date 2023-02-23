
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, View

from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


# template names in:
# https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """

    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    # def form_valid(self, form):
    #     print('form_valid called')
    #     object = form.save(commit = False)
    #     object.owner = self.request.user
    #     object.save()

    #     return super(OwnerCreateView, self).form_valid(form)

    # https://stackoverflow.com/questions/21652073/django-how-to-set-a-hidden-field-on-a-generic-create-view
    # https://stackoverflow.com/questions/19051830/a-better-way-of-setting-values-in-createview
    # I think this is better:
    def form_valid(self, form):
        print('form_valid called (my version)')

        form.instance.owner = self.request.user

        return super(OwnerCreateView, self).form_valid(form)


# read:
# https://stackoverflow.com/questions/18172102/object-ownership-validation-in-django-updateview
# One can check it, like described in:
# https://stackoverflow.com/questions/28775123/edit-and-replay-xhr-chrome-firefox-etc
# Or in
# https://stackoverflow.com/q/4797534/3790620

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """

        qs = super(OwnerUpdateView, self).get_queryset()
        #qs <- Get the queryset of the model. of the object "pk" was

        return qs.filter(owner = self.request.user)  # 'owner' is from the DB model (Article).



class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        print('delete get_queryset called')

        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner = self.request.user)



# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
