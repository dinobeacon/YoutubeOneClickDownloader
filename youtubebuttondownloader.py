from firefox_profile import FirefoxProfile
from pytube import YouTube
from sys import argv

def youtube_downloader(link):
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download('C:\\Users\\nourb\\Videos\\ytd')

for profile in FirefoxProfile.get_profiles():
    recovery_data = profile.get_recovery_data()
    if recovery_data is None:
        continue
    for i, window in enumerate(recovery_data.windows):
        # do something with window:
        print(f"window {i}")
        print(f"  tabs:")
        for j, tab in enumerate(window.tabs):
            # do something with tab:
            undu = tab.url
            print(f"    tab {j}")
            print(f"      url: {tab.url}")
            if 'youtube' in undu:
                youtube_downloader(undu)
                print("sucessfully downloaded")

