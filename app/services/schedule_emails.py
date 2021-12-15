import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime as dt, timedelta
from os import getenv
from flask import app
from app.models.sessions_model import Sessions
from app.models.customers_model import Customers
from sqlalchemy import and_
from app.models.therapists_model import Therapists



def sending_mails(send_to: str, data:str, hour:str, therapist:str):
    host = "smtp.gmail.com"
    port = 587
    username = str(getenv('EMAIL_USERNAME'))
    password = str(getenv('EMAIL_PASSWORD'))

    
    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()
    server.login(username, password)


    corpo  = f"""
    <html>

    <div>
    <h1 style="color: rgba(38,140,187,1); margin: 20px auto; text-transform: capitalize">Lembrete de Consulta</h1>
    <p style="color: rgba(38,140,187,1); cont-sieze 16px; margin: 20px auto">Consulta marcada para o dia {data} com o terapeuta {therapist} as {hour} hrs</p>
    <p style="color: rgba(38,140,187,1); font-size: 15px; margin: 20px auto; width:100%">Esperamos você, até breve.</p>
    <footer>
    <p style="color: rgba(38,140,187,1); font-size: 8px; margin: 20px auto; width:100%">Espaço Terapêutico Bem Viver</p>
    </footer
    </div>
    </html>
    """
    email_msg = MIMEMultipart()
    email_msg['From'] = username
    email_msg['To'] = send_to
    email_msg['Subject'] = "Aviso de consulta"
    email_msg.attach(MIMEText(corpo, 'html'))

    caminho = "/home/waldiney/Documentos/Livros/git-cheat-sheet.pdf"
    anexo = open(caminho, 'rb')

    anx = MIMEBase('application', 'octet-stream')
    anx.set_payload(anexo.read())
    encoders.encode_base64(anx)

    anx.add_header('Content-Disposition', f'attachment; filename={caminho}')
    anexo.close()
    email_msg.attach(anx)


    server.sendmail(username, email_msg['To'], email_msg.as_string())

    server.quit()



def get_appointments_emails(session_id):
    
    appointments = Sessions.query.filter_by(id_session=session_id).first()
    
    if not appointments:
        return False
    
    therapist = Therapists.query.filter_by(id_therapist=appointments.id_therapist).first()
    customer = Customers.query.filter_by(id_customer=appointments.id_customer).first()
    data_inicial = appointments.dt_start.strftime("%d/%m/%Y")
    hora_consulta = appointments.dt_start.strftime("%H:%M:%S")
    sending_mails(customer.ds_email, data_inicial, hora_consulta, therapist.nm_therapist)
    
        
    return True