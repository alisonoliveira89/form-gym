from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Função para enviar email
def send_email(to_mail, subject, body, cc_mail):
    from_email = "alison.oliveira89@gmail.com"  # Seu email
    from_password = "waod nmdx fmli tvni"  # Senha de aplicativo gerada no Google

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_mail
    msg["Cc"] = cc_mail

     # Corpo do email
    msg.attach(MIMEText(body, "plain"))

    # Lista de destinatários: principal (to_email) + CC (user_email)
    recipients = [to_mail, cc_mail]

    # Configurar o servidor SMTP do Gmail
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_email, from_password)
    server.sendmail(from_email, recipients, msg.as_string())
    server.quit()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/send-email', methods=['POST'])
def send_email_route():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    gender = request.form['gender']
    exercise = request.form['exercise']
    meals = request.form['meals']
    not_eat = request.form['notEat']
    wake_up_time = request.form['wakeUpTime']
    sleep_time = request.form['sleepTime']
    medication = request.form['medication']
    anabolic = request.form['anabolic']
    routine = request.form['routine']

    # Construindo o conteúdo do email com os dados do formulário
    body = f"""
    Nome: {name}
    E-mail: {email}
    Idade: {age}
    Sexo: {gender}
    Pratica atividade física: {exercise}
    Quantas refeições faz por dia: {meals}
    O que não come: {not_eat}
    Horário que costuma acordar: {wake_up_time}
    Horário que costuma dormir: {sleep_time}
    Usa algum tipo de medicação: {medication}
    Usa ou já usou anabolizante: {anabolic}
    Rotina diária: {routine}
    """

    # Enviando email
    send_email("alison.oliveira89@gmail.com", "Dados do Formulário de Rotina", body, email)

    # Redireciona para a página de sucesso
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
