from django.http import HttpResponseRedirect
from forms import NewLinkForm
from annoying.decorators import render_to
from models import Link

@render_to('new_link.html')
def new_url(request):
	if request.method == 'POST':
		form = NewLinkForm(request.POST)
		if form.is_valid():
			link = form.save()
			url = "http://localhost:9000/link/%s" % link.key
			return HttpResponseRedirect(url)
	else:
		form = NewLinkForm()

	return locals()


@render_to('view_shorten.html')
def view_shorten(request, key):
	"""
	Page that shows the shortened link and the page it points to
	"""
	link = Link.objects.get(key=key)
	print link
	return locals()

def do_redirect(request, key):
	link = Link.objects.get(key=key)
	return HttpResponseRedirect(link.url)