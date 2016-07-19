from django.http import HttpResponse
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.shortcuts import render
from waitBackened.collect_events import *
from django.http import HttpResponseRedirect

def wait_for_backend(request):
	if 'units_distance' in request.GET:
		latitude = request.GET['latitude']
		longtitude = request.GET['longtitude']
		covered_area = request.GET['covered_area']
		units_distance = request.GET['units_distance']
		select_category_event = request.GET['select_category_event']
		li=event_collection(latitude, longtitude, covered_area, units_distance, select_category_event)
		#j=len(li)
		i=0
		#Database starts now!!!
    	event.objects.order_by('-Date','-score')
    	for idd in li:
    		Event.object.filter('Eventid' == idd)
    		x_comm[i]=Event['Nocomments']
    		x_likes[i]=Event['Nolikes']
    		x_name[i]=Event['Eventname']
    		x_link[i]=Event['NoImages']
    		
   		
		scatter_diag = plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], filename='my-graph.html', auto_open=False, output_type='div')
    	bar_diag = plot([Bar(x=['1', '2', '3'], y=[13, 10, 50])], filename='my-bar.html', auto_open=False, output_type='div')
    	fig = {
		'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
		'values': [19, 26, 55],
		'type': 'pie'}],
		'layout': {'title': 'Event Comparison'}
		}
	return HttpResponseRedirect("/visual/")

