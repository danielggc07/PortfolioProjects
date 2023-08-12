import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pdfrw
from PyPDF2 import PdfReader, PdfWriter
import PyPDF2
import win32com.client as win32

# Initialize the new_customer value
new_customer = input("Enter new customer name: ")

while True:
    # Collect Input
    person_to_reach_name = input("Enter person to reach name: ")
    company_of_person_to_reach = input("Enter company of person to reach: ")
    person_to_reach_email = input("Enter person to reach email: ")

    # Split the person's name into first name and last name
    if person_to_reach_name:
        names = person_to_reach_name.split()

        if len(names) == 1:
            first_name = names[0]
            last_name = ""
        else:
            first_name = names[0]
            last_name = " ".join(names[1:])
    else:
        first_name = ""
        last_name = ""

    # Fill PDF
    pdf_template = "Request for Credit Reference.pdf"
    pdf_output = f"Request for Credit Reference for {new_customer}.pdf"

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Open the template PDF file
    with open(pdf_template, "rb") as template_file:
        pdf_reader = PyPDF2.PdfFileReader(template_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Fill in the fields
        page = pdf_reader.pages[0]
        pdf_writer.add_page(page)
        pdf_writer.updatePageFormFieldValues(page, {
            "Date": current_date,
            "PersonToReachName": person_to_reach_name,
            "CompanyOfPersonToReach": company_of_person_to_reach,
            "NewCustomerName": new_customer
        })

        # Save the filled PDF to a new file
        with open(pdf_output, "wb") as output_file:
            pdf_writer.write(output_file)

    print(f"Filled PDF saved as '{pdf_output}'")

    # Email Generation
    email_subject = f"Request for Credit Reference for {new_customer}"
    email_greeting = f"Hello {first_name}," if first_name else "Hello,"
    email_body = f"""
    <html>
    <body>
        {email_greeting}<br><br>
        We received a credit application from {new_customer} that listed {company_of_person_to_reach} as a credit reference.
        Could you please provide us with a credit reference for them?<br><br>
        Your prompt attention to this matter would be appreciated. Let me know if you have any questions or require additional information.<br><br>
        Thank you for your assistance.<br><br>
        <strong>Daniel Guevara</strong> | Accountant/Credit Analyst<br>

    </body>
    </html>
    """

    signature_image = 'Picture1.png'

    # Create the Outlook COM object
    outlook = win32.Dispatch('Outlook.Application')

    # Send Email
    email_user = os.environ.get('EMAIL_USER')
    email_password = os.environ.get('EMAIL_PASSWORD')
    receiver_email = person_to_reach_email

    # Create an email item
    mail = outlook.CreateItem(0)
    mail.Subject = email_subject
    mail.HTMLBody = email_body 
    mail.To = receiver_email

    # Attach the PDF file
    attachment = os.path.abspath(pdf_output)
    mail.Attachments.Add(attachment)

    # Attach the signature image as an embedded image
    signature_path = os.path.abspath(signature_image)
    signature_cid = 'signature_image'
    attachment = mail.Attachments.Add(signature_path, 0, len(email_body), signature_cid)
    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001E", signature_cid)

    # Send the email
    try:
        mail.Send()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    repeat = input("Do you want to request another credit reference for the same customer? (Y/N): ")
    if repeat.lower() != 'y':
        break