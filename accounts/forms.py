from django.contrib.auth.forms import UserCreationForm

# customized user creation form
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            # remove extraneous help text
            self.fields[fieldname].help_text = None
            # set form to use bootstrap class
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})