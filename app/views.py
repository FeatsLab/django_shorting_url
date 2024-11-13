from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import URL
from .utils import is_valid_url
import pyshorteners
from django.contrib.auth.decorators import login_required


def shorten_url(request):
    error_message = None  
    url = None

    if request.method == 'POST':
        original_url = request.POST.get('url')

        if URL.objects.filter(original_url=original_url):
            return HttpResponse(f'Unique Not valid: {original_url}\n Given url alredy in record please delete first.')
        
        # Validate the URL
        if not is_valid_url(original_url):
            error_message = "Invalid URL. Please enter a valid URL."  # Set error message
        else:
            # If URL is valid, generate short code using pyshorteners
            short_code = pyshorteners.Shortener().tinyurl.short(original_url)

            # Save the original URL and short code in the database
            url = URL.objects.create(original_url=original_url, short_code=short_code)
            

    # Render the template with the URL data and the possible error message
    return render(request, 'shortener/shorten_url.html', {'error_message': error_message, 'url' : url})


def delete_url(request, url_id):
    try:
        # Fetch the URL object by ID
        url_to_delete = URL.objects.get(id=url_id)
        
        # Delete the URL object
        url_to_delete.delete()
        
        # Redirect back to the URL list page
        return redirect('admin_page')
    except URL.DoesNotExist:
        # If the URL doesn't exist, redirect back with an error message
        return redirect('admin_page') 
    

def redirect_url(request, url_id):
    # Get the URL object by its short_code
    url = get_object_or_404(URL, id=url_id)
    
    # Increment the number of times this URL has been accessed
    url.number_of_time += 1
    url.save()  # Save the updated number of times
    
    # Redirect to the original URL
    return redirect(url.short_code)

@login_required
def admin_view(request):
    # Fetch all URLs from the database to display in the table
    urls = URL.objects.all()
    return render(request, 'shortener/admin/data_manage.html', {'urls': urls})
