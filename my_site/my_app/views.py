from django.shortcuts import render

# Create your views here.
def example_view(request):
    #my_app/templates/my_app/example.html
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var={
        'first_name':'Jenish',
        'last_name':'Prajapati',
        'some_list':[1,22,3],
        'some_dict':{'inside_key':'inside_value'}
    }
    return render(request,'my_app/variable.html',context=my_var)