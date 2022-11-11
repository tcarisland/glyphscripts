#MenuTitle: Add Layers
# -*- coding: utf-8 -*-
palettes = [3, 1, 2, 0, 4, 1]
masterID = Font.masters[0].id

def addColorLayers(glyph, palettes, masterID):
	for c in palettes:
		layer = GSLayer()
		layer.associatedMasterId = masterID
		layer.attributes['colorPalette'] = c
		glyph.layers.append(layer)

for myGlyph in Glyphs.font.selection:
	if(len(myGlyph.layers) == 1):
		addColorLayers(myGlyph, palettes, masterID)
