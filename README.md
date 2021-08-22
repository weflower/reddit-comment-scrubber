# Reddit Comment Scrubber
This Python script edits (scrubs) or deletes reddit comments based on a specified time period.

To enable this script to access your comments:

1. Install [Python](https://www.python.org/):
   1. Make sure it's added to your PATH environment variable.
   2. Install the pip utility when given the option.

2. Open a command prompt and install the PRAW plugin for python.
   ```shell
   pip install praw
   ```

3. Create an app definition in Reddit.
   1. Go to [reddit.com](https://old.reddit.com) > **Preferences** > **Apps**.
   2. Click **Create another app**.
   3. Name the app "comment-scrubber".
   4. Select the *script* option.
   5. In the `redirect-url` field, enter this value:  
      ```
      http://localhost:8080
      ```
   8. Click **create app**.
   9. Take note of the app's client ID, which is right below the name you gave it.
   10. Take note of the client secret.

4. In the file reddit-comment-scrubber.py:
   1. Modify line 4 to add your username.
   2. Modify lines 7-11 to add the correct client ID, client secret, your reddit password, the user agent (the name you gave the app), and your user name.
   3. If you want to limit cleaning to a specific set of subreddits, modify line 14 to list them in the array. For example:
      ```python
      subList = ['politics', 'pics', 'aww']
      ```    
      Otherwise, leave the array empty.

5. Open a command prompt where the reddit-comment-scrubber.py is located, and run it with one of these commands:
   * To replace comments' text with generic text:
     ```shell
      python reddit-comment-scrubber.py -m scrub -d 2020-01-01
      ```
     The body is replaced with this text: "*Comment has been automatically scrubbed via script.*"
     
   * To delete comments:
     ```shell
     python reddit-comment-scrubber.py -m delete -d 2020-01-01
     ```
     
   **Note:** For stability, the script only processes the most recent 2000 comments in your account. You can modify this limit on line 14, but the script has not been tested with higher numbers.

As the script runs, it outputs the progress as each comment is processed. The console output might look like this example:
```shell
Script started in scrub mode.
Cutoff date is: 2020-01-12 00:00:00

Comment scrubbed: <link to comment>
Comment scrubbed: <link to comment>
Comment scrubbed: <link to comment>
Comment scrubbed: <link to comment>

Script completed.
```