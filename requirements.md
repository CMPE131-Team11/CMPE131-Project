## Functional Requirements
1. Register Account
2. Edit User Profile
3. Send email
4. Create Task
5. begin chat
6. send chat message
7. delete email
8. add event
9. send event reminder
10. search for email
11. log out
12. login

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

4.  Add images to email
- **Pre-condition:**
  1. The user is already logged in, user is currently composing an email, and has the image URL

- **Trigger:**
  1. User presses enter image button 

- **Primary Sequence:**
  1. User is presented with a popup of screen
  2. User inputs/pastes their URL of the image that they’ll like to input
  3. User presses the insert button

- **Primary Postconditions:** 
  1. User sees their image on the composing email

- **Alternate Sequence:**  
  1. The URL that they imputed is not valid	
      - The user is prompted with an error message
      - System prompts "Invalid URL"

5. Create Task
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


6. Begin Chat
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