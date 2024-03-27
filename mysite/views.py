from django.shortcuts import render

def custom_error_view(request, exception=None):
    return render(request, 'error.html', {
        'error_code': 404,
        'error_message': 'Page not found'
    }, status=404)

#
# def homepage(request):
#     return render(request, 'countries.html')
#
# def about(request):
#     return render(request, 'about.html')