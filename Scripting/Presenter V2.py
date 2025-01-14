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

class Presenter:
    def __init__(self, args):
        self.args = args

    def run(self):
        if not self.args:
            print("Aucun argument n'est fourni.")
            return 1
        print("Argument reçu par le Presenter:")
        complete_arg = " ".join(self.args)
        print(f"- {complete_arg}")
        return 0

def main(args):
    # Point d'entrée pour le Presenter
    presenter = Presenter(args)
    return presenter.run()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
