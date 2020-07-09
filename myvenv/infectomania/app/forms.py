from django import forms
from .models import Forum


class ForumNew(forms.ModelForm):
			class Meta:
				model=Forum
				fields=['comment' ]
				
