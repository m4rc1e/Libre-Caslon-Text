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

`WARNING:fontTools.varLib:glyph agrave has incompatible masters; skipping`