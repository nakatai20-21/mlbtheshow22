from dataclasses import field
from datetime import date, datetime
from email import message
from mimetypes import init
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.test import tag
from matplotlib import widgets
from .models import Information, Member

from .input_param import mph, plate_appearance, hand, ball_type, result


#forms.Formだと通らない　forms.ModelFormだと通る
#前者の場合はモデルを使わず、後者の場合はモデルを使う
class InputForm(forms.ModelForm):

    class Meta():
        model = Information

        fields = ("season","first_runner","second_runner","third_runner","plate_appearance","hand","ball_type","mph","result")
        labels = {
            "season":"season",
            "plate_appearance":"plate_appearance",
            "first_runner":"first_runner",
            "second_runner":"second_runner",
            "third_runner":"third_runner",
            "hand":"hand",
            "ball_type":"ball_type",
            "mph":"mph",
            "result":"result"
        }
        """widgets = {
            "date":AdminDateWidget(),
        }"""

class MemberForm(forms.ModelForm):
    class Meta():
        model = Member
        fields = ("first_name","last_name","address","age","mail")
        labels = {"first_name":"fname", "last_name":"fname","address":"add","age":"age","mail":"mail"}

class MF(forms.Form):
    taichi = forms.CharField(label='namae')