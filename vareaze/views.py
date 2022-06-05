from django.shortcuts import render, redirect
from .models import Contract
from account.models import Account
from .forms import ContractForm


# Create your views here.
def home(request):
	"""The home page"""
	user = request.user
	accounts = Account.objects.all()
	context = {'accounts':accounts, 'user':user}
	return render(request, 'vareaze/home.html', context)

def initiate(request, user_id):
	"""List user contracts"""
	contracts = Contract.objects.all()
	user_vareaze_id = request.user.vareaze_id
	account_list = Account.objects.all()
	owner = Account.objects.get(id=user_id)
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ContractForm()
	else:
		print(request.POST)
		form = ContractForm(data=request.POST)
		if form.is_valid():
			if request.POST.get('vareaze_id') == user_vareaze_id:
				contract = form.save(commit=False)
				print(contract)
				contract.owner = owner
				print(contract.owner)
				contract.save()
				print(contract)
				return redirect('vareaze:home')
			else:
				return "Invalid Pin"
		else:
			return redirect('vareaze:initiate', user_id)
	context = {'contracts':contracts, 'owner':owner, 'form':form, 'account_list':account_list}
	return render(request, 'vareaze/contract.html', context)

def profile(request, user_id):
	user = Account.objects.get(id=user_id)
	context = {'user':user}
	return render(request, 'vareaze/profile.html', context)