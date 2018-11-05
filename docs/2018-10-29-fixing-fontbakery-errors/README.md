# Fixing FontBakery Errors by customizing a build script for Libre Caslon Text

I'll be logging my progress in getting through Failures & Errors caught by FontBakery on [this GitHub issue])(https://github.com/thundernixon/Libre-Caslon-Text/issues/2).

In this doc, I will go through setting up my `build.sh` script to handle Libre Caslon Text (which I'll call *LC*).

---

I'm using a `build.sh` set of scripts inherited from [@mjlagattuta](https://github.com/mjlagattuta), then customized and updated for [Encode Sans](https://github.com/thundernixon/Encode-Sans). This includes fixes for several of the problems that are flagged by FontBakery.

This script allows me to add fixes to the font export workflow, which can add up as I learn new fix methods, to gradually make exports better and better.

Here, I'll go through the changes I make to suit this build script to my needs for LC. With each change, I'll run the build script to make sure things are still working as expected. 

### Remove fix designspace script

This font will be only a 1-dimensional VF for now (with a `wght` axis), so I don't need to morph the designspace to be rectangular.

### Automatically set font name, to avoid errors

It's deleting the ttf folder before it can move the file ... my guess is, the VF file might be getting a name different from what I expect. So, I'll comment-out the `rm` lines of the build script, to see why the file can't be moved.

My `master_ufo` folder shows that the name of the font is `LibreCaslonText2048`, which is left over from earlier experiments with font scaling. I could update my variable in the build script, but that is a hacky solution. Instead, I'll make a helper script using glyphsLib to grab the font name.

Turns out, it's extremely simple. The shell script just needed to set a variable, feeding the source file into a Python helper script.

`build.sh`:
```Shell
VFname=`python2 scripts/helpers/get-font-name.py ${glyphsSource}`
```

`get-font-name.py`:
```Python
import sys
from glyphsLib import GSFont

filename = sys.argv[-1]
font = GSFont(filename)

# get font name, remove spaces
varFontName = font.familyName.replace(' ','') + '-VF'

print(varFontName)

sys.exit(0)
```

Fun fact: I tested that the variable was being set in the shell script by following that with `banner ${VFname}`, which prints variables in vertical ASCII art.

### Update (maybe remove?) Name Patch

Right now, the font is preview as if it had both `wdth` and `wght` axes, but it only has `wght`. Most likely, this is because the `NAMEpatch.xml` and `STATpatch.xml` files are still customized for Encode Sans.

![](assets/axis-error.gif)

To start, I'll comment-out the `sed`-based `name` and `STAT` patches, then see if this causes problems in FontBakery.

This doesn't solve the two-axis problem, so I'll need to `ttx` the VF and see more clearly what the `name` and `STAT` tables look like.

From this, I can see that the `STAT` table is showing two axes.

```
<STAT>
    <Version value="0x00010002"/>
    <DesignAxisRecordSize value="8"/>
    <!-- DesignAxisCount=2 -->
    <DesignAxisRecord>
      <Axis index="0">
        <AxisTag value="wght"/>
        <AxisNameID value="256"/>  <!-- Weight -->
        <AxisOrdering value="0"/>
      </Axis>
      <Axis index="1">
        <AxisTag value="wdth"/>
        <AxisNameID value="257"/>  <!-- Width -->
        <AxisOrdering value="1"/>
      </Axis>
    </DesignAxisRecord>
    <!-- AxisValueCount=0 -->
    <ElidedFallbackNameID value="2"/>  <!-- Regular -->
</STAT>
```

Similar issues also exist in the `name` table:

```
<namerecord nameID="256" platformID="1" platEncID="0" langID="0x0" unicode="True">
    Weight
</namerecord>
<namerecord nameID="257" platformID="1" platEncID="0" langID="0x0" unicode="True">
    Width
</namerecord>
```

This is probably due to GlyphsApp having both Weight and Width information for each instance, by default:

![](assets/glyphsapp-instance.png)

Because of this, I will try two things:
1. Adding a "Custom Parameter" of `axes` for `wght` to the GlyphsApp Font Into
1. ~~If the first step doesn't work, I'll also update the `NAMEpatch` and `STATpatch` files to remove the unnecessary~~ The first step seems to have worked!

![](assets/axis-fixed.png)

## To fix

- [x] For starters, I get this error when I build the VF: `WARNING:fontTools.varLib:glyph agrave has incompatible masters; skipping`

(This was easily fixed by reordering contours in `/agrave`).

- [x] Once I deleted the "patch" files, there was trouble using ttx on the `build.sh` outputs. 

(This was fixed by simplifying the build script, and making sure my path names were all correct).

- [x]  :fire: FAIL:</b> Checking file is named canonically.

(Made "Regular" instance `400` weight, added " and "SemiBold" weights at `500` and `600` weights). This didn't do the trick.

...after some digging, I eventually found that I was using an old version of FontBakery. I *think* this is because I used pip2 to update FontBakery earlier in the day, but this seems to have pulled a year-old version of FB into my py2 environment. In any case, this shows that I should probably just be using py3, aside from maybe with glyphsLib, which I think might be py2-only.

Plus, I have lots of FontBakery issues to resolve. I'm keeping a full log of these in [Issue #2](https://github.com/thundernixon/Libre-Caslon-Text/issues/2), but here are the others high-weight issues:

- [x] Checking with ots-sanitize. * ERROR: Failed with ModuleNotFoundError: No module named 'ots'

I found that "opentype sanitizer" was just updated to be a Python module and [updated in the FB checks](https://github.com/googlefonts/fontbakery/pull/2092).

I had to install it with `pip install opentype-sanitizer`. ([More info here](https://pypi.org/project/opentype-sanitizer/)).


- [ ] FAIL: Checking OS/2 usWinAscent & usWinDescent. – FAIL OS/2.usWinAscent value should be equal or greater than 1708, but got 1707 instead [code: ascent].
- [ ] FAIL: Checking OS/2 Metrics match hhea Metrics. – FAIL OS/2 sTypoAscender and hhea ascent must be equal. [code: ascender]

These errors seem related, and may be coming from my earlier re-adjustment of the overall scaling of this font. I wanted to check where these numbers are coming from, so I opened the `ttx` version of the VF.

The `<head>` table contains `<yMax value="1708"/>` and the  `<hhea>` table contains `<ascent value="1707"/>`. What is further strange is that the Glyphs source actually puts the ascender height of both masters at `1443`.

The MS Typography OpenType [spec on hhea](https://docs.microsoft.com/en-us/typography/opentype/spec/hhea) defines `acent` as "Distance from baseline of highest ascender." Meanwhile, the [`head` table spec](https://docs.microsoft.com/en-us/typography/opentype/spec/head) defines `ymax` as "For all glyph bounding boxes." This leads me to believe that it might include not just ascenders in the typical sense, but also accent marks.

And sure enough! The `ring` accent has a point at `1707`. 

![](assets/2018-11-05-11-47-06.png)

I didn't know if there was any other glyph taller than the `ring`, so I used a script to print a list of glyphs with an ascent of more than `1700`:

```Python
font = Glyphs.font

for glyph in font.glyphs:
	for layer in glyph.layers:
		ascent = layer.bounds.size.height + layer.bounds.origin.y		
		if ascent >= 1700:
			print(glyph.name, ascent)
```

It showed me that caps with a `caron.cap` accent all had an ascent of `1708`. This was surprising, as the `caron.cap` itself only had and ascent of `1690`. However, I realized by decomposing the `Rcaron` that the anchor was positioning the `caron.cap` higher in caps than it was drawn.

![](assets/2018-11-05-12-06-01.png)

It seems probable that the `head` must be getting derived from the highest point in the font, including in composed glyphs, while the `hhea` table is derived from the highest-drawn point in the font, not counting composed glyphs. And now to resolve that mismatch... 

I'll try moving the `caron.cap` to it's "natural" position, so that its height matches the composed height.