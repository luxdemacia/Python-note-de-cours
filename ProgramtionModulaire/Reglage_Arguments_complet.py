#!/usr/bin/env python3
#
#  Presenter.py
#  
#  Copyright 2025  <codex@Boubacar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys


class Reglage:
	def __init__(self, Mon_argument):
		self.Mon_argument=Mon_argument
	
	def run(self):
		if not self.Mon_argument:
			print("Aucun argument n'est fourni.")
			return 1
		print("Argument reçu et effectué par le Réglage :")
		# ~ On n'aura plus besoin de la boucle for
		Arguments_complet = " ".join(self.Mon_argument)
		print(f"- {Arguments_complet}")
		return 0
		
	# ~ Point d'entrer
def Mis_a_jour(Mon_argument):
	reglage = Reglage(Mon_argument)
	return reglage.run()
	
if __name__ == '__main__':
	sys.exit(Mis_a_jour(sys.argv[1:]))

