import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_correo(df, region):
    # Configurar los detalles del correo electrónico
    fromaddr = "angel.alzamora.flores.1@gmail.com"
    toaddr = "angel.alzamora.flores.1@gmail.com"
    password = "gbig rjjf qaik qlaf"

    # Crear el objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configurar los parámetros del mensaje
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = f"Reporte Top 5 de Costo de Inversión para la región {region}"

    # Adjuntar el DataFrame como un archivo CSV al correo electrónico
    filename = f"top5_costo_inversion_{region}.xlsx"
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(open(filename, "rb").read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename= {filename}')
    msg.attach(attachment)

    # Iniciar sesión en el servidor SMTP y enviar el correo electrónico
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
