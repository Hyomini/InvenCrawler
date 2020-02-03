import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "invenCrawler.settings")
import django
django.setup()
from parsed_data.models import LinkData

if __name__ == "__main__":
    tmp = LinkData.objects.all()
    link_list = []
    for t in tmp:
        link_list.append(t.link)
    print(link_list)