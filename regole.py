
"""
FOOTBALL BOT - MOTORE DELLE REGOLE
"""

import json

class RegoleBot:
    
    def __init__(self):
        self.carica_regole()
        self.allarmi = []
    
    def carica_regole(self):
        try:
            with open('regole.json', 'r') as f:
                data = json.load(f)
                self.regole = data['regole']
        except:
            self.regole = []
    
    def analizza(self, partita):
        self.allarmi = []
        
        for regola in self.regole:
            if self._verifica_condizione(regola['condizione'], partita):
                self.allarmi.append(regola['messaggio'])
        
        return {
            'allarmi': self.allarmi,
            'totale_allarmi': len(self.allarmi)
        }
    
    def _verifica_condizione(self, condizione, partita):
        valori = {
            'quota_1': partita.get('quota_1', 10),
            'scontro_diretto': partita.get('scontro_diretto', False),
            'grande_occasione': partita.get('grande_occasione', False),
            'salvezza_trasferta': partita.get('salvezza_trasferta', False),
            'sconfitte_consecutive': partita.get('sconfitte_consecutive', 0),
            'infortuni_titolari': partita.get('infortuni_titolari', 0),
            'vittorie_consecutive': partita.get('vittorie_consecutive', 0),
            'attacco_scarso': partita.get('attacco_scarso', False),
            'post_coppa': partita.get('post_coppa', False),
            'nuovo_allenatore': partita.get('nuovo_allenatore', False),
            'campionato': partita.get('campionato', ''),
            'forma_A_cattiva': partita.get('forma_A', '').count('S') >= 3,
            'forma_B_buona': partita.get('forma_B', '').count('V') >= 3,
            'rendimento_casa_scarso': partita.get('rendimento_casa', '').count('S') >= 3
        }
        
        from config import CAMPIONATI_ESOTICI
        if 'campionato in CAMPIONATI_ESOTICI' in condizione:
            return partita.get('campionato', '') in CAMPIONATI_ESOTICI
        
        try:
            return eval(condizione, {"__builtins__": {}}, valori)
        except:
            return False
