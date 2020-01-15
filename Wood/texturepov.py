#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import re
import fileinput

replace = { "<1,0,1>" : "texture{ Cherry_Wood }", # Magenta
            "<1,1,0.5>":"texture{ Cork }",
            "<1,0,1>":"texture{ DMFDarkOak }",
            "<0,1,0>":"texture{ DMFLightOak }",
            "<0,0.33,0>":"texture{ DMFWood1 }",
            "<0.67,0.67,0>":"texture{ DMFWood2 }",
            "<0.33,0,0>":"texture{ DMFWood3 }",
            "<1,0.67,1>":"texture{ DMFWood4 }",
            "<0,0,1>":"texture{ Dark_Wood }"}

withintexture = 0
textureblock = ""
newtexture = ""

for line in fileinput.input():
    if (line.strip().startswith("texture {")):
        withintexture = 1
        textureblock = ""
        newtexture = ""

    if (withintexture == 1):
        textureblock += line

        for key in replace.keys():
            if (line.find(key)>0):
                newtexture = replace[key]

        if (line.strip().startswith("}")):
            withintexture = 0
            if (newtexture != ""):
                print(newtexture)
            else:
                print(textureblock)
    else:
        print(line)
