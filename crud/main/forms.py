from .models import Name
from bootstrap_modal_forms.forms import BSModalForm


class NameForm(BSModalForm):
    class Meta:
        model = Name
        fields = ['name', 'hobby', 'category']