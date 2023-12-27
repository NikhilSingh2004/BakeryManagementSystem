from BakeryMSys.settings import BASE_DIR
from django.shortcuts import render,redirect
from core.models import Order, User
from core.forms import AddOrder, UpdateOrder, FindOrder, LogIn
import datetime

def logIn(request):

    log = LogIn()

    if request.method == "POST":
        try:

            logData = LogIn(request.POST)

            if logData.is_valid():
                
                if logData.cleaned_data['email']:
                    email = logData.cleaned_data['email']
                
                if logData.cleaned_data['password']:
                    password = logData.cleaned_data['password']

                    user = User.objects.filter(email = email, password = password)
            
                    if user:
                        return redirect('home')
                
                    return render(request, 'core/LogIn.html', {'logForm' : log, 'ErrorMessage' : 'User Not Found!'})

                return render(request, 'core/LogIn.html', {'logForm' : log, 'ErrorMessage' : 'Please Enter All Data!'})
            
            return render(request, 'core/LogIn.html', {'logForm' : log, 'ErrorMessage' : 'Invalid Data!'})

        except Exception as e :
            print(e.__str__())
            return render(request, 'core/LogIn.html', {'logForm' : log, 'ErrorMessage' : ''})
    else:
        return render(request, 'core/LogIn.html', {'logForm' : log, 'ErrorMessage' : ''})

def home(request):

    aOrder = AddOrder()
    updateOrder = UpdateOrder()
    findOrder = FindOrder()

    orders = Order.objects.all()

    return render(request, 'core/index.html', {'orders': orders, 'status': True, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})

def addOrder(request):

    orders = Order.objects.all()

    aOrder = AddOrder()
    updateOrder = UpdateOrder()
    findOrder = FindOrder()

    if(request.method == "POST"):
        try:

            addOrder = AddOrder(request.POST)

            if  addOrder.is_valid():
                
                cust_name = addOrder.cleaned_data['customer_name']
                order_name = addOrder.cleaned_data['order_name']
                order_date = datetime.datetime.now()
                order_quant = addOrder.cleaned_data['order_quantity']

                new_order = Order.objects.create(
                    customer_name= cust_name,
                    order_name = order_name,
                    order_date = order_date,
                    order_quantity = order_quant
                )

                new_order.save()

                return render(request, 'core/index.html' , {'status' : True, 'added' : True, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder}) 
        
            return render(request, 'core/index.html' , {'status' : False, 'added' : False, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder}) 
        
        except Exception as e :
            print(e.__str__())

            return render(request, 'core/index.html', {'status' : False, 'orders': orders,  'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})
    else:
        return render(request, 'core/index.html', {'status': False, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})

def findOrder(request):

    aOrder = AddOrder()
    updateOrder = UpdateOrder()
    findOrder = FindOrder()

    if(request.method == "POST"):
        try:

            fOrder = FindOrder(request.POST)
            
            if fOrder.is_valid():
                id = int(fOrder.cleaned_data['order_id'])

                orders = Order.objects.filter(id=id)

                if(orders):
                    return render(request, 'core/index.html', {'orders' : orders, 'status' : True, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})
                
                return render(request, 'core/index.html', {'orders' : orders, 'status' : False, 'notFound' : True, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})
            
            return render(request, 'core/index.html', {'orders' : orders, 'status' : False, 'notFound' : True, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})

        except Exception as e :
            print(e.__str__())

            return render(request, 'core/index.html', {'orders' : orders, 'status' : False, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})
    else:
        return render(request, 'core/index.html', {'orders' : orders, 'status': False, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})

def updateOrder(request):
            
    orders = Order.objects.all()

    aOrder = AddOrder()
    updateOrder = UpdateOrder()
    findOrder = FindOrder()

    if(request.method == "POST"):
        try:

            uOrder = UpdateOrder(request.POST)

            if uOrder.is_valid():
                id = int(uOrder.cleaned_data['order_id'])

                order = Order.objects.get(id=id)

                if order:

                    if(uOrder.cleaned_data['customer_name']):
                        order.customer_name = uOrder.cleaned_data['customer_name']

                    if(uOrder.cleaned_data['order_name']):
                        order.order_name = uOrder.cleaned_data['order_name']
                        
                    if(uOrder.cleaned_data['order_quantity']):
                        order.order_quantity = uOrder.cleaned_data['order_quantity']

                    order.save()

                    return render(request, 'core/index.html', {'update' : True, 'status': True, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})
                
                return render(request, 'core/index.html', {'update' : False, 'orders': orders, 'status': False, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})

            return render(request, 'core/index.html', {'update' : False, 'orders': orders, 'status': False, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})    
            
        except Exception as e :
            print(e.__str__())

            return render(request, 'core/index.html', {'status' : False, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})
    else:
        return render(request, 'core/index.html', {'status': False, 'orders': orders, 'addForm' : aOrder, 'updateForm' : updateOrder, 'findForm' : findOrder})

def AdminRedirect(request):
    return redirect(BASE_DIR+'admin/')
