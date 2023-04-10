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

