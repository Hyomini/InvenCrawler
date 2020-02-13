import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "invenCrawler.settings")
import django
django.setup()
from parsed_data.models import Link
from parsed_data.models import Cmt

if __name__ == "__main__":
    tmp = Cmt.objects.filter(nickname__nickname_text__exact='Gnar')
    comment_list = []
    for t in tmp:
        comment_list.append(t.comment)
    print(comment_list)
