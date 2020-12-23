from sender import email_sender 

# initializing the object with the smtp config
# working with smtp.gmail.com? Make sure to enable "less-secure" applications in your google settings
my_sender = email_sender("smtp.gmail.com",587,"example@gmail.com","<your-password>")

# writting both html and css (optional)
html = """
<h1>Hey!</h1>
"""
css = """
h1 {
    font-weight:bold;
    color: #999;
}
"""

# calling the send method to send the message
my_sender.send("<sender>","<recipient>","<subject>",html,css)
