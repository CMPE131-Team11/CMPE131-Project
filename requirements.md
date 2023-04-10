## Functional Requirements

1. send email
2. make account
3. login
4. add event
5. begin chat
6. open existing chat
7. delete email
8. create task
9. send task reminder
10. search for email
11. block email
12. log out

## Non-functional Requirements

1. non-functional
2. non-functional
3. non-functional
4. non-functional

## Use Cases

1. Register Account

- **Trigger:** A first-time user enters our application or a user clicks on the ‘register account’ button


- **Primary Sequence:**
  
  1. The user clicks the register account button
  2. Enters a valid User Name
  3. Enters a valid password
  4. Enters First and Last Name
  5. Clicks register button


- **Primary Postconditions:** The user is logged in to their account and can do anything a signed-in user can do


- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. A user enters an invalid username or password
  2. System response with invalid username or password and reason why it’s invalid
  3. The user re-enters a valid username and password


2. Edit User Profile

- **Trigger:** User clicks on ‘Edit Profile’ button


- **Primary Sequence:**
  
  1. User clicks ‘edit profile’ button
  2. User makes all desired edits
  3. User clicks ‘Save button’
  4. User clicks ‘Exit Profile’ button


- **Primary Postconditions:** All edited changes are applied to the User



- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. User clicks ‘Exit’ before ‘Save’ button
  2. System sends alert saying ‘Do you want to sasve changes’
  3. Systems saves changes depending on User’s answers

3. Send email
- **Pre-condition:** <can be a list or short description> User is logged in.

- **Trigger:** <can be a list or short description> User presses compose button. 

- **Primary Sequence:**
  
  1. User types recipient name(s) 
  2. User writes the subject
  3. User writes the message they want to send
  4. User presses the "Send" button 
  5. System prompts the user with a date box and a time box 
  6. User inputs the date and time into respective boxes
  7. User presses the "Schedule send" button
  8. User is sent to the homescreen

- **Primary Postconditions:** <can be a list or short description> System displays “message has been sent".

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise> 
  Recipient names are not in the system	
      a) System displays error
      b) System prompts “Invalid Recipient name(s)”

  User inputs an invalid schedule time 
      a) System displays error
      b) System prompts Invalid schedule time ”

4.  Add images to email
- **Pre-condition:** <can be a list or short description> The user is already logged in, user is currently composing an email, and has the image URL

- **Trigger:** <can be a list or short description> User presses enter image button 

- **Primary Sequence:**
  
  1. User is presented with a popup of screen
  2. User inputs/pastes their URL of the image that they’ll like to input
  3. User presses the insert button

- **Primary Postconditions:** <can be a list or short description> User sees their image on the composing email

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise> 
  The URL that they imputed is not valid	
      a) The user is prompted with an error message
      b) System prompts "Invalid URL"
