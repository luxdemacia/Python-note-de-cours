#!/usr/bin/env python3
#
#  While_Continue.py
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


def Boucle_While():
	x=0
	while x<=5:
		print("La valeur de x avec while :", x)
		x+=1
	return 0
# ~ Boucle_While()


def Boucle_If_Continue():
	x=0
	while x<=5:
		# ~ print("Les valeurs de x dans while :",x)
		x+=1
		if x==3:
			# ~ print("La valeur de x dans if x==3 :",x)
			continue
		print("Les valeurs de x dans while après if_continue:", x)
Boucle_If_Continue()


# ~ Pense à continue comme à un bouton "passer cette étape et recommencer depuis le début".
