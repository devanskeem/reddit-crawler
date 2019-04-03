import praw

reddit = praw.Reddit(client_id='QZennBK3huGPAQ',
                     client_secret='6Ln46EaQTkd5yVxE0VqgPEHe9NM',
                     username='dskeemer',
                     password='5yv545b1',
                     user_agent='crawler1')

subreddit = reddit.subreddit('tifu')

hot_tifu = subreddit.hot(limit=10)


front_page = reddit.front.hot(limit=100)

for submission in hot_tifu:
    if not submission.stickied:
        print('Title: ', submission.title, submission.url, '\n-----------')
# for submission in hot_python:
#     if not submission.stickied:
#         print('Title: {}, ups: {}, downs {}, comments: {}'.format(submission.title,
#                                                     submission.ups,
#                                                     submission.downs,
#                                                     submission.num_comments))

        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        for comment in comments:
            print(20*'-')
            print(comment.body)

