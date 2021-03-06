#!/usr/bin/env python3

import json
import string
from collections import OrderedDict as odict

from pathlib import Path

#load colors so they're avail in config
color_file = Path(__file__).parent / Path('material-colors.json')
with color_file.open('r') as f:
    material_colors = json.load(f)
material_colors = odict([(c['name'], odict([(k['strength'], k['hex']) for k in c['shades']])) for c in material_colors['colors']])



#CONFIG

xorg_color_types = '''black
red
green
yellow
blue
magenta
cyan
white'''

material_color_types = '''
red
light green
amber
indigo
purple
teal
'''

default_strength = 800
highlight_strength = 'A700'


invalid = '#ff00ff'
foreground = material_colors['grey'][900]
background = '#ffffff'


#CODE





xorg_color_types = xorg_color_types.split('\n')
material_color_types = [s if s else None for s in material_color_types.split('\n')]

colors = odict()

n = len(xorg_color_types)
for i, c in enumerate(material_color_types):
    if c is not None:
        default = material_colors[c][default_strength]
        highlight = material_colors[c][highlight_strength]
    else:
        default = highlight = invalid
        
    colors[i] = default
    colors[i+n] = highlight



colors_s = '\n'.join(['*color%s: %s' % c for c in colors.items()])


tpl = string.Template('''*background: $background
*foreground: $foreground

$colors''').substitute(foreground=foreground, background=background, colors=colors_s)

print(tpl)
