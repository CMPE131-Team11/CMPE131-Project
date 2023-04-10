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

1. Send email
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

2.  Add images to email
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
