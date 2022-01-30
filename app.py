# Importing the required modules.
import praw
import time

# Creating a read-only reddit instance.
reddit = praw.Reddit(
    # From reddit Third Party App Authorization, create a new app and fill the following.
    client_id = "tu8goLFqiIjr1SfrnaVrDA",
    client_secret = "BzBM7KW8iZ4HXVPFN4AP4yyM0tM-AA",
    user_agent = "R-scraper-newsletter",
)


# main function
if __name__ == "__main__":

    t1 = time.time()

    # print(reddit.read_only)

    file = open("Test.txt", "w+")

    sub = "piracy"

    # subName = sub.display_name
    subTitle = sub.title
    # subDescription = sub.description

    subHead = [subTitle]

    file.writelines(sub + "\n\n")

    letterText = []

    i = 5

    letterText.append("*** Hot Submissions!!! ***\n")
    for hotSubmission in reddit.subreddit(f"{sub}").hot(limit=i):
        letterText.append(hotSubmission.title + " " + "(" + hotSubmission.url + ")")

    letterText.append("\n\n")

    letterText.append("*** New Submissions!!! ***\n")
    for newSubmission in reddit.subreddit(f"{sub}").new(limit=i):
        letterText.append(newSubmission.title + " " + "(" + newSubmission.url + ")")

    letterText.append("\n\n")

    letterText.append("*** Controversial Submissions!!! ***\n")
    for conSubmission in reddit.subreddit(f"{sub}").controversial(limit=i):
        letterText.append(conSubmission.title + " " + "(" + conSubmission.url + ")")

    j = 0

    while j < i:
        for lines in letterText:
            file.writelines("#" + " => " + str(lines) + "\n")
            j += 1

    file.close()    
    t2 = time.time()
    duration = t2 - t1
    print("Completed. Exiting. Duration: " + f"{duration}")