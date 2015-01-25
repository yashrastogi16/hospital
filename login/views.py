from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from models import *
from forms import *
# Create your views here.
def user_login_required(f):
		def wrap(request, *args, **kwargs):
				print "decorater is calling"
				#this check the session if userid key exist, if not it will redirect to login page
				if 'user' not in request.session.keys():
						return HttpResponseRedirect("/")
				return f(request, *args, **kwargs)
		wrap.__doc__=f.__doc__
		wrap.__name__=f.__name__
		return wrap
def base(request):
	return render_to_response('base.html')

def home(request):
	return render_to_response('home.html')

def registerpatient(request):
	return render_to_response('registerpatient.html')

def login(request):
	content = {}
	content['err_msg'] = 'Please Login with your username or password'
	# content['form'] = form
	content.update(csrf(request))
	if 'user' in request.session.keys():
		return HttpResponseRedirect("/home")
	if request.method == "POST":
		username = request.POST['userid']
		password = request.POST['password']
		print username
		user_list = master_admin.objects.filter(userid=username, password=password)
		if(user_list):
			userobj = user_list[0]   
			request.session['user'] = userobj
			sess_ob = request.session['user']
			print userobj.firstname
			content['name'] = sess_ob.firstname
			content['id'] = sess_ob.id
			return render_to_response('managepatient.html', content, context_instance=RequestContext(request))
		else:
			content['err_msg'] = 'Invalid username or password'
		return render_to_response('login.html', content, context_instance=RequestContext(request))
	return render_to_response('login.html', content, context_instance=RequestContext(request))

def adminregister(request):
	content = {}
	form = master_adminForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/admin_login')
	return render_to_response('adminregister.html',locals(),context_instance=RequestContext(request))

def managepatient(request):
	content = {}
	return render_to_response('managepatient.html',content,context_instance=RequestContext(request))

@user_login_required
def logout(request):
	content = {}
	user = request.session['user']
	session_keys = request.session.keys()
	# form = UserForm(request.POST)
	for key in session_keys:
		print "del"
		del request.session[key]
	content['err_msg'] = 'Succesfully Logged Out !!!'
	return render_to_response('login.html', content, context_instance=RequestContext(request))