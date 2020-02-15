from django.shortcuts import render
from parsed_data.models import Cmt, Link, Member
from django.views import generic
from parsed_data.forms import searchNickForm

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

    def get_queryset(self):
        member_list = Member.objects.all()
        searchNick = self.request.GET.get('search_nick', '')  # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
        if searchNick:  # q가 있으면
            member_list = member_list.filter(nickname_text__icontains=searchNick)  # 제목에 q가 포함되어 있는 레코드만 필터링

        return member_list


class MemberDetailView(generic.DetailView):
    model = Member
