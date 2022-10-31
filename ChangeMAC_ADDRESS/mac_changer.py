#va a funcionar en dispositivos Linux
from ast import arguments
import subprocess #Correr comandos
import optparse #Crear comandos

parser=optparse.OptionParser()  # vincular comandos con interfaz
parser.add_option("-i", "--interface", dest ="interface", help="Interfaz para cambiar dirección MAC")
parser.add_option("-m", "--mac", dest ="new_mac", help="Nueva dirección MAC")

(options, arguments) =parser.parse_args()

interface = input("interface >")
new_mac = input("new MAC >")

print("[+] Cambiando Direccion MAC para" + interface + " to"  + new_mac)

#subprocess.call("ifconfig" + interface + " down", shell=True)                  Poco seguro
#subprocess.call("ifconfig" + interface + " hw ether" + new_mac, shell=True)    Poco seguro
#subprocess.call("ifconfig" + interface + " up", shell=True)                    Poco seguro

interface = options.interface
new_mac = options.new_mac

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

