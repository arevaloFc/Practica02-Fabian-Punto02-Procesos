import subprocess

p = subprocess.run(['ping','-c2','www.google.com'], universal_newlines=True, stdout=subprocess.PIPE)
response = p.stdout

lineas = response.split('\n') 

print("Lineas --" , lineas)

print(type(response))