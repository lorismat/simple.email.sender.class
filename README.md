# A very simple email sender

**Goal of this project** is to draft a very minimalist email sender class.  
This project is not packaged, nor installed on PyPI. To see a finished project that you can `pip install` from the terminal, check out my [get.comics.anywhere repository](https://github.com/lorismat/get.comics.anywhere).  

The class is called `sender.py`. The `example.py` is an illustration on how to use it.  

Below are some documentation I've used on the way, not relevant required to use the class.  

## General Doc on SMTP

**Simple Mail Transfer Protocol**  

The SMTP server has an address. This address is specific to the service you are using (gmail address: `smtp.gmail.com`).  

The recipient’s inbox service provider, like `gmail` will download your message and place it in the inbox.  

The server goals are exclusively to: send, receive, and relay emails. These servers are constantly running.  

The SMTP server takes care of protecting you from illegitimate emails and will send you back the email if the recipient's address does not exist.  

**Use cases:**  
- Send emails from your website
- Schedule mass emails easily

**Beware!**
- SMTP cannot transfer email attachments! _Multipurpose Internet Mail Extension_ (MIME) protocol is a workaround for this. MIME encodes all non-text data into text before sending the email through SMTP.

## `smtplib` doc

- [smtplib doc](https://docs.python.org/3/library/smtplib.html)  

## Sources

- [What is SMTP](https://sendgrid.com/blog/what-is-an-smtp-server/)
- [Setting up Gmail SMTP](https://www.gmass.co/blog/gmail-smtp/)

## Alternatives: use with `flask`

- [Flask mails](https://flask-mail.readthedocs.io/en/latest/)

## Working with classes

- [15min video about Object-Oriented Programming](https://youtu.be/pnWINBJ3-yA)
