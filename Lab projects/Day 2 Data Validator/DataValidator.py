# def valid_email(email):
#     if email.count("@") != 1:
#         return False
#     for i in email:
#         if not i.isascii():
#             return False
#     parts = email.split('@')
#     for i in parts[1]:
#         if not i.isalnum() and i not in (".", "-"):
#             return False
#     if not parts[0] or not parts[1] or len(parts[0]) > 64 or len(parts[1]) > 255:
#         return False
#     if parts[0][0] == "." or parts[0][-1] == "." or parts[1][0] == "." or parts[1][-1] == ".":
#         return False
#     for i in range(len(parts[0]) - 1):
#         if parts[0][i] == "." and parts[0][i+1] == ".":
#             return False
#     return True
#

def valid_url(url):
    print(url[:12])
    if (url[:12] == "https://www." and url[12:]) or (url[:11] == "http://www." and url[11:]):
        return True
    return False

print(valid_url("http://www.dfghj"))