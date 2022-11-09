from cryptography.fernet import Fernet
import os

def retornarKey():
    return open("key.key","rb").read()

def decryp(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.decrypt(file_data)
        
        with open(x,"wb") as file:
            file.write(data)

if __name__ == "__main__":
    
    archivos = 'Users\\javiercestinourdiales\\Desktop\\Ataque' #Ubicación de los archivos
    os.remove(archivos+"\\"+"README.txt")
    items = os.listdir(archivos)
    archivos_2 = [archivos+"\\"+ x for x in items]
    


key = retornarKey()

decryp(archivos_2, key)

