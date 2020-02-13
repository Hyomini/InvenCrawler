from django.shortcuts import render
from parsed_data.models import Cmt, Link, Member
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_members = Member.objects.all().count()
    num_cmts = Cmt.objects.all().count()

    # The 'all()' is implied by default.
    num_links = Link.objects.count()

    context = {
        'num_members': num_members,
        'num_cmts': num_cmts,
        'num_links': num_links,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MemberListView(generic.ListView):
    model = Member
    paginate_by = 30


class MemberDetailView(generic.DetailView):
    model = Member