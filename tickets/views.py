from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_tickets(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Generate the PDF ticket (replace this with your actual PDF generation logic)
        pdf_file = generate_pdf_ticket()

        # Send the email with the PDF attachment
        email_subject = 'Your Tickets'
        email_message = 'Please find your tickets to the RE-AWAKENING: Halloween Festival attached.'
        email_from = 'edemgold2406@gmail.com'  # Replace with your email
        email_to = [email]

        email = EmailMessage(email_subject, email_message, email_from, email_to)
        email.attach('ticket.pdf', pdf_file, 'application/pdf')
        email.send()

        return render(request, 'tickets/success_popup.html')  # Render the success pop-up template

    return render(request, 'tickets/tickets.html')

def generate_pdf_ticket():
    # Generate the PDF using ReportLab (replace this with your actual PDF generation logic)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "This is your pass to the Halloween Festival. Have fun and stay safe!")
    p.showPage()
    p.save()
    return response
