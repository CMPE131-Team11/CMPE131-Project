## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. requirement
2. requirement
3. requirement
4. requirement
5. requirement
6. requirement
7. requirement
8. requirement
9. requirement
10. requirement
11. requirement
12. requirement

## Non-functional Requirements

1. non-functional
2. non-functional
3. non-functional
4. non-functional

## Use Cases

1. Create Task
- **Pre-condition:** 
> User have an account and have logged into their account.

- **Trigger:** 
> The user click on the 'Create' button.

- **Primary Sequence:**
  
  1. User navigate to the 'Task' section on the home screen and click on 'Create New Task' button.
  2. System prompts the user to enter the date for the task to be done or due
  3. User enters the date manually on the date bar.
  4. System checks if the date is valid (cannot be before the date of making the task).
  5. User enters a title for the task.
  6. User enters the summary or details of the Task.
  7. System saves the Task.
  8. User close the Task window.

- **Primary Postconditions:** 
  1. The user reveives a message notification indicates the task has been created.
  2. The user can see the task on calendar.

- **Alternate Sequence:**
  
4. User enters a date that has already passed.
> a. The system displays error message indicates that the day has already passed.
> b. The system lets the customer to enter the date again. 


2. Begin Chat
- **Pre-condition:** 
> User have an account and have logged into their account.

- **Trigger:**  
> The user click on the 'Chat' button.

- **Primary Sequence:**
  
  1. User navigates through the home screen and select the chat option.
  2. System prompts a list of contacts.
  3. User selects the name of the contact.
  4. System prompts a chat window.
  5. User enters message in the chat box.
  6. System sends the message to the person of contact. 
  7. User closes the chat window.

- **Primary Postconditions:**  
  1. The user reveives a message notification indicates when the person of contact replies back.
  2. User can see the history of chat.

- **Alternate Sequence:**
  
 3. User cannot find the contact in the list of already existing contacts.
> a. The system allows user to enter the email address of the contact manually.
> b. The system asks user to save the new contact to the list of contacts.
