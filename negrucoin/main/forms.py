from django import forms

from django.contrib.auth import get_user_model

from negrucoin.settings import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH

User = get_user_model()

LOGIN_ERROR_MESSAGE = 'Неверный логин или пароль'


class LoginForm(forms.ModelForm):
    """Login form, used in login view to validate user data."""

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self) -> None:
        """Clean data."""
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(LOGIN_ERROR_MESSAGE)

        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError(LOGIN_ERROR_MESSAGE)

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
    """Registration form, used in registration view."""

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'

    def clean_username(self) -> None:
        """Clean only username.
        We have to check uniqueness of username.
        """
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Логин "{username}" занят')
        return username

    def clean(self) -> None:
        """Clean data.

        Checks password strength with following rules:
        - must have from 8 to 255 chars
        - must have number
        - must have letter
        - must have uppercase letter
        """

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')

        if not MIN_PASSWORD_LENGTH < len(password) < MAX_PASSWORD_LENGTH:
            raise forms.ValidationError(
                f'Длина пароля должна быть от {MIN_PASSWORD_LENGTH}'
                f' до {MAX_PASSWORD_LENGTH} символов'
            )

        if all(map(str.isdigit, password)):
            raise forms.ValidationError('Пароль должен содержать хотябы одну букву')

        if not any(map(str.isdigit, password)):
            # Password are not contain digits
            raise forms.ValidationError('Пароль должен содержать хотябы одно число')

        if not any(map(str.isupper, password)):
            raise forms.ValidationError('Пароль должен содержать хотябы одну заглавную букву')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
