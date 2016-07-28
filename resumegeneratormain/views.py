from django.shortcuts import render

from django.contrib.auth.models import User
from weasyprint import HTML, CSS

from django.template import loader

from django.http import HttpResponse

def form(request):
	return render(request, "RGhomepage.html")

def resume(request):
	data = {"user": User.objects.get(username="11438029_richardlancegparayno")}
	return render(request, "BlankResume.html", data)

def resumePdf(request):
	template = loader.get_template("BlankResume.html")
	data = {"user": User.objects.get(username="11438029_richardlancegparayno")}
	html = template.render(data)
	css = CSS(filename='resumegeneratormain/static/resumegeneratormain/css/blank-resume.css')
	pdf = HTML(string=html,base_url='/Users/Admin/dlsuresumegenerator').write_pdf(stylesheets=[css])
	return HttpResponse(pdf, content_type='application/pdf')
