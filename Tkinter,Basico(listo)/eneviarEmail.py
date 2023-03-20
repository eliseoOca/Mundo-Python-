import smtplib

def enviar(remitente, destinatario, mensaje):
    usuario= remitente
    password = 'josecodetech12'
    try:
        conexion= smtplib.SMTP('mstp.gmail.com', 587)
        conexion.starttls()
        conexion.login(usuario,password)
        print("Login correcto")
        conexion.sendmail(remitente, destinatario, mensaje)
        print("email enviado correctamente")
        conexion.quit
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticacion")
        
if __name__== "__main__":
    enviar("josecodetech@gmail.com","josecodetech@gmail.com",
           "Hola, prueba desde Python")