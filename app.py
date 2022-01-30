# Importing the required modules.
import praw


# Creating a read-only reddit instance.
reddit = praw.Reddit(
    # From reddit Third Party App Authorization, create a new app and fill the following.
    client_id = "tu8goLFqiIjr1SfrnaVrDA",
    client_secret = "BzBM7KW8iZ4HXVPFN4AP4yyM0tM-AA",
    user_agent = "R-scraper-newsletter",
)


# main function
if __name__ == "__main__":
    # print(reddit.read_only)

    file = open("Test.txt", "w+")

    sub = "NuclearRevenge"

    # subName = sub.display_name
    subTitle = sub.title
    # subDescription = sub.description

    subHead = [subTitle]

    file.writelines(sub + "\n")

    letterText = []

    i = 5

    letterText.append("*** Hot Submissions!!! ***\n")
    for hot_submission in reddit.subreddit(f"{sub}").hot(limit=i):
        letterText.append(hot_submission.title)

    j = 0

    while j <= i:
        for lines in letterText:
            file.writelines("#" + " => " + str(lines) + "\n")
            j += 1

    file.close()
    print("Completed. Exiting.")