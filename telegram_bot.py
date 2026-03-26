"""
FOOTBALL BOT - TELEGRAM BOT
Riceve palinsesti, analizza partite, invia schedine
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from config import TELEGRAM_TOKEN
from regole import RegoleBot
from palinsesto_parser import PalinsestoParser

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot_regole = RegoleBot()
parser = PalinsestoParser()

MENU = """
🤖 *FOOTBALL BOT*

/start - Avvia il bot
/help - Mostra questo menu

📝 *Come inviare un palinsesto:*
Turchia vs Romania 1.43 4.80 6.60
Danimarca vs Macedonia 1.40 4.50 7.00

Ogni riga: SquadraCasa vs SquadraTrasferta quota1 quotaX quota2
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU, parse_mode='Markdown')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENU, parse_mode='Markdown')


async def analizza_messaggio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    testo = update.message.text
    
    if testo.startswith('/'):
        return
    
    partite = parser.parse_testo(testo)
    
    if not partite:
        await update.message.reply_text(
            "❌ Non ho trovato partite. Usa il formato:\n\n"
            "Turchia vs Romania 1.43 4.80 6.60"
        )
        return
    
    risultati = []
    for p in partite:
        dati_partita = {
            'nome': p['nome'],
            'quota_1': p['quota_1'],
            'campionato': 'Da definire'
        }
        
        analisi = bot_regole.analizza(dati_partita)
        
        if analisi['totale_allarmi'] == 0:
            confidenza = "🟢 ALTA"
        elif analisi['totale_allarmi'] <= 2:
            confidenza = "🟡 MEDIA"
        else:
            confidenza = "🔴 BASSA"
        
        risultati.append({
            'partita': p['nome'],
            'quota': p['quota_1'],
            'confidenza': confidenza,
            'allarmi': analisi['totale_allarmi']
        })
    
    risposta = "📊 *ANALISI PALINSESTO*\n\n"
    for r in risultati:
        risposta += f"⚽ *{r['partita']}*\n"
        risposta += f"   Quota: {r['quota']}\n"
        risposta += f"   Confidenza: {r['confidenza']}\n\n"
    
    await update.message.reply_text(risposta, parse_mode='Markdown')


def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analizza_messaggio))
    
    print("🤖 Football Bot avviato!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
