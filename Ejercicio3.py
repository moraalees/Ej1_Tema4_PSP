import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import ntplib
from datetime import datetime

# --- Funciones DNS ---
def dns_nombre_a_ip():
    nombre = dns_entry.get()
    try:
        ip = socket.gethostbyname(nombre)
        dns_log.insert(tk.END, f"{nombre} → {ip}\n")
    except Exception as e:
        dns_log.insert(tk.END, f"❌ Error: {e}\n")

def dns_ip_a_nombre():
    ip = dns_entry.get()
    try:
        nombre = socket.gethostbyaddr(ip)[0]
        dns_log.insert(tk.END, f"{ip} → {nombre}\n")
    except Exception as e:
        dns_log.insert(tk.END, f"❌ Error: {e}\n")

# --- Función NTP ---
def consultar_ntp():
    ntp_host = ntp_entry.get()
    try:
        cliente = ntplib.NTPClient()
        respuesta = cliente.request(ntp_host, version=3)
        hora = datetime.fromtimestamp(respuesta.tx_time)
        ntp_log.insert(tk.END, f"Hora NTP ({ntp_host}): {hora}\n")
    except Exception as e:
        ntp_log.insert(tk.END, f"❌ Error: {e}\n")

# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("NetworkLab - DNS y NTP")
root.geometry("1000x500")

# --- DNS Frame ---
frame_dns = tk.LabelFrame(root, text="DNS", padx=10, pady=10)
frame_dns.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(frame_dns, text="Nombre/IP:").pack()
dns_entry = tk.Entry(frame_dns, width=30)
dns_entry.pack(pady=5)

btn_nombre_ip = tk.Button(frame_dns, text="Nombre → IP", command=dns_nombre_a_ip)
btn_nombre_ip.pack(pady=5)

btn_ip_nombre = tk.Button(frame_dns, text="IP → Nombre", command=dns_ip_a_nombre)
btn_ip_nombre.pack(pady=5)

dns_log = scrolledtext.ScrolledText(frame_dns, width=50)
dns_log.pack(fill=tk.BOTH, expand=True, pady=5)
dns_log.insert(tk.END, "Logs DNS:\n")

# --- NTP Frame ---
frame_ntp = tk.LabelFrame(root, text="NTP", padx=10, pady=10)
frame_ntp.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(frame_ntp, text="Servidor NTP:").pack()
ntp_entry = tk.Entry(frame_ntp, width=30)
ntp_entry.pack(pady=5)
ntp_entry.insert(0, "pool.ntp.org")  # Servidor NTP público

btn_ntp = tk.Button(frame_ntp, text="Consultar Hora NTP", command=consultar_ntp)
btn_ntp.pack(pady=5)

ntp_log = scrolledtext.ScrolledText(frame_ntp, width=50)
ntp_log.pack(fill=tk.BOTH, expand=True, pady=5)
ntp_log.insert(tk.END, "Logs NTP:\n")

root.mainloop()