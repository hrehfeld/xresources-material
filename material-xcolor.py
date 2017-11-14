#!/usr/bin/env python3

import json
import string
from collections import OrderedDict as odict

from pathlib import Path

color_file = Path(__file__).parent / Path('material-colors.json')
with color_file.open('r') as f:
    material_colors = json.load(f)
material_colors = odict([(c['name'], odict([(k['strength'], k['hex']) for k in c['shades']])) for c in material_colors['colors']])


color_types = '''black
red
green
yellow
blue
magenta
cyan
white'''.split('\n')

material_color_types = [s if s else None for s in '''
red
light green
amber
indigo
purple
teal
'''.split('\n')]

default_strength = 800
highlight_strength = 'A700'


invalid = '#ff00ff'
foreground = '#222222'
background = '#ffffff'
colors = odict()

n = len(color_types)
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
