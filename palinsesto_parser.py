"""
FOOTBALL BOT - PARSER PALINSESTI
Legge palinsesti da testo e li trasforma in partite analizzabili
"""

import re

class PalinsestoParser:
    
    def parse_testo(self, testo):
        """Legge palinsesto in formato testo"""
        
        partite = []
        righe = testo.strip().split('\n')
        
        for riga in righe:
            partita = self._parse_riga(riga)
            if partita:
                partite.append(partita)
        
        return partite
    
    def _parse_riga(self, riga):
        """Parsa una singola riga"""
        
        # Pattern: SquadraA vs SquadraB quota1 quotaX quota2
        pattern = r'(.+?)\s+vs\s+(.+?)\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)'
        match = re.search(pattern, riga)
        
        if match:
            return {
                'casa': match.group(1).strip(),
                'trasferta': match.group(2).strip(),
                'nome': f"{match.group(1)} vs {match.group(2)}",
                'quota_1': float(match.group(3)),
                'quota_X': float(match.group(4)),
                'quota_2': float(match.group(5))
            }
        
        return None
