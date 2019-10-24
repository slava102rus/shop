from django import forms
from django.core import validators
from .models import AdvUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from captcha.widgets import ReCaptchaV2Checkbox
from captcha.fields import ReCaptchaField


class LoginForm(forms.Form):
    email1 = forms.EmailField(required=True,label='Ваша почта',validators=[validators.EmailValidator(validators.validate_email)],\
                             widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Введите ваш почтовый адрес'}))
    password1 = forms.CharField(label='Пароль',required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'пароль'}),\
                               validators=[validate_password])
    captcha = ReCaptchaField(label='')
    def clean_email(self):
        email = self.cleaned_data['email1']
        try:
            email = AdvUser.objects.get(email=email)
        except AdvUser.DoesNotExist:
            raise ValidationError('Данный емайл не зарегистрирован')
        return email
    class Meta:
        model = AdvUser
        fields =('email','password',)
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Ваша почта',
                             validators=[validators.EmailValidator(validators.validate_email)], \
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш почтовый адрес'}))
    first_name = forms.CharField(max_length=30,required=True,label='Ваше имя',validators=[validators.RegexValidator(regex='[a-zA-Zа-яА-Я0-9]{3,30}',message="Вы ввели апрещенные символы"),\
                                                                            validators.MinLengthValidator(3,message='Минимальная длина 3 символа'),\
                                                                            validators.MaxLengthValidator(30,message='Максимальная длина 30 символов')],\
                                 widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Введите ваше имя'}))
    last_name = forms.CharField(max_length=30,required=True, label='Ваша фамилия', validators=[validators.RegexValidator(regex='[a-zA-Zа-яА-Я0-9]{3,30}', message="Вы ввели апрещенные символы"), \
                                                                             validators.MinLengthValidator(3, message='Минимальная длина 3 символа'), \
                                                                             validators.MaxLengthValidator(30, message='Максимальная длина 30 символов')], \
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу фамилию'}))
    password = forms.CharField(label='Пароль', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль'}),validators=[validate_password])
    password2 = forms.CharField(label='Повторите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}), \
                                validators=[validate_password])
    captcha = ReCaptchaField(label='')
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
           raise ValidationError('Пароли не совпадают')
        return cleaned_data


    class Meta:
        model = AdvUser
        fields=('email','first_name','last_name','password','password2')

