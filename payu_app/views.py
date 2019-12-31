from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import  logout
from payu_app.forms import UserDetailsForm, UserInputForm
from payu_app.models import UserInput
from itertools import count
from datetime import datetime
from django.http import HttpResponse
import xlwt
import pandas
from sendfile import sendfile

counter = count(123)

def login(request):
    if request.method == 'POST':
        if request.POST.get("Refno") == None:
            form1 = UserInputForm()
            return render(request, 'index.html', {'form': form1})
        else:
            form = UserDetailsForm(request.POST)
            form1 = UserInputForm()
            if form.is_valid():
                form.save()
                messages.success(request, ("You have been logged in !"))
                return render(request, 'index.html', {'form': form1})
    else:
        form = UserDetailsForm()
        return render(request, 'home.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out !"))
    return redirect('login')

def create_code(request):
    if request.method == 'POST':
        count2 = next(counter)
        form = UserInputForm()
        state_code = request.POST.get('sts')
        sta = state_code[0:2]
        A_Type = request.POST.get('A_Type')
        D_Type = request.POST.get('D_Type')
        created_date = datetime.now()
        print("FFFFF")
        print(created_date)
        print(type(created_date))
        result = f"Code has been created {(sta+A_Type+D_Type+str(count2)).upper()}"
        increment = f"Auto Increment Value Displayed here ( of 3 digits ) {(str(count2))}"
        data = UserInput(state_code=state_code,A_Type=A_Type,D_Type=D_Type,result=(sta+A_Type+D_Type+str(count2)).upper(),created_date=created_date)
        data.save()
        return render(request, 'index.html', {'result': result, 'form':form, 'increment':increment})
    else:
        return render(request, 'index.html', {'cancel':'true'})

def search(request):
    if request.method == 'POST':
        return render(request, 'index.html', {'search':'true'})

def displayResult(request):
    global queryset
    if request.method == 'POST':
        start_date = request.POST.get("start")
        end_date = request.POST.get("end")
        queryset = UserInput.objects.filter(created_date__range=(start_date, end_date))
        return render(request, 'search.html', {'queryset': queryset, 'display':'true'})

def download(request):
    data_dict = queryset.values("state_code","Refno", "A_Type", "D_Type", "result", "created_date")
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"+".csv")
    df = pandas.DataFrame(list(data_dict))
    df.to_csv(filename, encoding='utf-8', index=None)
    return sendfile(request, filename, attachment=True)
