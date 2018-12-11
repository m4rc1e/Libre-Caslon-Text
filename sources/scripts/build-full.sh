### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path
### requires a python 3 environment, for now

##################################################
################# set vars below #################

glyphsSource="sources/LibreCaslonText.glyphs"

## move VF into new folder of dist/ with timestamp and fontbake; otherwise, add fresh file to fonts/ folder
## advice: make this 'true' while you're working, and 'false' while you're working to publish the final fonts
timestampAndFontbakeInDist=false

## keep designspace file if you want to check values later
keepDesignspace=false

################# set vars above #################
##################################################



# ===========================================================================
# Set up names ==============================================================

# get font name from glyphs source
VFname=`python sources/scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"

## make temp glyphs filename with "-build" suffix
tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

## copy Glyphs file with temp filename
cp $glyphsSource $tempGlyphsSource

# ===========================================================================
# Generate Variable Font ====================================================

## call fontmake to make a varfont
fontmake -o variable -g $tempGlyphsSource

if [ $keepDesignspace == true ]
then
    echo "designspace in master_ufo folder"
else
    rm -rf master_ufo
fi

## clean up temp glyphs file
rm -rf $tempGlyphsSource

# ===========================================================================
# OpenType table fixes ======================================================

# cd variable_ttf

## fix file metadata with gftools
echo "fix DSIG in " ${VFname}
gftools fix-dsig --autofix variable_ttf/${VFname}.ttf
rm -rf ${VFname}-backup-fonttools-prep-gasp.ttf


# ===========================================================================
# Autohinting ===============================================================

ttfPath=variable_ttf/${VFname}.ttf
hintedPath=${ttfPath/".ttf"/"-hinted.ttf"}

# Hint with TTFautohint-VF 
# currently janky – I need to find how to properly add this dependency
# https://groups.google.com/forum/#!searchin/googlefonts-discuss/ttfautohint%7Csort:date/googlefonts-discuss/WJX1lrzcwVs/SIzaEvntAgAJ
# ./Users/stephennixon/Environments/gfonts3/bin/ttfautohint-vf ${ttfPath} ${ttfPath/"-unhinted.ttf"/"-hinted.ttf"}
echo "================================================"
echo ttfautohint-vf $ttfPath $hintedPath
echo "================================================"
ttfautohint-vf -I $ttfPath $hintedPath

finalHintedFont=${hintedPath/"-hinted"/""}
cp $hintedPath $finalHintedFont


# ===========================================================================
# Sort into final folder ====================================================

# open VF in default program; hopefully you have FontView
open ${finalHintedFont}

# set this to true/false at top of script
if [ $timestampAndFontbakeInDist == true ]
then
    newFontLocation=`python sources/scripts/helpers/distdate.py variable_ttf/${VFname}.ttf`

    fontbakery check-googlefonts ${newFontLocation}/${VFname}.ttf --ghmarkdown ${newFontLocation}/${VFname}-fontbakery-report.md

    echo "new VF location is " ${newFontLocation}
else
    ## move font into fonts/, then fontbake
    finalFontLocation=fonts/${VFname}.ttf
    cp $finalHintedFont $finalFontLocation
    echo "new VF location is " ${finalFontLocation}

    fontbakery check-googlefonts ${finalFontLocation} --ghmarkdown ${finalFontLocation/".ttf"/"-fontbakery-report.md"}
fi

rm -rf variable_ttf
