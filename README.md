# GymManager

Un sistema di gestione per clienti di una palestra, scritto in Python con un approccio orientato agli oggetti. Il programma gestisce registrazione, login, tessere annuali, corsi, sconti stagionali e la distinzione tra clienti standard e clienti plus.

## Funzionalità principali

- **Registrazione clienti (Standard/Plus)** con controllo di input
- **Login clienti** con verifica tessera
- **Gestione corsi** (Yoga, Gym, Pilates, Karate)
- **Sconti mensili** in base al tipo di corso
- **Sistema tessera annuale** con scadenza e stato attivo/disattivo
- **Visualizzazione e modifica dati clienti**
- **Interfaccia admin separata dall'interfaccia cliente**

## Struttura del Progetto

```text
├── main.py              # Avvio dell'app con menu Admin/Utente
├── README.md            # Questo file
```

  Il progetto è contenuto in un singolo file Python per semplicità, ma è strutturato per poter essere facilmente modulare.

## Classi Principali

  - **Cliente (astratta)**

  - **ClienteStandard**

  - **ClientePlus (30% sconto annuale)**

  - **Tessera**

  - **Admin**

## Come usare il programma
**Requisiti**

- Python 3.10 o superiore

- Esecuzione

- python main.py

**Modalità disponibili**

  Admin: può registrare/modificare clienti, visualizzare tutti i dati, vedere gli sconti mensili.

  Utente: può registrarsi, effettuare login, verificare lo stato della propria tessera, consultare gli sconti del mese.

## Sicurezza

  Il codice fiscale deve essere lungo 16 caratteri

  La password deve essere di almeno 9 caratteri

## Sistema Tessera

Ogni cliente riceve una tessera annuale alla registrazione. La tessera scade dopo 365 giorni dalla data di attivazione. Il sistema verifica automaticamente la validità della tessera al login.
## Sconti stagionali

Gli sconti variano in base al **corso** e al **mese corrente**. Ecco un **esempio**:
```
Corso | Mesi con Sconto | Prezzo scontato
Yoga | Apr, Mag, Giu | €35
Pilates | Gen, Feb, Mar | €35
Gym | Lug, Ago, Set | €35
Karate | Ott, Nov, Dic | €40
```

# Esempio d’uso

Seleziona la tua opzione:
```
1. ADMIN
2. UTENTE
0. Esci
> 1

--- Menu Admin ---
1. Aggiungi Cliente
2. Modifica Cliente
3. Verifica Tessera Cliente
4. Visualizza Tutti i Clienti
5. Visualizza sconti del mese per i clienti
0. Esci
```
*Autore: Giacomo Visciotti-Giuseppe Del Vecchio*

