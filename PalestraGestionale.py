# Importazione delle librerie necessarie
from abc import ABC, abstractmethod  # Per definire classi astratte
from datetime import datetime, timedelta  # Per gestire date e calcoli temporali

# Classe astratta Cliente, rappresenta un cliente generico
class Cliente(ABC):
    def __init__(self, codice_fiscale, nome, eta, prezzo_mensile, password, corso, tessera):
        # Attributi privati del cliente
        self.__codice_fiscale = codice_fiscale
        self.__nome = nome
        self.__eta = eta
        self.__prezzo_mensile = prezzo_mensile
        self.__password = password
        self.__corso = corso
        self.__tessera = tessera

    # Metodi astratti per ottenere e impostare gli attributi
    @abstractmethod
    def get_codice_fiscale(self): pass
    @abstractmethod
    def set_codice_fiscale(self, codice_fiscale): pass
    @abstractmethod
    def get_nome(self): pass
    @abstractmethod
    def set_nome(self, nome): pass
    @abstractmethod
    def get_eta(self): pass
    @abstractmethod
    def set_eta(self, eta): pass
    @abstractmethod
    def get_prezzo_mensile(self): pass
    @abstractmethod
    def set_prezzo_mensile(self, prezzo): pass
    @abstractmethod
    def get_password(self): pass
    @abstractmethod
    def set_password(self, password): pass
    @abstractmethod
    def get_corso(self): pass
    @abstractmethod
    def set_corso(self, corso): pass
    @abstractmethod
    def get_tessera(self): pass
    @abstractmethod
    def set_tessera(self, tessera): pass

# Classe ClienteStandard, implementa Cliente per clienti standard
class ClienteStandard(Cliente):
    def __init__(self, codice_fiscale, nome, eta, prezzo_mensile, password, corso):
        super().__init__(codice_fiscale, nome, eta, prezzo_mensile, password, corso)
        # Creazione automatica di una tessera associata al cliente
        self.__tessera = Tessera(nome, datetime.today().strftime("%d/%m/%Y"))

    # Implementazione dei metodi astratti
    def get_tessera(self): return self.__tessera
    def set_tessera(self, tessera): self.__tessera = tessera
    def get_codice_fiscale(self): return self.__codice_fiscale
    def set_codice_fiscale(self, codice_fiscale): self.__codice_fiscale = codice_fiscale
    def get_nome(self): return self.__nome
    def set_nome(self, nome): self._nome = nome
    def get_eta(self): return self.__eta
    def set_eta(self, eta): self.__eta = eta
    def get_prezzo_mensile(self): return self.__prezzo_mensile * 12  # Prezzo annuale
    def set_prezzo_mensile(self, prezzo): self.__prezzo_mensile = prezzo
    def get_password(self): return self.__password
    def set_password(self, password): self.__password = password
    def get_corso(self): return self.__corso
    def set_corso(self, corso): self.__corso = corso

# Classe ClientePlus, implementa Cliente per clienti premium con sconto
class ClientePlus(Cliente):
    def __init__(self, codice_fiscale, nome, eta, prezzo_mensile, password, corso):
        super().__init__(codice_fiscale, nome, eta, prezzo_mensile, password, corso)
        self.__tessera = Tessera(nome, datetime.today().strftime("%d/%m/%Y"))

    # Implementazione dei metodi astratti
    def get_tessera(self): return self.__tessera
    def set_tessera(self, tessera): self.__tessera = tessera
    def get_codice_fiscale(self): return self.__codice_fiscale
    def set_codice_fiscale(self, codice_fiscale): self.__codice_fiscale = codice_fiscale
    def get_nome(self): return self.__nome
    def set_nome(self, nome): self.__nome = nome
    def get_eta(self): return self.__eta
    def set_eta(self, eta): self.__eta = eta
    def get_prezzo_mensile(self):
        # Prezzo annuale con sconto del 30%
        annuale = self.__prezzo_mensile * 12
        return annuale * 0.7
    def set_prezzo_mensile(self, prezzo): self.__prezzo_mensile = prezzo
    def get_password(self): return self.__password
    def set_password(self, password): self.__password = password
    def get_corso(self): return self.__corso
    def set_corso(self, corso): self.__corso = corso

