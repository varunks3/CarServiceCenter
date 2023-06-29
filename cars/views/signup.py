from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from ..models import User
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        user = User (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateUser (user)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            user.password = make_password (user.password)
            user.register ()
            return redirect ('/')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateUser(self, user):
        error_message = None
        if (not user.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (user.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not user.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (user.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not user.phone:
            error_message = 'Enter your Phone Number'
        elif len (user.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (user.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif user.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.models import User, auth

# # Create your views here.
# def home(request):
#     return render(request,'home/index.html')

# def aboutUs(request):
#     return render(request,'home/About Us.html')

# def contact(request):
#     return render(request,'home/Contact.html')


# def signup(request):
#     if request.method == 'POST':
#         fName = request.POST['fname']
#         lName = request.POST['lname']
#         userName = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(username = userName, password = password, email = email, first_name = fName, last_name = lName)
#         print('account created')
#         return redirect('/login')
#     else:
#         return render(request,'home/signup.html')



# # def index(request):
# #     if request.method == 'POST':
        
# #     return HttpResponse('Hey, there')


# def login(request):
#     if request.method == 'POST':
#         userName = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username = userName, password = password)

#         if user is not None:
#             auth.login(request, user)
#             print('Logged in')
#             return redirect('/')
#     else:
#         return render(request,'home/login.html')