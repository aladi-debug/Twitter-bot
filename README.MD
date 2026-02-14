# TechCrunch-Twitter Bot 🤖

this program retrives the latest news of tech from techcrunch and posts it on twitter
## 🚀 Features
- **Parser:** Uses [feedparser](https://pythonhosted.org/feedparser/introduction.html) to get the "latest" [techcrunch](https://TechCrunch.com) news.
- **Bypass:** Injects session cookies to skip Google/Twitter login using [editthiscookie](https://chromewebstore.google.com/detail/editthiscookie-v3/ojfebgpkimhlhcblbalbfjblapadhbol). Note: This is necessary because Google blocks sign-in attempts from automated browsers unconditionally [learnmore](https://support.google.com/accounts/answer/7675428?hl=en&co=GENIE.Platform%3DAndroid), it makes the code less by a huge margin since you don't need to know how every one prefers to log in, makes it securer since you won't have your human-readable credentials in the code as variables and i'm not(not yet) at the level where i could bypass the security of twitter specifically made to stop bots trying to bypass. 
- **Automation:** Selenium-driven search and navigation. more of it is [here](https://www.selenium.dev/documentation/)

## 🛠 Setup
1. **Install Dependencies:**
   ```bash
   pip install selenium feedparser json 
   


2. **copying cookies to bybass**

    got to [editthiscookie](https://chromewebstore.google.com/detail/editthiscookie-v3/ojfebgpkimhlhcblbalbfjblapadhbol) and install.

    go to your browser where you logged in on your [twitter](https://x.com/home), press the extension button on your browser, press editthiscookie 
    and then export by pressing the downward arrow. navigate to twitter_cookies.json(the file is already in the folder) and paste all of that in.

3. **MUST DO FOR THE PROGRAM TO WORK**
    if there is a problem with line 25. then make sure that your running the program from the parent folder or just give the full path e.g. C:\Users\[NAME]\[downloads]\Twitter-bot

    if you intend not make any changes. then the program must run on the parent folder e.g. TWitter-bot directory



> [!IMPORTANT]
> Please note that extreme use (e.g., 500+ posts a day) may violate platform terms of service and/or degrade the experience for others. Please use this tool responsibly and in good faith.