# Classe Tessera, rappresenta una tessera associata a un cliente
class Tessera:
    def __init__(self, cliente, data, attiva=True):
        self.__cliente = cliente
        self.__data = data
        self.__attiva = attiva

    # Metodo per verificare lo stato della tessera
    def attivazione(self, data_attuale_str):
        data_attivazione = datetime.strptime(self.__data, "%d/%m/%Y")
        data_attuale = datetime.strptime(data_attuale_str, "%d/%m/%Y")
        data_scadenza = data_attivazione + timedelta(days=365)

        if data_attuale > data_scadenza:
            self.__attiva = False
            print(f"La tessera di {self.__cliente} è SCADUTA il {data_scadenza.strftime('%d/%m/%Y')}.")
        else:
            self.__attiva = True
            print(f"La tessera di {self.__cliente} è ATTIVA. Scadrà il {data_scadenza.strftime('%d/%m/%Y')}.")
        return self.__attiva

    # Getter e setter per gli attributi della tessera
    def is_attiva(self): return self.__attiva
    def set_attiva(self, attiva): self.__attiva = attiva
    def get_data(self): return self.__data
    def set_data(self, data): self.__data = data
    def get_cliente(self): return self.__cliente
    def set_cliente(self, cliente): self.__cliente = cliente

# Classe Admin, gestisce i clienti e le loro tessere
class Admin:
    def __init__(self):
        self.clienti = []  # Lista dei clienti registrati

    # Metodo per aggiungere un cliente
    def aggiungi_cliente(self, cliente: Cliente):
        self.clienti.append(cliente)
        print("Cliente aggiunto correttamente.")

    # Metodo per calcolare e mostrare gli sconti mensili
    def sconti_clienti(self):
        mese_corrente = datetime.now().strftime("%b")  # Mese corrente
        print(f"\nMese corrente: {mese_corrente}")

        # Prezzi scontati per corso e mese
        prezzi_scontati = {
            "Pilates": {"Gen": 35, "Feb": 35, "Mar": 35},
            "Yoga": {"Apr": 35, "Mag": 35, "Giu": 35},
            "Gym": {"Lug": 35, "Ago": 35, "Set": 35},
            "Karate": {"Ott": 40, "Nov": 40, "Dic": 40}
        }

        for cliente in self.clienti:
            corso = cliente.get_corso()
            prezzo_base = cliente.get_prezzo_mensile() / 12  # Prezzo mensile stimato

            if corso in prezzi_scontati and mese_corrente in prezzi_scontati[corso]:
                prezzo_scontato = prezzi_scontati[corso][mese_corrente]
                print(f"\nCliente: {cliente.get_nome()} ({corso})")
                print(f"Prezzo normale: €{prezzo_base:.2f}")
                print(f"Prezzo scontato per {mese_corrente}: €{prezzo_scontato:.2f}")
            else:
                print(f"\nCliente: {cliente.get_nome()} ({corso})")
                print(f"Nessuno sconto per il mese di {mese_corrente}. Prezzo: €{prezzo_base:.2f}")

    # Metodo per verificare lo stato della tessera di un cliente
    def verifica_tessera(self, cliente_cf):
        for cliente in self.clienti:
            if cliente.get_codice_fiscale() == cliente_cf:
                tessera = cliente.get_tessera()
                return tessera.attivazione(datetime.today().strftime("%d/%m/%Y"))
        return False

    # Metodo per modificare i dati di un cliente
    def modifica_cliente(self):
        codice = input("Codice fiscale del cliente da modificare: ")
        for cliente in self.clienti:
            if cliente.get_codice_fiscale() == codice:
                print(f"Modifica cliente: {cliente.get_nome()}")
                print("1. Nome\n2. Età\n3. Prezzo Mensile\n4. Codice Fiscale\n5. Password\n6. Corso\n7. Attiva/Disattiva Tessera")
                scelta = input("Scelta (1-7): ")
                match scelta:
                    case "1":
                        cliente.set_nome(input("Nuovo nome: "))
                    case "2":
                        cliente.set_eta(int(input("Nuova età: ")))
                    case "3":
                        cliente.set_prezzo_mensile(float(input("Nuovo prezzo mensile: ")))
                    case "4":
                        cliente.set_codice_fiscale(input("Nuovo codice fiscale: "))
                    case "5":
                        cliente.set_password(input("Nuova password: "))
                    case "6":
                        cliente.set_corso(input("Nuovo corso: "))
                    case "7":
                        tessera_attiva = self.verifica_tessera(codice)
                        if tessera_attiva:
                            scelta = input("La tessera è attiva. Vuoi disattivarla? (s/n): ")
                            if scelta.lower() == "s":
                                cliente.get_tessera().set_attiva(False)
                                print("Tessera disattivata.")
                        else:
                            scelta = input("La tessera è disattiva. Vuoi attivarla manualmente? (s/n): ")
                            if scelta.lower() == "s":
                                cliente.get_tessera().set_attiva(True)
                                print("Tessera attivata.")
                    case _:
                        print("Scelta non valida.")
                print("Modifica completata.")
                return
        print("Cliente non trovato.")

    # Metodo per stampare i dettagli di tutti i clienti
    def stampa_clienti(self):
        if not self.clienti:
            print("Nessun cliente registrato.")
            return

        for cliente in self.clienti:
            tipo = "Plus" if isinstance(cliente, ClientePlus) else "Standard"
            print(f"Tipo: {tipo}")
            print(f"Codice Fiscale: {cliente.get_codice_fiscale()}")
            print(f"Nome: {cliente.get_nome()}")
            print(f"Età: {cliente.get_eta()}")
            print(f"Prezzo annuale: €{cliente.get_prezzo_mensile():.2f}")
            print(f"Corso: {cliente.get_corso()}")
            print(f"Tessera attiva: {cliente.get_tessera().is_attiva()}")
            print("-" * 30)

