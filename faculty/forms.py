from django import forms

class InventoryFilterForm(forms.Form):
    subcategory = forms.CharField(required=False)
    stream = forms.CharField(required=False)
    sem = forms.CharField(required=False)
    status = forms.CharField(required=False)


class FacultyFilterForm(forms.Form):
    Last_name = forms.CharField(required=False)
    First_name = forms.CharField(required=False)
    Employee_id = forms.CharField(required=False)
    Employee_department = forms.CharField(required=False)



class StudentFilterForm(forms.Form):
    Last_name = forms.CharField(required=False)
    First_name = forms.CharField(required=False)
    Student_id = forms.CharField(required=False)
    Student_course = forms.CharField(required=False)