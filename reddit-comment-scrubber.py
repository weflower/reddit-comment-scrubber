import csv, praw, argparse, datetime

# Define your username
myUserName=''

# Create reddit object
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='comment-scrubber',
                     username=myUserName)

# Clean only these subreddits. The value should be set like: subList = ['pics','aww','politics']
subList = []

# Number of comments to process
commentLimit=2000

# Prefix to add to permalinks in output
permalinkPrefix = 'https://old.reddit.com'

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s -m <mode> -d <cutoff date>",
        description="Clean or delete comments from a Reddit account."
    )

    parser.add_argument("-m", "--mode", choices=['scrub', 'delete'],help='The mode to run. The value must be \"scrub\" or \"delete\".')
    parser.add_argument("-d", "--date", help='The cutoff date; any comments before this date are processed. The value must be in the format: \"YYYY-mm-dd\".')

    return parser

def main():

    parser = init_argparse()
    args = parser.parse_args()

    if (args.mode == None or args.date == None):
        parser.print_help()
        exit()

    cutoff = datetime.datetime.strptime(args.date, '%Y-%m-%d')

    print('Script started in ' + str(args.mode) + ' mode.')
    print('Cutoff date is: ' + str(cutoff))
    print()
    
    # Create user object
    thisUsr = User(myUserName);
    
    if thisUsr.invalid_flag != True:
        
        # Loop through all of this suspect's comments
        for currentComment in thisUsr.comment_list:
            created_datetime = datetime.datetime.utcfromtimestamp(currentComment.created_utc)
            
            if (created_datetime < cutoff):
                if (args.mode == "scrub"):
                    currentComment.edit("*Comment has been automatically scrubbed via script.*")
                    print("Comment scrubbed: " + permalinkPrefix + currentComment.permalink)
                elif (args.mode == "delete"):
                    currentComment.delete()
                    print("Comment deleted: " + permalinkPrefix + currentComment.permalink)
                else:
                    print('Error: Invalid mode.')
    
    print()
    print('Script completed.')
    

# User class
class User:
    def __init__(self, userName):
        if (len(subList) > 0):
            comment_list = [x for x in reddit.redditor(userName).comments.new(limit=commentLimit) if str(x.subreddit).lower() in subList]
        else:
            comment_list = [x for x in reddit.redditor(userName).comments.new(limit=commentLimit)]
            
        self.name = userName
        
        if len(comment_list) < 1:
            self.invalid_flag = True
        else: 
            self.invalid_flag = False
            self.comment_list = comment_list
            
if __name__ == "__main__":
    main()