# Decoratore per validare input di codice fiscale e password
def verifica_input(funzione):
    def wrapper(admin):
        while True:
            codice = input("Codice fiscale (16 caratteri): ")
            if len(codice) != 16:
                print(" Codice fiscale non valido. Deve contenere esattamente 16 caratteri.")
                continue

            password = input("Password (almeno 9 caratteri): ")
            if len(password) < 8:
                print(" Password troppo corta. Deve contenere almeno 9 caratteri.")
                continue

            # Passaggio ai parametri della funzione
            return funzione(admin, codice, password)
    return wrapper

# Funzione per registrare un nuovo cliente
@verifica_input
def registrazione(admin, codice, password):
    nome = input("Nome: ")
    eta = int(input("Età: "))
    prezzo = float(input("Prezzo mensile: "))
    corso = input("Corso (Yoga/Gym/Pilates): ")
    tipo = input("Tipo cliente (standard/plus): ").lower()

    if tipo == "plus":
        cliente = ClientePlus(codice, nome, eta, prezzo, password, corso)
    else:
        cliente = ClienteStandard(codice, nome, eta, prezzo, password, corso)

    admin.aggiungi_cliente(cliente)

# Funzione per il login di un cliente
@verifica_input
def login(admin, codice, password):
    for cliente in admin.clienti:
        if cliente.get_codice_fiscale() == codice and cliente.get_password() == password:
            if admin.verifica_tessera(codice):
                print(f"Benvenuto, {cliente.get_nome()}!")
                return cliente
            else:
                print("La tua tessera è scaduta.")
                return None
    print("Cliente non trovato. Procedo con registrazione.")
    registrazione(admin)

# Menu per l'amministratore
def menu_admin(admin):
    while True:
        print("\n--- Menu Admin ---")
        print("1. Aggiungi Cliente")
        print("2. Modifica Cliente")
        print("3. Verifica Tessera Cliente")
        print("4. Visualizza Tutti i Clienti")
        print("5. Visualizza sconti del mese per i clienti")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                registrazione(admin)
            case "2":
                admin.modifica_cliente()
            case "3":
                cf = input("Inserisci il codice fiscale del cliente: ")
                admin.verifica_tessera(cf)
            case "4":
                admin.stampa_clienti()
            case "5":
                admin.sconti_clienti()
            case "0":
                print("Uscita dal menu Admin.")
                break
            case _:
                print("Scelta non valida.")

# Menu per il cliente
def menu_cliente(admin):
    while True:
        print("\n--- Menu Utente ---")
        print("1. Aggiungi Registrazione")
        print("2. Login")
        print("3. Verifica Tessera Cliente")
        print("4. Visualizza sconti del mese per i clienti")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                registrazione(admin)
            case "2":
                login(admin)
            case "3":
                cf = input("Inserisci il codice fiscale del cliente: ")
                admin.verifica_tessera(cf)
            case "4":
                admin.sconti_clienti()
            case "0":
                print("Uscita dal menu Utente.")
                break
            case _:
                print("Scelta non valida.")

# Funzione principale dell'applicazione
def app():
    admin = Admin()  # Creazione dell'oggetto Admin
    while True:
        scelta = int(input("Seleziona la tua opzione \n1. ADMIN\n2. UTENTE\n0. Esci\n> "))

        match scelta:
            case 1:
                menu_admin(admin)
            case 2:
                menu_cliente(admin)
            case 0:
                print("--- USCITA DAL SISTEMA ---")
                break
            case _:
                print("Scelta non valida.")

# Avvio dell'applicazione
app()