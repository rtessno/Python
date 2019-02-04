import re

test_html = "<>" \
            "<b>" \
            "<!--..-->" \
            "<!DOCTYPE>" \
            "</b>"

# print(bool(re.match("<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>", test_html)))
print(bool(re.match( " " ,test_html)))