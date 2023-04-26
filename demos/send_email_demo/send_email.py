from email_obj.email_obj import Send_email

samp = Send_email()


samp.add_recipient('carlos.rojas@sjsu.edu')

samp.set_body_text('Hello')

samp.set_subject_text('This is subject')

samp.send()
