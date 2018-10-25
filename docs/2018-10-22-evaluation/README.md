# General Evaluation of Libre Caslon, as of October 2018

As of Oct 2018, Libre Caslon Text has relatively-complete character sets in Regular, Bold, and Regular Italic masters. These fonts have been converted from `.vfb` (FontLab) files into `.ufo`, then `.glyphs`.

I am now proofing them to judge roughly how much effort it would be to complete the family and publish them.

It’s an inviting basis for a typeface. It’s crisp and looks relatively modern, and it some three styles already drawn: Regular to Bold basis in the romans, and has an italic with a very heavy slant and cursive forms. However, like any work, it has some issues that could be improved. I'll go through the ones I notice first, as a basis for potential improvment work.

Without knowing exactly the sources Pablo Impallari used for the work so far, I am basing some of my critique on this Caslon specimen: [Archive.org: A specimen of printing types by Caslon, William, 1754-1833](https://archive.org/details/specimenofprinti00caslrich/page/n5)

## Technical Issues

### Uneven widths

The `n` in the roman appears overly-narrow, in comparison to other letters. This means, by extension, that the spacing is called into question (because spacing tends to be based on the width of the `n` and `o`).

### Inconsistent letterforms

Most of the serifs are "wedge-style" serifs, with sharp angles connecting serifs to stems. However, most of the diagonal letters, `A, K, V, W, X, Y` in regular, Italic, and Bold and the `v, w, x, y` in regular and Bold have smooth serif brackets.

![inconsistent serif brackets](assets/brackets.png)

![Letters with smooth vs sharp brackets](assets/smooth_and_sharp2.png)

The design could also be thought of as a collection of smooth and sharp connections with more details taken in mind, such as the ball terminals of letters. If the scope is broadened like this, the design is slightly more balanced, though still, I would argue, could benefit from a more consistent approach to details. However, the consistency of serif brackets is an obvious detail to be harmonized, whereas terminals are separate enough visually, they can probably be safe to leave as-is.

![Letters with smooth vs sharp details](assets/smooth_and_sharp.png)

There's no rule saying a typeface _can't_ have different forms of serif brackets, but the inconsistency seems arbitrary. If a typeface is going to be a modern spin on a classic style by sharpening brackets, it makes more sense to be consistent, as [Spectral](https://fonts.google.com/specimen/Spectral) is to the original model of Plantin type.

![libre caslon vs spectral](assets/libre_caslon-spectral.png)

### Some drawings need revision

The `A` has an odd top notch which doesn't meet up. Additionally, this is much more accentuated than Caslon `A` notches that I have seen in historical references.

![](assets/axen.png)

![The thin legs are lined up in the wrong way – they should be offset in the opposite direction](assets/x.png)

_The thin legs are lined up in the wrong way – they should be offset in the opposite direction]_

![Why doesn’t the top of the A align? This could be decomposed to work better.](assets/A.png)

_Why doesn’t the top of the A align? This could be two contours in order to work better._

![These ogoneks should be less “stuck on”](assets/ogonek.png)

The `X` and `x` have misaligned thin legs.

### Uneven slopes in Italic

The `*f*` is too visually sloped overall, because at its minimum slope, it matches the slope of straight stems in letters like `*l*`, whereas in historical sources, the midpoint is at a more gradual slope so that the overall shape matches the flow of surrounding letters.

![These fs are overly slanted](assets/falafel.png)

### The Regular & Italic styles seems overly light and thin for a "Text" typeface

When compared to an original specimen of text type from Caslon, Libre Caslon is _much_ lighter and higher-contrast.

![libre caslon vs original](assets/libre_caslon-og_caslon.png)

There is also a regular weight of Libre Caslon Display, so it may be possible to extrapolate a roman with lower contrast. However, a quick test of this shows that the extrapolated "caption" style gets a _massive_ x-height, revealing that one of the biggest differences in the original Text and Dispaly was a different x-height.

However, there is no Libre Caslon Display Italic, so this font would have to be corrected entirely by hand if we wish to adjust the contrast.

I was curious about the narrow `n`s and the sharp contrast of Libre Caslon Text, and wondered how it might compare against something like Times New Roman. A comparison shows:
- The "regular" of Libre Caslon is a bit lighter
- Overall, the letter shapes are noticeably more condensed.
- The contrast in Libre Caslon is higher – thin strokes and serifs are more thin/delicate.

![Libre Caslon vs Times New Roman](assets/libre_caslon-times_new_roman.png)

### Is the italic overly sterilized?

Compared to the original Caslon, the existing Libre Caslon Italic has too symmetrical of stroke contrast from top to bottom. It's closer to "expansion" models of contrast, from fonts like Didot or Century Old Style, whereas Caslon was closer to a flat-pen, transitional-contrast model.

In addition, Libre Caslon Italic is very smooth, and lacks the sharp turns from the corners of the original, especially visible in the shoulders and bowls of letters like `t, n, e, b`.

Finally, Libre Caslon Italic is missing many of the warm details of the original cuts. Not only are swash caps `J, Q, T` missing, but other things have been lost, as well, such as the rotation of the `o`, the turning-in of the `h`, the elegant leaning-back curve of the `f`, and the hard angle of the `A` (pictured above). Finally, this may be partly a result of the overly-light contrast in Libre Caslon, but the joints / ink traps of letters like `n, u, r, d` appear to be much more aggressive in the original.

![Italics](assets/italics.png)

### Odd font metrics

When compared to other fonts, including Libre Caslon Display, Libre Caslon Text has a much larger overall body size. This would be helpful to normalize before publication as a web font, in order to make font loading smoother from system fonts, as well as to make this an easier and more-predictable font to design with.

One positive thing shown when cap heights are matched: the stroke contrast of the Libre Caslon Text isn't quite as problematically high as I first thought. It's close to being the same as TNR and Times, and if the regular is interpolated to be just slightly bolder, the color of it might work decently well in text sizes.

This image compares the current Libre Caslon Regular against default "serif" fonts across several OSes and browsers, as they are according to [this resource](https://www.granneman.com/webdev/coding/css/fonts-and-formatting/web-browser-font-defaults). It also compares LC Display for a look at the relative metrics. It shows things at the same point size to show how LC is abnormal, then at a "normalized" size, to better compare actual font sizing for x-height and overall weight.

![relative-size-analysis.png](assets/libre-caslon-relative_sizing.png)

### Some glyphs incompatible

Some glyphs are incompatible and currently preventing a variable font export. However, in most glyphs this seems to be only due to the bold master lacking anchors for diacritics, which will be relatively quick to solve.

![incompatible-glyphs](assets/incompatible-glyphs.png)

# Work needed

**To make it good and useful:**

- Font metrics should be adjusted so that the text style is closer in body size to common fallback fonts
- The regular weight instance should have a little more weight so that the text style is closer in body size to common fallback fonts
- The character set will probably need to be expanded somewhat in order to meet Adobe Latin 3 or 4 (need to find current gfonts expectation).
- A Bold Italic will need to be added, with care taken to make the weight properly match the upright Bold.
- Letters will need to be given overlaps and made compatible for interpolation where they aren’t yet.
- Anchors will need to be added to the bold in order to properly compose diacritics and allow interpolation.

**To make it _even better_:**

- Ideally, I would be able to see the historical resources used by Pablo Impallari in the existing design.
- Some of the letterforms will need to be optically corrected (e.g. `x`, italic `f`).
  - A full check should happen to determine all the spots that should be corrected.
- We could experiment with how the font might look with sharper details in the ball terminals, and whether serif brackets should be all sharp or all smooth.

**To make it _really good_, we might eventually do a few more things:**

- The weight range could be expanded (Light to Bold, or even Thin to Heavy)
- Libre Caslon Display could be built out with Bold, Italic, and Bold Italic, to create a 3-axis variable font
- Swash italics could be added
- Greek, Hebrew, and Arabic letters from fonts by Caslon could eventually be added

![Greek](assets/caslon-greek.png)
![Hebrew](assets/caslon-hebrew.png)
![Arabic](assets/caslon-arabic.png)
