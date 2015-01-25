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
			list1 = patient.objects.all()
			content = {'lists' : list1}
			return render_to_response('patientrecord.html', content, context_instance=RequestContext(request))
		else:
			content['err_msg'] = 'Invalid username or password'
		return render_to_response('login.html', content, context_instance=RequestContext(request))
	return render_to_response('login.html', content, context_instance=RequestContext(request))

@user_login_required
def logout(request):
	content = {}
	user = request.session['user']
	session_keys = request.session.keys()
	for key in session_keys:
		print "del"
		del request.session[key]
	return render_to_response('home.html', content, context_instance=RequestContext(request))

def adminregister(request):
	content = {}
	form = master_adminForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/admin_login')
	return render_to_response('adminregister.html',locals(),context_instance=RequestContext(request))
@user_login_required
def patientrecord(request):
	content = {}
	list1 = patient.objects.all()
	content = {'lists' : list1}
	return render_to_response('patientrecord.html',content,context_instance=RequestContext(request))
	
def registerpatient(request):
	content = {}
	abc = doctor.objects.all()
	content = {'doctor1': abc}
	if request.method == 'POST':
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		age = request.POST.get('age')
		mobile = request.POST.get('mobile')
		date = request.POST.get('date')
		email = request.POST.get('email')
		city = request.POST.get('city')
		doctor1 = request.POST.get('doctor1')
		try:
			print doctor1
			doc = doctor.objects.get(doctorname=doctor1)
			print type(doc)
			patientregister = patient.objects.create(firstname=firstname,lastname=lastname,age=age,mobile=mobile,date=date,email=email,city=city,doctor=doc)
			msg = "Registered successfully"
			return render_to_response('home.html',content,context_instance=RequestContext(request)) 
		except Exception as e:
			print e
			msg = "Registration Failed"
			content['err_msg'] = msg
			return render_to_response('registerpatient.html',content,context_instance=RequestContext(request))
	return render_to_response('registerpatient.html',content,context_instance=RequestContext(request))
