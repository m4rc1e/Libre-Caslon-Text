# Making Romans Compatible

As is documented in the Evaluation log, there are several incompatible glyphs to make compatible.

![](assets/incompatible-glyphs.png)

Because most of these seem to be about anchor points missing in the bold, I will first write a script to copy over the anchor points between masters, and then I will go through an adjust their positions in the bold master.

I'm starting by checking which glyphs have different amounts of anchors:

```
font = Glyphs.font

# help(font.masters[0])

for glyph in font.glyphs:
	if len(glyph.layers[0].anchors) !=  len(glyph.layers[1].anchors):
		print glyph.name, "\n"
		for layer in glyph.layers:
			if len(layer.anchors) > 0:
				print layer.name, "\n", layer.anchors,"\n", "\n"
```

Comparing just the amount of anchors, I get this:

```
A D E G H I J K L N O R S T U W Y Z c d dotlessi dotlessj h i k l o s w y z
```

I now need to find how to insert anchors into the glyphs that are missing them.

`anchors` is a "list, dict" within GSLayer. Glyphs says this can be done with:

```
# add a new anchor
layer.anchors['top'] = GSAnchor()
```

...and then I can probably set the x, y coordinates.
