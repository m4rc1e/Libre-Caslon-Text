# General Evaluation of Libre Caslon, as of October 2018

As of Oct 2018, Libre Caslon Text has relatively-complete character sets in Regular, Bold, and Regular Italic masters. These are in `.vfb` (fontlab) files.

These fonts have been converted from `.vfb` (FontLab) files into `.ufo`, then `.glyphs`.

I am now proofing them to judge roughly how much effort it would be to complete the family and publish them.

It’s an inviting basis for a typeface. It’s crisp and looks relatively modern, and it some three styles already drawn: Regular to Bold basis in the romans, and has an italic with a very heavy slant and cursive forms. However, it has some issues.

## Issues

### Uneven widths

The `n` in the roman appears overly-narrow, in comparison to other letters. This means, by extension, that the spacing is called into question (because spacing tends to be based on the width of the `n` and `o`).

### Inconsistent letterforms

Most of the serifs are "wedge-style" serifs, with sharp angles connecting serifs to stems. However, the diagonal letters, `V, W, X, Y` in regular, Italic, and Bold and the `v, w, x, y` in regular and Bold have smooth serif brackets.

[image]

### The Regular & Italic styles seems overly light and thin for a "Text" typeface

There is also a regular weight of Libre Caslon Display, so it may be possible to extrapolate a roman with lower contrast.

However, there is no Libre Caslon Display Italic, so this font would have to be corrected entirely by hand if we wish to adjust the contrast.

### Some drawings need revision

The `A` has an odd top notch which doesn't meet up.

[add image]

The `X` and `x` have misaligned thin legs.

### Uneven slopes in Italic

The `*f*` is too sloped.

### Is the italic overly sterilized?

![original italic](assets/specimen-1.png)

## Work needed

To make it useful at a basic level:

- A Bold Italic will need to be added, with care taken to make the weight properly match the upright Bold.
- Anchors will need to be added to the bold in order to properly compose diacritics.
- The character set will need to be expanded somewhat, in order to meet Adobe Latin 3 or 4 (check with Dave on current expectation).
- Letters will need to be given overlaps and made compatible for interpolation, where they aren’t yet (it’s unclear in how many letters this is the case).

To make it _good_, some of the letterforms will need to be corrected. A full check should happen to determine all the spots that should be corrected.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539887893306_image.png)

![The thin legs are lined up in the wrong way – they should be offset in the opposite direction](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539887921771_image.png)
![Why doesn’t the top of the A align? This could be decomposed to work better.](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539887928707_image.png)

![These fs are overly slanted](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539888571556_image.png)

![These ogoneks should be less “stuck on”](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539888886572_image.png)

To make it _really good:_

- The weight range could be expanded (Light to Bold, or even Thin to Heavy)
- Proper historical references for Caslon should be checked to verify that this interpretation follows its actual visual direction
  - [Archive.org: A specimen of printing types by Caslon, William, 1754-1833](https://archive.org/details/specimenofprinti00caslrich/page/n5)
- Libre Caslon Display could be built out with Bold, Italic, and Bold Italic, to create a 3-axis variable font
- Swash italics could be added
- the historic reference could be more closely followed
- Greek letters from Caslon could be added

# Italic

It appears that some of the italic may have been created by half-rotating, half-slanting the romans.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539891995361_image.png)

Above, from left to right:

- the existing italic `g`
- a `g` rotated 15° and skewed 5°
- a `g` rotated 10° and skewed 10° (it looks pretty close to this)
- a `g` rotated 5° and skewed 15°
- a `g` skewed 20°

This could be good for the Bold Italic, in that it does provide a quick starting point. On the other hand, it might mean that I should throw out much of what currently exists, in order to do it better…

![Swash J, Q, and T seem to be defaults. h is a different form from the n. The g is more elogated here. Ink traps are much deeper.](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539889887065_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539889603604_image.png)

![Is it a](https://d2mxuefqeaa7sj.cloudfront.net/s_E35D387272F7DC8DA375E0A1C17DE340883DD37DCA77B3D4824EC13EDA015977_1539892557873_image.png)
