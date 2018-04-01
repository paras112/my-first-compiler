from django import forms

from .models import ProgramSave

class ProgramSaveForm(forms.ModelForm):
	class Meta:
		model=ProgramSave
		fields={
		"saveprogram"
		}

	def saveprogramclean(self):
		saveprogram=self.cleaned_data.get('saveprogram')
		return saveprogram
