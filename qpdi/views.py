from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
import psycopg2
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
from io import BytesIO
import requests
from io import BytesIO
from PIL import Image
import tempfile
import os
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')

#@login_required
def plataforma(request):
    return render(request, 'plataforma.html')
