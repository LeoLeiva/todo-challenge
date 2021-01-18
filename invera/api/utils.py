import io
import csv
import logging

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.utils import timezone

logger = logging.getLogger('__name__')


def send_test_csv_report(test_results, recipients):
       # response content type
    response = HttpResponse(content_type='text/csv')

    #decide the file name
    response['Content-Disposition'] = 'attachment; filename="test_csv_report.csv"'

    filename = "test_csv_report.csv"
    string = io.StringIO()
    csv_writer = csv.writer(
        string, 
        delimiter=',', 
        quotechar='"', 
        quoting=csv.QUOTE_MINIMAL
    )

    csv_writer.writerow([
        'S.No', 
        'Test Name', 
        'Test Result', 
        'Test Description'
    ])

    for result_index, result in enumerate(test_results):
        csv_writer.writerow([
            result_index + 1, 
            result['test_name'], 
            result['result'],
            result['test_description']
        ])
    

    email = EmailMultiAlternatives(
        subject=str(timezone.now().strftime("%d-%m-%Y")) + ' ' +     'Test Results' + " CSV report",
        from_email='email@origen.com',
        to=recipients
    )
    email.attach(
        filename=filename, 
        mimetype="text/csv", 
        content=string.getvalue()
    )
    email.send()

    logger.info('Email Sent Successfully!!')
    return response