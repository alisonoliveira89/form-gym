from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Função para enviar email
def send_email(to_email, subject, body):
    from_email = "alison.oliveira89@gmail.com"  # Seu email
    from_password = "waod nmdx fmli tvni"  # Senha de aplicativo gerada no Google

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    # Configurar o servidor SMTP do Gmail
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/send-email', methods=['POST'])
def send_email_route():
    name = request.form['name']
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
    email_body = f"""
    Nome: {name}
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
    send_email("destinatario@exemplo.com", "Dados do Formulário de Rotina", email_body)

    # Redireciona para a página de sucesso
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
