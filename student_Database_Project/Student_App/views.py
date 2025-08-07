from django.shortcuts import render

# Create your views here.
# students/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'student_App/home.html')
from django.shortcuts import render

def signup_select(request):
    return render(request, 'Student_App/signup_select.html')

def signup_student(request):
    return render(request, 'Student_App/signup_student.html')  # Placeholder for now

def signup_teacher(request):
    return render(request, 'Student_App/signup_teacher.html')  # Placeholder for now


from django.shortcuts import render, redirect
from .forms import TeacherSignUpForm
from .models import Teacher
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def signup_teacher(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.password = make_password(form.cleaned_data['password'])
            teacher.save()
            return render(request, 'Student_App/welcome.html', {
                'user_type': 'Teacher',
                'name': teacher.first_name
            })
            messages.success(request, "Teacher account created successfully!")
            return redirect('signup-select')
    else:
        form = TeacherSignUpForm()

    return render(request, 'Student_App/signup_teacher.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import StudentSignUpForm


def signup_student(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            return render(request, 'Student_App/welcome.html', {
                'user_type': 'Student',
                'name': student.first_name
            })
            messages.success(request, "Student account created successfully!")
            return redirect('welcome')  # Or wherever you want
    else:
        form = StudentSignUpForm()

    return render(request, 'Student_App/signup_student.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import StudentLoginForm
from .models import Student

def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email)
                if check_password(password, student.password):
                    return render(request, 'Student_App/welcome.html', {
                        'user_type': 'Student',
                        'name': student.first_name
                    })
                else:
                    messages.error(request, "Incorrect password.")
            except Student.DoesNotExist:
                messages.error(request, "Student with this email does not exist.")
    else:
        form = StudentLoginForm()

    return render(request, 'Student_App/login_student.html', {'form': form})



from django.contrib.auth.hashers import check_password
from .models import Teacher
from .forms import TeacherLoginForm

def login_teacher(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            try:
                teacher = Teacher.objects.get(email=email, phone=phone)
                if check_password(password, teacher.password):
                    return render(request, 'Student_App/welcome.html', {
                        'user_type': 'Teacher',
                        'name': teacher.first_name
                    })
                else:
                    messages.error(request, "Incorrect password.")
            except Teacher.DoesNotExist:
                messages.error(request, "Teacher with this email and phone number does not exist.")
    else:
        form = TeacherLoginForm()

    return render(request, 'Student_App/login_teacher.html', {'form': form})



from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin-dashboard')    # Ensure this path exists
        else:
            messages.error(request, 'Invalid credentials or not an admin user.')

    return render(request, 'Student_App/admin_login.html')


from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    return render(request, 'Student_App/admin_dashboard.html')
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirects to home page after logout
