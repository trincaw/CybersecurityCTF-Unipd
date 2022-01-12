import base64
decoded = base64.b64decode('Q2Flc2FyCg==').decode('ascii')
print(decoded)