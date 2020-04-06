from django.shortcuts import render
import requests
# from requests_ntlm import HttpNtlmAuth

# Create your views here.

def home(request):
    url = 'http://desktop-cmq34np/gt_qlik/qrs/app/full?xrfkey=123456789ABCDEFG'
    headers = {
        'hdr-usr' : 'DESKTOP-CMQ34NP\\user',
        'X-Qlik-xrfkey' : '123456789ABCDEFG',
        "Content-Type": "application/json",
    }
    resp = requests.get(url,headers=headers)    
    return render(request, 'index.html',{'resp':resp})
