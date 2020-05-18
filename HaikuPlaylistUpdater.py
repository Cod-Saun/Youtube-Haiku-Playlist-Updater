#Python Reddit API Wrapper
import praw
import re
import os
#Google libraries for youtube Data API
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

#----------------REDDIT PORTION OF APP------------------------
#List of video Urls
videos = []

#reddit API client setup
reddit = praw.Reddit(client_id = os.environ.get("REDDIT_CLIENT_ID"),
                     client_secret = os.environ.get("REDDIT_CLIENT_SECRET"),
                     user_agent="my user agent")

#get top 10 submissions of /r/youtubehaiku and add them to the videos list
for submission in reddit.subreddit('youtubehaiku').top('month', limit=40):
    videos.append(submission.url)

##----------------YOUTUBE PORTION OF APP---------------------
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_id.json"

## Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

VidID = ""
#lines 36-44 adapted from silentsokolov @ https://gist.github.com/silentsokolov/f5981f314bc006c82a41
regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')

for i in range(len(videos)):
export TEST_API_KEY=ABC123
    match = regex.match(videos[i])

    if not match:
        print('no match')
    VidID = match.group('id')
    print("Adding Video " + match.group('id'))

    body = {
      "snippet": {
        "playlistId": os.environ.get("YOUTUBE_PLAYLIST_ID"),
        "resourceId": {
            "kind": "youtube#video",
            "videoId": VidID
        }
      }
     }

    request = youtube.playlistItems().insert(part="snippet", body=body)
    try:
      response = request.execute()
    except:
      pass