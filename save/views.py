from django.shortcuts import render
from .models import ProgramSave
# Create your views here.
from .forms import ProgramSaveForm
# Create your views here.
def save(request):

	form=ProgramSaveForm(request.POST or None)
	if request.method == "POST":
		text = request.POST.get("text")
		program_save = ProgramSave()
		program_save.saveprogram = text
		program_save.save()  

		
	context={
	"form" :form,
		}
	return render(request,"save.html",context) 