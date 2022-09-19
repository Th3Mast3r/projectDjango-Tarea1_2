from django.shortcuts import render #backend renderizar lo que va a pasar de la base de datos(parte vital : proyecta tolo lo que hemos hecho), la parte de url, el index (que recibe y que hace)
from django.contrib import messages #aca va a mostrar los datos solicitados que se piden a travez de django
from django.views import generic #importa el generico = forma en que se muestra lo importado
from .forms import BlogForm, ReviewForm,ContactForm,CreateUserForm #, ReviewForm, BlogForm #el conector de backend y frontend (forms)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import ( #importamos todos los datos desde las tablas
	Blog,
	Review,
	)

def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main:login')

#hacemos las clases para las vistas
class IndexView(generic.TemplateView):
	template_name = "main/index.html" #asignando la vista

	def get_context_data(self, **kwargs): #funcion q va a obtener la data
		#declaramos las variables donde se va a gaurdar la info
		context = super().get_context_data(**kwargs) #context guardara la informacion de testimonial, certificate, etc.
		blogs = Blog.objects.filter(is_active=True)
		reviews = Review.objects.filter(is_active=True)

		context["blogs"] = blogs
		context["reviews"] = reviews
		return context #regresamos la info

class BlogView(generic.ListView): #aca se suben las noticia (blog), aca se ven 10 lineas
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10 #para q no se sature, mostrara solo 10 lineas... (no toda la info x si es larga)
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True) #retorno de info apenas encuentre todo

class BlogDetailView(generic.DetailView): #aca se encuentra todo (detalles) (despues de clickear la blogview)
	model = Blog
	template_name = "main/blog-detail.html"

class ContactView(generic.FormView):
	template_name = "main/contact.html" #asigno la vista que html recibe
	form_class = ContactForm #creado para recibir info
	success_url = "/" #envia al index apenas de se clic
	
	def form_valid(self, form): 
		form.save()	#guarda info en base de datos
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form) 

class BlogAddInfo(generic.FormView):
	template_name = "main/blog-create.html" #asigno la vista que html recibe
	form_class = BlogForm #creado para recibir info
	success_url = "/" #envia al index apenas de se clic
	
	def form_valid(self, form): 
		form.save()	#guarda info en base de datos
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form) 

class ReviewView(generic.ListView): #aca se suben las noticia (blog), aca se ven 10 lineas
	model = Review
	template_name = "main/review.html"
	paginate_by = 10 #para q no se sature, mostrara solo 10 lineas... (no toda la info x si es larga)
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True) #retorno de info apenas encuentre todo

class ReviewDetailView(generic.DetailView): #aca se encuentra todo (detalles) (despues de clickear la blogview)
	model = Review
	template_name = "main/review-detail.html"

class ReviewAddInfo(generic.FormView):
	template_name = "main/review-create.html" #asigno la vista que html recibe
	form_class = ReviewForm #creado para recibir info
	success_url = "/" #envia al index apenas de se clic
	
	def form_valid(self, form): 
		form.save()	#guarda info en base de datos
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form) 