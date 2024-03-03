from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control mb-3 rounded-0', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-3 rounded-0', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-3 rounded-0', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



class SignUpFormAdmin(UserCreationForm):
    is_superuser = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input mb-3 rounded-0'}))
    is_active = forms.BooleanField(initial=True,required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input mb-3 rounded-0'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'is_superuser', 'is_active' )


    def __init__(self, *args, **kwargs):
        super(SignUpFormAdmin, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '' 

        self.fields['email'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['email'].help_text = '' 
        self.fields['email'].required = False

        self.fields['password1'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].required = False
        
        self.fields['password2'].widget = forms.HiddenInput()
        self.fields['password2'].required = False

        self.fields['is_superuser'].help_text = '<span class="form-text text-muted"><small>Designates that this user has all permissions without explicitly assigning them.</small></span>' 
        self.fields['is_active'].help_text = '<span class="form-text text-muted"><small>Designates whether this user should be treated as active. Unselect this instead of deleting accounts.</small></span>' 

    def clean_username(self):
        return self.cleaned_data.get('username')
    
    def clean_password1(self):
        return self.cleaned_data.get('password1')



class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = 'First name'
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = 'Last name'
        self.fields['last_name'].help_text = '' 

        self.fields['email'].widget.attrs['class'] = 'form-control mb-3 rounded-0'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = 'Email'
        self.fields['email'].help_text = '' 

        self.fields['is_superuser'].help_text = '<span class="form-text text-muted"><small>Designates that this user has all permissions without explicitly assigning them.</small></span>' 
        self.fields['is_active'].help_text = '<span class="form-text text-muted"><small>Designates whether this user should be treated as active. Unselect this instead of deleting accounts.</small></span>' 

        self.fields['password'].widget = forms.HiddenInput()
