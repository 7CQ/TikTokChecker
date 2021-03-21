from TikTokApi import TikTokApi
import string
import random

verifyFp = "REPLACE THIS WITH YOUR OWN verifyFp IF YOU WANT TO USE THE FYP FUNCTON!"

totalLikes = 0
totalDuration = 0
totalVerified = 0
totalViews = 0
leastLikes = 1000000000000000
leastLikesId = 0
mostLikes = 0
mostLikesId = 0

userName = input("Username to check(type None to check fyp): ")
videosToCheck = input("Enter amount (below 2000) of videos to check: ")
videosToCheckCount = False
try:
    videosToCheckCount = int(videosToCheck)
except ValueError:
    print('Not a valid number! Checking default value: 10')
    videosToCheckCount = False

if videosToCheckCount >= 2000:
    print('Not a valid number! Checking default value: 10')
    videosToCheckCount = False

if videosToCheckCount:
    if videosToCheckCount <= 0:
        print('Not a valid number! Checking default value: 10')
        videosToCheckCount = False



did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFy=verifyFp, use_test_endpoints=True, custom_did=did)

if (userName.lower()) == 'none':
    if videosToCheckCount:
        tiktoks = api.by_trending(videosToCheckCount)
    else:
        tiktoks = api.by_trending(10)
else:
    if videosToCheckCount:
        tiktoks = api.by_username(userName ,videosToCheckCount)
    else:
        tiktoks = api.by_username(userName ,10)

def getAvrage(total, count):
    return total / count

for tiktok in tiktoks:
    author = tiktok['author']['uniqueId']
    verified = tiktok['author']['verified']
    VideoId = tiktok['id']
    authorId = tiktok['author']['id']
    musicName = tiktok['music']['title']
    musicId = tiktok['music']['id']
    duration = tiktok['video']['duration']
    likes = tiktok['stats']['diggCount']
    views = tiktok['stats']['playCount']

    totalLikes += likes
    totalViews += views
    totalDuration += duration
    if verified:
        totalVerified += 1
    if likes <= leastLikes:
        leastLikes = likes
        leastLikesId = VideoId
    if likes >= mostLikes:
        mostLikes = likes
        mostLikesId = VideoId



#    print("Author: " + str(author))
#    print("Verified: " + str(verified))
#    print("VideoId: " + str(VideoId))
#    print("Duration: " + str(duration))
#    print("AuthorId: " + str(authorId))
#    print('MusicName: ' + str(musicName))
#    print('MusicId: ' + str(musicId))

if tiktoks:
    print("Avrage Likes: " + str(getAvrage(totalLikes, len(tiktoks))))
    print("Views Per Like: " + str(getAvrage(totalViews, len (tiktoks)) / getAvrage(totalLikes, len(tiktoks))))
    print("Avrage duration: " + str(getAvrage(totalDuration, len(tiktoks))))
    print("Videos Checked: " + str(len(tiktoks)))
    print('\n')
    print("Most liked video: " + str(mostLikes))
    print("Most liked video id: " + str(mostLikesId))
    print("Least liked video: " + str(leastLikes))
    print("Least liked video id: " + str(leastLikesId))
    print("Total likes: " + str(totalLikes))
    print("Total views: " + str(totalViews))
else:   
    print("NOT ANY VALID VIDEOS!")