from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import MilanUrl
from .forms import SubmitForm
from django .views import View
from django.http import HttpResponse, HttpResponseRedirect
from analaytics.models import ClickEvent
# Create your views here.
# def milan_redirect_view(request,shortcode=None, *args, **kwargs):
	# print(args)
	# print(kwargs)
	# obj=MilanUrl.objects.get(shortcode=shortcode)
	# return HttpResponse('hello {sc}'.format(sc=obj.url))

	# qs=MilanUrl.objects.filter(shortcode__iexact=shortcode)
	# if qs.exists() and qs.count()==1:
	# 	obj=qs.first()
	# 	obj_url=obj.url
	# return HttpResponse('hello {sc}'.format(sc=obj.url))

	# obj=get_object_or_404(MilanUrl, shortcode=shortcode)
	# obj_url=obj.url
	# return redirect(obj_url)


class UrlRedirectView(View):
	def get(self, request,shortcode=None, *args, **kwargs):
		print('hello')
		obj=get_object_or_404(MilanUrl, shortcode=shortcode)
		print(obj.url)
		ClickEvent.objects.create_event(obj)
		return HttpResponseRedirect(obj.url)

class HomeView(View):
	def get(self, request, *args, **kwargs):
		form=SubmitForm()
		context={
			'title':'Milan.co',
			'form':form,
		}
		return render(request,'shortener/home.html',context)

	def post(self, request, *args, **kwargs):
		form=SubmitForm(request.POST)
		context={
			'title':'Milan.co',
			'form':form,
		}
		if form.is_valid():
			new_url=form.cleaned_data.get('url')
			obj, created =MilanUrl.objects.get_or_create(url=new_url)
			context={
				'object':obj,
				'created':created
			}
			if created:
				return render(request, 'shortener/success.html',context)
			else:
				return render(request, 'shortener/exist.html', context)
		return render(request,'shortener/home.html',context)

