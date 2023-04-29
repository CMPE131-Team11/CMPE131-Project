# Gmail clone Group 11
- Gene Luong (@FluffyFTW)
- Kerry Liu (@kerrycliu)
- Rafael Antipuesto (@raf023)
- Ketan Ambati (@shambutennis)

# Installation
```
 $ pip install -r requirements.txt
 ```

# Running the code
```
 $ python3 main.py
 ```

# Warnings
```
This google cloud developer project is unverified and will in turn throw a massive warning on the screen. We will not be uploading the token or .db file so it should be generally safe, if you want to trust me. To get passed the warning, simply press advanced -> proceed to testing
 ```

# Use case testing
- Sign In -- Group
    1. Go to http://127.0.0.1:5000/sign_up/
    2. Register a new username with a password, you cannot have multiple same usernames
    3. This will auto log you into the home page

- Login -- Group
    1. Go to http://127.0.0.1:5000/login/
    2. Enter existing loggin credentials
    3. This will send you to home if the credentials exist

- Delete Account -- Group
    1. Go to http://127.0.0.1:5000/home/
    2. Click Delete

- Log Out Account -- Group
    1. Go to http://127.0.0.1:5000/home/
    2. Click Log Out

- Send Email -- Raf
    1. Click 'Send Email' button
    2. Enter the subject 
    3. Enter recipient email
    4. Enter body 
    5. Press Send Button
    6. Note: This may prompt a verification link in the terminal

- Edit User Profile -- Ketan
    1. Successfully login to your account
    2. Click the 'Edit Profile' button at the top of the screen
    3. Enter in the desired changes into the username and password text boxes
    4. Click Save
    5. The changes for the username can be seen in the home page adn changes for password can be seen when you login in again

- Add Calendar event -- Gene
    1. Go to http://127.0.0.1:5000/home/
    2. Click the 'Add Event To Calendar' button at the top of the screen
    3. Enter in the Title, Start Time, End Time and Attendees (one for now)
    4. Enter a description (optional)
    5. Hit sent, this will update your gmail calendar
    6. Make sure the End time is greater than the start time
    7. Note: This may prompt a verification link in the terminal

- Create Tasks -- Kerry
    1. After logged into your account, click on Create a Task
    2. Enter the email address that you want the task to assign to
    3. Enter the title for your task
    4. Enter the task that you need to finish under that title.
    5. You will be asked to sign in with your Gmail account for authenticaion. 
    6. Go to Gmail and you will see your task being added in your Gmail Task located on the right side of the Gmail inbox page.