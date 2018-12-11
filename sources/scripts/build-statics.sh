############################################
################# set vars #################

glyphsSourceRoman="sources/LibreCaslonText.glyphs"

glyphsSourceItalic="sources/LibreCaslonText-Italic.glyphs"

################# set vars #################
############################################

# ===========================================================================
# functions =================================================================

fixDsig()
{
    FILEPATH=$1
    echo "fix DSIG in " ${FILEPATH}
    gftools fix-dsig --autofix ${FILEPATH}
}

AutohintFont()
{
    FILEPATH=$1
    echo "TTFautohint " ${FILEPATH}
    hintedFile=${FILEPATH/".ttf"/"-hinted.ttf"}
    # autohint with detailed info
    ttfautohint -I ${FILEPATH} ${hintedFile}
    cp ${hintedFile} ${FILEPATH}
    rm -rf ${hintedFile}
}

sortAndFontbakeFile()
{
    FILEPATH=$1

    fileName=$(basename $FILEPATH)
    newPath=fonts/librecaslontext/${fileName}
    cp ${FILEPATH} ${newPath}

    fontbakery check-googlefonts ${newPath} --ghmarkdown ${newPath/".ttf"/"-fontbakery-report.md"}
}

# ===========================================================================
# Roman Instances ===========================================================

fontmake -g ${glyphsSourceRoman} --output ttf --interpolate --overlaps-backend booleanOperations

for file in instance_ttf/*; do 
if [ -f "$file" ]; then 
    fixDsig ${file}
    AutohintFont ${file}
    sortAndFontbakeFile ${file}
fi 
done

rm -rf instance_ttf

# ===========================================================================
# Italic Instances ==========================================================

fontmake -g ${glyphsSourceItalic} --output ttf --overlaps-backend booleanOperations

for file in master_ttf/*; do 
if [ -f "$file" ]; then
    if [[ $file == *"-Italic"* ]]; then
        fixDsig ${file}
        AutohintFont ${file}
        sortAndFontbakeFile ${file}
    fi 
fi
done

# ===========================================================================
# clean up build files ======================================================

rm -rf instance_ttf
rm -rf instance_ufo
rm -rf master_ttf
rm -rf master_ufo