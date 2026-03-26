"""
FOOTBALL BOT - MAIN
Esegue l'analisi delle partite
"""

from regole import RegoleBot

def analizza_partita(partita_data):
    """Analizza una singola partita"""
    bot = RegoleBot()
    risultato = bot.analizza(partita_data)
    
    print(f"\n📊 ANALISI: {partita_data.get('nome', 'Partita')}")
    print("-" * 40)
    
    if risultato['allarmi'] == 0:
        print("✅ TUTTE LE REGOLE SUPERATE")
        print("🎯 PRONOSTICO CONSIGLIATO: Vittoria del favorito o Under 2.5")
    else:
        print(f"⚠️ {risultato['allarmi']} ALLARMI RILEVATI")
        for r in risultato['esiti']:
            print(r)
    
    return risultato

def inserisci_manuale():
    """Inserimento manuale dei dati"""
    print("\n" + "="*50)
    print("FOOTBALL BOT - Inserisci i dati della partita")
    print("="*50)
    
    partita = {
        'nome': input("Nome partita: "),
        'campionato': input("Campionato: "),
        'quota_1': float(input("Quota 1: ")),
        'sconfitte_consecutive': int(input("Sconfitte consecutive squadra favorita (0 se nessuna): ")),
        'scontro_diretto': input("Scontro diretto per obiettivo importante? (s/n): ").lower() == 's',
        'infortuni_titolari': int(input("Infortuni titolari squadra favorita (0 se nessuno): ")),
        'grande_occasione': input("Pressione da grande occasione? (s/n): ").lower() == 's',
        'crisi_e_goleada': input("Squadra reduce da goleada? (s/n): ").lower() == 's',
        'nuovo_allenatore': input("Nuovo allenatore al debutto? (s/n): ").lower() == 's',
        'salvezza_trasferta': input("Squadra in lotta salvezza in trasferta? (s/n): ").lower() == 's',
    }
    
    return partita

if __name__ == "__main__":
    print("FOOTBALL BOT - Versione 1.0")
    print("25 regole attive\n")
    
    while True:
        partita = inserisci_manuale()
        analizza_partita(partita)
        
        continua = input("\nAnalizzare un'altra partita? (s/n): ").lower()
        if continua != 's':
            break
    
    print("\nGrazie per aver usato Football Bot! 💪")
