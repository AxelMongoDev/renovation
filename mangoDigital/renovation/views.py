from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template   
from django.http import Http404, JsonResponse 
from django.shortcuts import render, redirect 
from .forms import BussinessContactForm   
from .models import BussinessContact
from django.contrib import messages
from django.conf import settings 
'''
def send_mail(mail):
    context = {'mail': mail}
    template = get_template('renovation.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
    'MANGO DIGITAL COMENTARIO DE:'+ mail.businessName, #Encabezado
    'COMENTARIO:'+ mail.businessComment + '\n' + ' TEL: ' + mail.businessPhone , #Contenido de correo
    settings.EMAIL_HOST_USER, #Correo que envia
    [mail.businessEmail]) #Destinatarios
    email.attach_alternative(content,' text/html ')
    email.send() 
'''

def home_view(request):
    if request.method == 'POST':
        form = BussinessContactForm(request.POST) 
        if (form.is_valid()): 
            form.save()  
            #Impresion en pantalla de los datos registrados y ya guardados en la BD 
            print(form.data['businessName'],form.data['businessComment'],
            form.data['businessPhone'],form.data['businessEmail'])
            return redirect('/')
    else:
        form = BussinessContactForm()
    return render(request,"renovation.html", {'form': form},status=200)

'''
def home_list_view(request,*args, **kwargs):
    """
    REST API VIEW
    consume by javaScript or Ios/Android
    return json data.
    """
    qs = BussinessContact.objects.all()
    contact_list = [{"id":x.id, "businessName":x.businessName} for x in qs]
    data = {
        "isUser": False,
        "response": contact_list
    } 
    return JsonResponse(data)

def home_detail_view(request, blog_id, *args, **kwargs):
    """
    REST API VIEW
    consume by javaScript or Ios/Android
    return json data.
    """
    data = {
        "id": blog_id,
      #  "businessName":obj.businessName,
      #  "businessWeb":obj.businessWeb,
      #  "businessUnit":obj.businessUnit,
      #  "businessDir":obj.businessDir,
      #  "businessPhone":obj.businessPhone
      #  "description":obj.description
    }
    status = 200
    try:
        obj = BussinessContact.objects.get(id=blog_id)
        data['businessName'] = obj.businessName
        print(data)
    except:  #raise Http404
        data['message'] = "Not found"
        status = 404
        print(data)
    return JsonResponse(data, status=status)
    '''