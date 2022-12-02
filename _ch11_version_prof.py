"""
Exemple récapitulatif qui inclut les notions du chapitre 11 et de tous les autres.
"""


from _ch8_version_prof import *
from _ch9_version_prof import *
from _my_bot_version_prof import MyBot


def run_ch11_example():
	opts = parse_args()

	config = load_config(opts.config_file)
	quotes = load_quotes(opts.quotes_file)

	# TODO: Construire un objet de type `MyBot` avec "logs" comme dossier de journaux et avec les citations extraites du JSON.
	bot = MyBot("logs", quotes)
	bot.connect_and_join(config.password, config.nickname, config.channel)
	bot.run()


if __name__ == "__main__":
	run_ch11_example()
