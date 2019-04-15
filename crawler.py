import praw

reddit = praw.Reddit(client_id='QZennBK3huGPAQ',
                     client_secret='6Ln46EaQTkd5yVxE0VqgPEHe9NM',
                     username='dskeemer',
                     password='5yv545b1',
                     user_agent='crawler1')

front_page = reddit.front.hot()

for submission in frontpage.stream.submissions():
    if not submission.stickied:
        print('Title: {}, ups: {}, downs {}, comments: {}'.format(submission.title,
                                                    submission.ups,
                                                    submission.downs,
                                                    submission.num_comments))


