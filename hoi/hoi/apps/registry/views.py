from django.db.models import Count
from apps.registry.models import Persona, Report
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from cgi import escape
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings
import os

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    print path
    return path


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request, pk):
    p = Persona.objects.get(pk=pk)
    return render_to_pdf(
            'mytemplate.html',
            {
                'pagesize':'letter',
                'persona': p,
                # 'mylist': results,
            }
        )

def persona_area(request, fecha_inicio, fecha_fin):
    inicio = fecha_inicio
    fin = fecha_fin
    ddata = Persona.objects.values('area'
                                   ).annotate(count=Count('area')
                                              ).filter(fecha_inicio__gte=inicio
                                                       ).filter(fecha_fin__lte=fin)
    ddata = zip(*[x.values() for x in ddata])
    if len(ddata) == 0:
        return HttpResponseRedirect(reverse('error'))
    xdata,zdata = ddata
    ydata = ()
    for i in zdata:
        if i == 0:
            new = 'Ortopedia Infantil'
            ydata = ydata + (new,)
        elif i == 1:
            new = 'Hombro'
            ydata = ydata + (new,)
        elif i == 2:
            new = 'Columna'
            ydata = ydata + (new,)
        elif i == 3:
            new = 'Cadera'
            ydata = ydata + (new,)
        elif i == 4:
            new = 'Miembros inferiores'
            ydata = ydata + (new,)
        elif i == 5:
            new = 'Neuro-Ortopedia'
            ydata = ydata + (new,)
        elif i == 6:
            new = 'Medicina fisica y rehabilitacion'
            ydata = ydata + (new,)
        elif i == 7:
            new = 'Cirugia de mano'
            ydata = ydata + (new,)
        elif i == 8:
            new = 'Pediatria'
            ydata = ydata + (new,)
        elif i == 9:
            new = 'Fisioterapia'
            ydata = ydata + (new,)
        elif i == 10:
            new = 'Terapia del Lenguaje'
            ydata = ydata + (new,)
        elif i == 11:
            new = 'Taller de Ortopedia'
            ydata = ydata + (new,)
        elif i == 12:
            new = 'Terapia Ocupacional'
            ydata = ydata + (new,)
    chartdata = {'x': ydata, 'y': xdata}
    charttype = "discreteBarChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'piechart_2.html', data)

def persona_programa(request, fecha_inicio, fecha_fin):
    inicio = fecha_inicio
    fin = fecha_fin
    ddata = Persona.objects.values('tipo'
                                   ).annotate(count=Count('tipo')
                                              ).filter(fecha_inicio__gte=inicio
                                                       ).filter(fecha_fin__lte=fin)
    ddata = zip(*[x.values() for x in ddata])
    if len(ddata) == 0:
        return HttpResponseRedirect(reverse('error'))
    xdata,zdata = ddata
    ydata = ()
    for i in zdata:
        if i == 0:
            new = 'Pasantia'
            ydata = ydata + (new,)
        elif i == 1:
            new = 'Post-Grado'
            ydata = ydata + (new,)
        elif i == 2:
            new = 'Fellow'
            ydata = ydata + (new,)
        elif i == 3:
            new = 'Visitor'
            ydata = ydata + (new,)
    chartdata = {'x': ydata, 'y': xdata}
    charttype = "discreteBarChart"
    chartcontainer = 'discretebarchart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'tooltips':False,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'piechart_3.html', data)

def persona_genero(request, fecha_inicio, fecha_fin):
    inicio = fecha_inicio
    fin = fecha_fin
    ddata = Persona.objects.values('sexo'
                                   ).annotate(count=Count('sexo')
                                              ).filter(fecha_inicio__gte=inicio
                                                       ).filter(fecha_fin__lte=fin)
    ddata = zip(*[x.values() for x in ddata])
    if len(ddata) == 0:
        return HttpResponseRedirect(reverse('error'))
    xdata,ydata = ddata
    ydata = ['Femenino', 'Masculino']
    chartdata = {'x': ydata, 'y': xdata}
    charttype = "discreteBarChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'piechart_1.html', data)


def paises_global(request, fecha_inicio, fecha_fin):
    inicio = fecha_inicio
    fin = fecha_fin
    ddata = Persona.objects.values('pais_nacimiento'
                                   ).annotate(count=Count('pais_nacimiento')
                                              ).filter(fecha_inicio__gte=inicio
                                                       ).filter(fecha_fin__lte=fin)
    ddata = zip(*[x.values() for x in ddata])
    if len(ddata) == 0:
        return HttpResponseRedirect(reverse('error'))
    xdata, ydata = ddata
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "discreteBarChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'piechart.html', data)

def report_error(request):
    return render(request, 'report_error.html')

def report(request):
    if request.method == 'POST':
        form = Report(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            fecha_inicio = form.cleaned_data['pinicio']
            fecha_fin = form.cleaned_data['pfin']
            if tipo == '1':
                return persona_programa(request, fecha_inicio, fecha_fin)
            elif tipo == '2':
                return persona_area(request, fecha_inicio, fecha_fin)
            elif tipo == '3':
                return paises_global(request, fecha_inicio, fecha_fin)
            elif tipo == '4':
                return persona_genero(request, fecha_inicio, fecha_fin)
    else:
        form = Report()

    return render(request, 'reports.html', {
        'form': form,
    })
