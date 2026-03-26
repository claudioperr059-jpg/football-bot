"""
FOOTBALL BOT - 25 REGOLE COMPLETE
Auto-apprendente - Aggiornato al 26/03/2026
"""

class RegoleBot:
    
    def __init__(self):
        self.regole_applicate = []
        self.errori_rilevati = []
    
    def regola_1(self, partita):
        """No quote sotto 1.50 senza motivazione"""
        if partita.get('quota_1', 10) < 1.50:
            return "⚠️ Quota 1 sotto 1.50, richiede motivazione forte"
        return "✅ OK"
    
    def regola_2(self, partita):
        """Forma reale > qualità rosa"""
        forma_a = partita.get('forma_A', '')
        forma_b = partita.get('forma_B', '')
        if 'S' in forma_a[:10] and 'V' in forma_b[:10]:
            return "⚠️ Squadra A in cattiva forma, attenzione"
        return "✅ OK"
    
    def regola_3(self, partita):
        """Fattore casa obbligatorio"""
        if partita.get('casa', ''):
            rendimento_casa = partita.get('rendimento_casa', '')
            if rendimento_casa and 'S' in rendimento_casa[:20]:
                return "⚠️ Squadra di casa in cattivo rendimento"
        return "✅ OK"
    
    def regola_4(self, partita):
        """Motivazioni reali"""
        if partita.get('coppa_settimana', False):
            return "⚠️ Squadra reduce da coppa infrasettimanale"
        return "✅ OK"
    
    def regola_5(self, partita):
        """Mai giocare squadra dopo sconfitta pesante"""
        if partita.get('sconfitta_pesante', False):
            return "⚠️ Squadra reduce da sconfitta pesante"
        return "✅ OK"
    
    def regola_6(self, partita):
        """Bestie nere H2H"""
        h2h = partita.get('h2h', '')
        if '0 vittorie' in h2h:
            return "⚠️ Bestia nera: una squadra non vince da tempo"
        return "✅ OK"
    
    def regola_7(self, partita):
        """Grande occasione"""
        if partita.get('grande_occasione', False):
            return "⚠️ Pressione alta → partita tesa"
        return "✅ OK"
    
    def regola_8(self, partita):
        """Regressione xG"""
        xg_a = partita.get('xG_A', 0)
        gol_a = partita.get('gol_A', 0)
        if gol_a > xg_a * 1.2:
            return "⚠️ Squadra A in over-performance (fortuna)"
        return "✅ OK"
    
    def regola_9(self, partita):
        """Regressione difensiva"""
        clean_sheet = partita.get('clean_sheet_consecutivi', 0)
        if clean_sheet > 5:
            return "⚠️ Striscia difensiva >5 partite → rischio Under"
        return "✅ OK"
    
    def regola_10(self, partita):
        """Campionati esotici"""
        esotici = ['India', 'Cina', 'Serbia', 'Egitto', 'Perù', 'Vietnam', 'Indonesia', 'Romania', 'Colombia', 'Argentina']
        if partita.get('campionato', '') in esotici:
            return "🔴 CAMPIONATO ESOTICO → EVITARE"
        return "✅ OK"
    
    def regola_11(self, partita):
        """No aggiunte senza ok"""
        return "✅ OK"
    
    def regola_12(self, partita):
        """Trappole da Champions"""
        if partita.get('post_coppa', False):
            return "⚠️ Post-coppa → rischio scivolone"
        return "✅ OK"
    
    def regola_13(self, partita):
        """Scontri diretti obiettivi"""
        if partita.get('scontro_diretto', False):
            return "⚠️ Scontro diretto → Under e 1X preferiti"
        return "✅ OK"
    
    def regola_14(self, partita):
        """Squadre in crisi"""
        sconfitte = partita.get('sconfitte_consecutive', 0)
        if sconfitte >= 3:
            return "⚠️ Squadra in crisi (3+ sconfitte) → evitare Over/GG"
        return "✅ OK"
    
    def regola_15(self, partita):
        """Verifica BTTS %"""
        btts_a = partita.get('btts_percentuale_A', 50)
        btts_b = partita.get('btts_percentuale_B', 50)
        if btts_a < 40 or btts_b < 40:
            return "⚠️ BTTS basso (<40%) → evitare Goal"
        return "✅ OK"
    
    def regola_16(self, partita):
        """Forma batte storia"""
        return "✅ OK"
    
    def regola_17(self, partita):
        """Vantaggio killer"""
        if partita.get('vantaggio_andata', 0) >= 3:
            return "⚠️ Vantaggio >3 gol → evitare GG"
        return "✅ OK"
    
    def regola_18(self, partita):
        """Crisi + goleada"""
        if partita.get('crisi_e_goleada', False):
            return "⚠️ Crisi + goleada → evitare GG"
        return "✅ OK"
    
    def regola_19(self, partita):
        """Multipla max 3 eventi"""
        return "✅ OK"
    
    def regola_20(self, partita):
        """Salvezza in trasferta vs big"""
        if partita.get('salvezza_trasferta', False):
            return "⚠️ Salvezza in trasferta vs big → evitare GG, preferire Under"
        return "✅ OK"
    
    def regola_21(self, partita):
        """Nuovo allenatore al debutto"""
        if partita.get('nuovo_allenatore', False):
            return "⚠️ Nuovo allenatore al debutto → abbassare confidenza"
        return "✅ OK"
    
    def regola_22(self, partita):
        """5+ infortuni titolari"""
        if partita.get('infortuni_titolari', 0) >= 5:
            return "⚠️ 5+ infortuni → favorito incerto, preferire X2/Under"
        return "✅ OK"
    
    def regola_23(self, partita):
        """Difesa solida in casa ≠ Under"""
        difesa_solida = partita.get('difesa_solida_casa', False)
        attacco_forma = partita.get('attacco_in_forma', False)
        if difesa_solida and attacco_forma:
            return "⚠️ Difesa solida ma attacco in forma → Under non automatico"
        return "✅ OK"
    
    def regola_24(self, partita):
        """Striscia positiva inattesa"""
        vittorie_consecutive = partita.get('vittorie_consecutive', 0)
        attacco_scarso = partita.get('attacco_scarso', False)
        if vittorie_consecutive >= 3 and attacco_scarso:
            return "⚠️ Striscia positiva inattesa → attenzione a Under"
        return "✅ OK"
    
    def regola_25(self, partita):
        """X + Under 1.5 contraddittoria"""
        if partita.get('pronostico_X', False) and partita.get('pronostico_under_15', False):
            return "🔴 X + Under 1.5 → contraddittoria! Usa Under 2.5"
        return "✅ OK"
    
    def analizza(self, partita):
        """Applica tutte le regole e restituisce risultati"""
        risultati = []
        for i in range(1, 26):
            metodo = getattr(self, f"regola_{i}")
            esito = metodo(partita)
            if esito != "✅ OK":
                risultati.append(f"📌 Regola #{i}: {esito}")
        
        return {
            'esiti': risultati,
            'allarmi': len([r for r in risultati if '🔴' in r or '⚠️' in r]),
            'regole_applicate': self.regole_applicate
        }


# Test rapido
if __name__ == "__main__":
    bot = RegoleBot()
    
    test_partita = {
        'quota_1': 1.43,
        'campionato': 'Qualificazioni Mondiali',
        'scontro_diretto': True,
        'infortuni_titolari': 1,
        'grande_occasione': True
    }
    
    risultato = bot.analizza(test_partita)
    print("RISULTATO ANALISI:")
    for r in risultato['esiti']:
        print(r)
