from django.http import JsonResponse

def return_404_error(request, exception):
    return JsonResponse({ "error": "Invalid URL" }, status=404)

def return_500_error(request):
    return JsonResponse({ "error": "Internal error" }, status=500)
