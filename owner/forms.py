from django import forms
from owner.models import Mobiles
# class MobileForm(forms.Form):
#     mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     colour=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     battery=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     storage=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     ram=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     processor=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         battery=cleaned_data.get("battery")
#         storage=cleaned_data.get("storage")
#         ram=cleaned_data.get("ram")
#         processor=cleaned_data.get("processor")
#         weight=cleaned_data.get("weight")
#         price=cleaned_data.get("price")
#         if price<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if weight < 0:
#             msg = "incorrect weight"
#             self.add_error("weight", msg)
#         if processor < 0:
#             msg = "invalid"
#             self.add_error("processor", msg)
#         if ram < 0:
#             msg = "invalid ram"
#             self.add_error("ram", msg)
#         if storage < 0:
#             msg = "invalid"
#             self.add_error("storage", msg)
#         if battery< 0:
#             msg = "invalid"
#             self.add_error("battery", msg)

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"
        widgets={
           "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "colour":forms.TextInput(attrs={"class":"form-control"}),
            "battery":forms.NumberInput(attrs={"class":"form-control"}),
            "storage":forms.NumberInput(attrs={"class":"form-control"}),
            "ram":forms.NumberInput(attrs={"class":"form-control"}),
            "processor":forms.NumberInput(attrs={"class":"form-control"}),
            "weight":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }