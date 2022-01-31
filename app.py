# Importing the required modules.
from msilib.schema import Class
import praw
import time
import threading

# Creating a read-only reddit instance.
reddit = praw.Reddit(
    # From reddit Third Party App Authorization, create a new app and fill the following.
    client_id = "tu8goLFqiIjr1SfrnaVrDA",
    client_secret = "BzBM7KW8iZ4HXVPFN4AP4yyM0tM-AA",
    user_agent = "R-scraper-newsletter",
)

i = 5

class fetchArticle:
    def fetchHotArticle(self):
        letterText.append("*** Hot Submissions!!! ***\n")
        for hotSubmission in reddit.subreddit(f"{sub}").hot(limit=i):
            letterText.append(hotSubmission.title + " " + "(" + hotSubmission.url + ")\n")

    def fetchRisingArticle(self):
        letterText.append("*** Rising Submissions!!! ***\n")
        for risingSubmission in reddit.subreddit(f"{sub}").rising(limit=i):
            letterText.append(risingSubmission.title + " " + "(" + risingSubmission.url + ")\n")

    def fetchNewArticle(self):
        letterText.append("*** New Submissions!!! ***\n")
        for newSubmission in reddit.subreddit(f"{sub}").new(limit=i):
            letterText.append(newSubmission.title + " " + "(" + newSubmission.url + ")\n")

    def fetchConArticle(self):
        letterText.append("*** Controversial Submissions!!! ***\n")
        for conSubmission in reddit.subreddit(f"{sub}").controversial(limit=i):
            letterText.append(conSubmission.title + " " + "(" + conSubmission.url + ")\n")

    def __init__(self):
        t1 = threading.Thread(target=self.fetchHotArticle)
        t2 = threading.Thread(target=self.fetchRisingArticle)
        t3 = threading.Thread(target=self.fetchNewArticle)
        t4 = threading.Thread(target=self.fetchConArticle)

        t1.start()
        t1.join()

        t2.start()
        t2.join()

        t3.start()
        t3.join()

        t4.start()
        t4.join() 
        
def writeToFile(i, j, file):
    while j < i:
        for lines in letterText:
            file.writelines("#" + " => " + str(lines) + "\n")
            j += 1


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

    fetchArticle()

    j = 0

    writeToFile(i, j, file)

    file.close()    
    t2 = time.time()
    duration = t2 - t1
    print("Completed. Exiting. Duration: " + f"{duration}")