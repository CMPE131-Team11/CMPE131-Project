## Functional Requirements
1. Register Account     group
2. Edit User Profile    Ketan
3. Send email           Raf
4. Create Task          Kerry
5. begin chat           Kerry
6. open global chat     Kerry
7. add event            Gene 
8. send event reminder  Gene
9. search for email     Gene
10. log out             group
11. login               Ketan
12. Delete account      group

## Non-functional Requirements

1. send email 500ms
2. implement the google api

## Use Cases

1. Register Account
- **Trigger:**
  1. A first-time user enters our application or a user clicks on the ‘register account’ button

- **Primary Sequence:**
  1. The user clicks the register account button
  2. Enters a valid User Name
  3. Enters a valid password
  4. Enters First and Last Name
  5. Clicks register button

- **Primary Postconditions:**
  1. The user is logged in to their account and can do anything a signed-in user can do

- **Alternate Sequence:** 
  1. A user enters an invalid username or password
     System response with invalid username or password and reason why it’s invalid
     The user re-enters a valid username and password


2. Edit User Profile
- **Trigger:**
  1. User clicks on ‘Edit Profile’ button

- **Primary Sequence:**
  1. User clicks ‘edit profile’ button
  2. User makes all desired edits
  3. User clicks ‘Save button’
  4. User clicks ‘Exit Profile’ button

- **Primary Postconditions:** 
  1. All edited changes are applied to the User

- **Alternate Sequence:** 
  1. User clicks ‘Exit’ before ‘Save’ button
     System sends alert saying ‘Do you want to sasve changes’
     Systems saves changes depending on User’s answers


3. Send email
- **Pre-condition:** 
  1. User is logged in

- **Trigger:**
  1. User presses compose button

- **Primary Sequence:**
  1. User types recipient name(s) 
  2. User writes the subject
  3. User writes the message they want to send
  4. User presses the "Send" button 
  5. System prompts the user with a date box and a time box 
  6. User inputs the date and time into respective boxes
  7. User presses the "Schedule send" button
  8. User is sent to the homescreen

- **Primary Postconditions:**
  1. System displays “message has been sent"

- **Alternate Sequence:**  
  1. Recipient names are not in the system	
      - System displays error
      - System prompts “Invalid Recipient name(s)”

  1. User inputs an invalid schedule time 
      - System displays error
      - System prompts Invalid schedule time ”


4. Create Task
- **Pre-condition:** 
  1. User have an account and have logged into their account

- **Trigger:** 
  1. The user click on the 'Create' button

- **Primary Sequence:**
  1. User navigate to the 'Task' section on the home screen and click on 'Create New Task' button
  2. System prompts the user to enter the date for the task to be done or due
  3. User enters the date manually on the date bar
  4. System checks if the date is valid (cannot be before the date of making the task)
  5. User enters a title for the task
  6. User enters the summary or details of the task
  7. System saves the Task
  8. User close the Task window

- **Primary Postconditions:** 
  1. The user reveives a message notification indicates the task has been created
  2. The user can see the task on calendar

- **Alternate Sequence:**
  1. User enters a date that has already passed
      - The system displays error message indicates that the day has already passed
      - The system lets the customer to enter the date again 


5. Begin Chat
- **Pre-condition:** 
  1. User have an account and have logged into their account

- **Trigger:**  
  1. The user click on the 'Chat' button

- **Primary Sequence:**
  1. User navigates through the home screen and select the chat option
  2. System prompts a list of contacts
  3. User selects the name of the contact
  4. System prompts a chat window
  5. User enters message in the chat box
  6. System sends the message to the person of contact
  7. User closes the chat window

- **Primary Postconditions:**  
  1. The user reveives a message notification indicates when the person of contact replies back
  2. User can see the history of chat

- **Alternate Sequence:**
  1. User cannot find the contact in the list of already existing contacts
      - The system allows user to enter the email address of the contact manually
      - The system asks user to save the new contact to the list of contacts


8. Open Global Chat  
- **Pre-condition:** 
  1. User have an account and have logged into their account

- **Trigger:**  
  1. User Presses on the 'Chat Room' button

- **Primary Sequence:**
  1. User is prompted with the UI of the chat room
  2. User scrolls through the messages
  3. Displayes the message, who its sent by and to and at one time

- **Primary Postconditions:**  
  1. Printed messages

- **Alternate Sequence:**
 1. User decides to leave the page
    - presses the 'Home' button


7. Add Event
- **Pre-condition:** 
  1. User have an account and have logged into their account
  1. User has event details

- **Trigger:** 
  1. The user click on the 'Create Event' button

- **Primary Sequence:**
  1. New Task Popup has appeared
  2. Ask for Event name
  3. Ask for Event time
  4. Ask for Event invitee's email 

- **Primary Postconditions:** 
  1. Email has been sent to all invited attendees
  2. All accepted invitatees will have the event on their calender

- **Alternate Sequence:**
  1. User enters a date that has already passed
     - The system displays error message indicates that the day has already passed
     - The system lets the customer to enter the date again

  2. Invitee rejects Event
     - The system removes invitees from email list


8. Send Task Reminder
- **Pre-condition:** 
  1. User have an account and have logged into their account
  2. User has an upcoming task

- **Trigger:**  
  1. Task remind time is approaching

- **Primary Sequence:**
  1. Task Email is Generated
  2. Send email to all listed members of the task
  3. Repeat for as many event reminders set

- **Primary Postconditions:**  
  1. All attendees will recieve email notification
  2. Mute the email after Task time has passed

- **Alternate Sequence:**
 1. Mute Task reminder
    - remove the user from the reminder


9. Search for email
- **Pre-condition:** 
  1. User have an account and have logged into their account

- **Trigger:**  
  1. User Presses on the 'Inbox' button

- **Primary Sequence:**
  1. User types in the a word or message
  2. User presses enter
  3. Webpage outputs an emails by the search criteria

- **Primary Postconditions:**  
  1. Printed emails

- **Alternate Sequence:**
 1. User decides to leave the page
    - presses the 'Home' button


10. Log out
- **Pre-condition:** 
  1. User have an account and have logged into their account

- **Trigger:**  
  1. User Presses on the 'Log out' button

- **Primary Sequence:**
  1. User presses log out button
  2. User is prompted "You have been logged out."
  3. User is sent to the home page

- **Primary Postconditions:**  
  1. User is on the home page

- **Alternate Sequence:**
 1. User decides that they don't want to log out
    - User can log back in


11. Login
    - **Pre-condition:** 
  1. User is on the landing page

- **Trigger:**  
  1. User Presses on the 'Login' button

- **Primary Sequence:**
  1. User types in the username
  2. User types in the password
  3. User presses the "sign in" button

- **Primary Postconditions:**  
  1. User is on the home page

- **Alternate Sequence:**
 1. User doesn't have an account
    - User presses on the register account


12. Delete Account
    - **Pre-condition:** 
  1. User is on the landing page

- **Trigger:**  
  1. User Presses on the 'Delete' button

- **Primary Sequence:**
  1. Users account is deleted
  2. User is prompted with "Your account is deactivated" 
  3. User is sent to the landing page

- **Primary Postconditions:**  
  1. User is on the landing page

- **Alternate Sequence:**
 1. User decides that they don't want to delete account
    - User can make a new account