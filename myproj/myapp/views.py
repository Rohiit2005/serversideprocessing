from django.shortcuts import render
from django.template import loader
def triarea(request):
    context={}
    context['area']="0"
    context['h']="0"
    context['b']="0"
    if request.method == 'POST':
        print("POST method is used")
        h = request.POST.get('height','0')
        b = request.POST.get('base','0')
        print('request=',request)
        print('height=',h)
        print('base=',b)
        area = 0.5 * int(h) * int(b)
        context['area'] = area
        context['h'] = h
        context['b'] = b
        print('area=',area)
    return render(request,'myapp/math.html',context)    
