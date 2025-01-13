#!/usr/bin/env python3
#
#  exemple_args.py
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

def main(args):
    if not args:
        print("\nAucun argument fourni")
        return 1  # Retourne 1 pour indiquer un échec
    for arg in args:
        print(f"Argument reçu: {arg}")
    return 0  # Retourne 0 pour indiquer un succès

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # Passe les arguments sans le nom du script

# ~ Explication :
# ~ sys.argv[1:] récupère tous les arguments passés après le nom du script. Ces arguments sont ensuite envoyés à la fonction main sous forme de liste.
# ~ La fonction main traite cette liste et effectue une action selon les arguments fournis.
# ~ L'instruction sys.exit(main(sys.argv[1:])) garantit que le code de sortie du programme est retourné, où 0 signifie un succès et un autre code (comme 1) indique une erreur ou une condition particulière.


