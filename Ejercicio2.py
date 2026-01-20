import tkinter as tk
from tkinter import scrolledtext, messagebox
import smtplib
from email.mime.text import MIMEText

def enviar_correo():
    host = host_entry.get()
    puerto = int(port_entry.get())
    usuario = user_entry.get()
    password = pass_entry.get()
    remitente = remitente_entry.get()
    destinatario = destinatario_entry.get()
    contenido_html = html_text.get("1.0", tk.END)

    msg = MIMEText(contenido_html, "html")
    msg['Subject'] = "Correo de prueba Python Tkinter"
    msg['From'] = remitente
    msg['To'] = destinatario

    try:
        servidor = smtplib.SMTP(host, puerto)
        servidor.login(usuario, password)
        servidor.send_message(msg)
        servidor.quit()
        log_text.insert(tk.END, "Correo enviado correctamente.\n")
        messagebox.showinfo("Éxito", "Correo enviado correctamente")
    except Exception as e:
        log_text.insert(tk.END, f"Error: {e}\n")
        messagebox.showerror("Error", f"No se pudo enviar el correo.\n{e}")

root = tk.Tk()
root.title("Ejercicio 2 - Enviar correo con Mailtrap")
root.geometry("900x500")

frame_conn = tk.Frame(root)
frame_conn.pack(pady=10)

tk.Label(frame_conn, text="SMTP Host:").grid(row=0, column=0)
host_entry = tk.Entry(frame_conn, width=20)
host_entry.grid(row=0, column=1)
host_entry.insert(0, "sandbox.smtp.mailtrap.io")

tk.Label(frame_conn, text="Puerto:").grid(row=0, column=2)
port_entry = tk.Entry(frame_conn, width=5)
port_entry.grid(row=0, column=3)
port_entry.insert(0, "2525")

tk.Label(frame_conn, text="Usuario:").grid(row=1, column=0)
user_entry = tk.Entry(frame_conn, width=20)
user_entry.grid(row=1, column=1)
user_entry.insert(0, "d38ba0dfce277e")

tk.Label(frame_conn, text="Password:").grid(row=1, column=2)
pass_entry = tk.Entry(frame_conn, width=20, show="*")
pass_entry.grid(row=1, column=3)
pass_entry.insert(0, "bde283f86cd1bd")

tk.Label(frame_conn, text="Remitente:").grid(row=2, column=0)
remitente_entry = tk.Entry(frame_conn, width=20)
remitente_entry.grid(row=2, column=1)
remitente_entry.insert(0, "prueba@example.com")

tk.Label(frame_conn, text="Destinatario:").grid(row=2, column=2)
destinatario_entry = tk.Entry(frame_conn, width=20)
destinatario_entry.grid(row=2, column=3)
destinatario_entry.insert(0, "destino@example.com")

# Panel de texto
frame_text = tk.Frame(root)
frame_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Ventana de HTML (izquierda)
html_text = scrolledtext.ScrolledText(frame_text, width=50)
html_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
html_text.insert(tk.END, "<h1>¡Hola desde Python Tkinter!</h1>\n<p>Fran, estoy vivo.</p>")

# Ventana de log (derecha)
log_text = scrolledtext.ScrolledText(frame_text, width=50)
log_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Botón enviar
send_button = tk.Button(root, text="Enviar correo", command=enviar_correo, bg="green", fg="white")
send_button.pack(pady=10)

root.mainloop()
