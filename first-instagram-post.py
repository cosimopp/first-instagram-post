import instaloader #first pip install instaloader, then proceed
L = instaloader.Instaloader()
L.login("yourusername", "yourpassword")
p = list(instaloader.Profile.from_username(L.context, "chiaraferragni").get_posts())
print(f"1st absolute post: instagram.com/p/{str(p[len(p) - 1])[6:-1]}") #It could take 15 mins
print(f"2nd absolute post: instagram.com/p/{str(p[len(p) - 2])[6:-1]}")
print(f"3rd absolute post: instagram.com/p/{str(p[len(p) - 3])[6:-1]}")