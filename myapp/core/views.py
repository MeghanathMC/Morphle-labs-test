from django.shortcuts import render

# Create your views here.
import os
import pwd
import subprocess
from datetime import datetime
import pytz
from django.http import HttpResponse

def htop(request):
  
    try:
        username = os.getlogin()
    except OSError:
        username = pwd.getpwuid(os.getuid())[0]

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

   
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

   
    html = f"""
    <h1>System Information</h1>
    <p><b>Name:</b> Meghanath Reddy M C</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html)
