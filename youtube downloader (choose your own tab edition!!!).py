from firefox_profile import FirefoxProfile
from pytube import YouTube

Dlink = []
Dlink_Name = []

def youtube_downloader(link):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download('C:\\Users\\nourb\\Videos\\ytd')


for profile in FirefoxProfile.get_profiles():
    recovery_data = profile.get_recovery_data()
    if recovery_data is None:
        continue
    for i, window in enumerate(recovery_data.windows):
        print(f"window {i}")
        print(f"  tabs:")
        for j, tab in enumerate(window.tabs):
            print(f"    tab {j}")
            print(f"      url: {tab.url}")
            if 'https://www.youtube.com/' == tab.url:
                    print("unable to use general directory for youtube")
            elif 'youtube.com' in tab.url:
                Dlink.append(tab.url)


for z in range(len(Dlink)):
    urlz = YouTube(Dlink[z])
    url_title = urlz.title
    Dlink_Name.append("Position (" + str(z) + ") :  " + url_title)

print(" ")
print(" These are the retrieved links from youtube")
print (" ")
print( '\n'.join(Dlink))
print(" ")
print("These are the names of the videos retrieved ")
print(" ")
print( '\n'.join(Dlink_Name))
print(" ")


Newlink_positions = []

k = 1

while k == 1 :
    for l in range(len(Dlink)):
        a = input("Please enter which video to download. Please only use positions from previois printed list ")
        if a == "end":
            k+=1
            break
        try:
            x = int(a)
            Newlink_positions.append(x)

        except ValueError:
            print("please enter an integer")




for u in range(len(Newlink_positions)):
    print("position : " + str(Newlink_positions[u]))
    youtube_downloader(Dlink[Newlink_positions[u]])
    print("download successful")
