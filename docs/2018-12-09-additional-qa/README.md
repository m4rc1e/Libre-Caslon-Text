# Additional QA

This is a not-very-descriptive title, referring to QA done outside of FontBakery and my earlier QA work. This will encompass random issues I see crop up, plus specific Red Arrows / FontAudit checks.

## Drawbot Specimen

In making a specimen in Drawbot, I've noticed several interpolation errors.

![](assets/charset-tall3.png)

Errors I'm now seeing are messed-up interpolation from out-of-order contours in:
- `/perthousand`
- `/colon`
- `/divide` and `/divide.tnum`
- `/guillemotleft` and `/guillemotright`
- `/brokenbar`

![](assets/2018-12-10-20-40-27.png)

![](assets/2018-12-10-20-50-24.png)

Unfortunately, I have already adjusted the weight of the Regular master from an interpolated instance, so I can't simply fix contour order. I will have dig up the deleted file with the too-light "Regular" master, update it to the new `2000` UPM, make a new `440` weight instance, make that a master, and copy in the glyphs from there. As far as I can tell, it's only a few glyphs, so this won't take long. 

## Red Arrows Outlines QA


### Simplifying brackets?

There are some brackets that have Red Arrows for "Incorrect Smooth Curves" which have unnecessary points.

![](assets/bracket.gif)

These vertical extreme points cause no visible disruption, but also offer no benefit in hinting. I'll remove them in cases like this, where their removal does not visible alter the outlines.

### Simplifying curve anchors to prevent kinks

There are many control points on non-extreme parts of curves. This has the potential to cause kinking. However, in practice, the kinks that exist are invisible to the naked eye, even at a very large scale.

![](assets/curve-point.gif)


At SemiBold, this kink is invisible:
![](assets/2019-01-07-12-19-51.png)

At Medium, this kink is invisible:
![](assets/2019-01-07-12-21-40.png)

These invisible kinks are the case for many characters, like `/B`, `/D`, `/G`, and many more. With this font, the weight range between masters isn't very extreme, which is part of the reason these points don't cause much of a problem, whereas they likely would if something were really a thin-to-black interpolation range. Still, I'll check each for visible kinks.

### Removing inflections

I'll remove/correct inflections by copying outlines to a visible background layer to ensure the overall shapes change as little as possible.

![](assets/2019-01-07-12-27-47.png)

![](assets/2019-01-07-12-28-50.png)

In cases like the `/S`, I'll instead insert points with the GlyphsApp script [Insert Inflections](https://github.com/mekkablue/Glyphs-Scripts/blob/7ba28e691f6ce76650bf9da344cf230f7a5bb44a/Paths/Insert%20Inflections.py) from @mekkablue.

![](assets/s-inflections.gif)

...checking that it doesn't cause kinking in interpolated instances:

![](assets/2019-01-07-12-34-39.png)

![](assets/2019-01-07-12-37-02.png)

I'll actually add two points, then balance the handles. This keeps the original shape, but allows for more-balanced handles.

![](assets/2019-01-07-13-05-56.png)

And match that in the lowercase:

![](assets/2019-01-07-15-56-08.png)

Of course, in certain areas, removing inflections would likely cause more trouble than it would resolve, as in the `/Q` and `/asciitilde`

![](assets/2019-01-07-12-30-56.png)

Here I inserted a point into the long and prominent curve, plus balanced handles with Simon Cozens' [SuperTool](http://www.simon-cozens.org/supertool.html). This should improve output TTF curves. I left the other inflections, however, because they are too small or slight to correct without disrupting the curve. Checking in the exported VF, these curves don't seem to be too disruptive to TTF quadratic curves.

![](assets/2019-01-07-12-57-22.png)

![](assets/Q.gif)

![](assets/2019-01-07-12-31-36.png)


Some are pretty messy:

![](assets/2019-01-07-15-05-03.png)

This `/r` isn't related in shape to the `/n` or `/m`, so I'll change the connection to a sharp one, as I make a better curve:

![](assets/2019-01-07-15-11-43.png)

![](assets/2019-01-07-15-11-52.png)

![](assets/2019-01-07-15-10-50.png)

The inflections on the `/w` create visibly-poor curves. Let me fix that.

![](assets/2019-01-07-18-15-13.png)

Better:

![](assets/2019-01-07-18-19-42.png)




### Fractional transformation

Probably due to my previous work of making a slightly-heavier "regular" master, the /Tbar has a slight fractional X translation. Because I don't see this much elsewhere, I'll manually correct this one rather than writing a script.

![](assets/2019-01-07-14-08-51.png)


### Unnecessary control points

There are quite a few control points that do little to nothing for the actual shapes, such as this very small flat segments in `/e`-shapes.

![](assets/2019-01-07-14-37-35.png)

It's easy to remove these points and achieve almost exactly the same contour, which slightly smoothes out the slight kinks from this:

Before:

![](assets/2019-01-07-14-40-13.png)

After (showing the previous outlines as a background layer):

![](assets/2019-01-07-14-39-28.png)


![](assets/2019-01-07-14-57-50.png)

![](assets/2019-01-07-14-59-04.png)

Some letters have probably-unecessary points, but they don't cause issues, so I'll leave them:

![](assets/2019-01-07-15-03-59.png)

No kinks caused:

![](assets/2019-01-07-15-04-22.png)

Some unecessary control points cause lumpy curves. Here's a before-after of the `/t` (it is now a smoother curve, which better aligns to the overall design style):

![](assets/round-t.gif)

This has an unneeded point, and can be simplified without changing shape:

![](assets/2019-01-07-18-04-29.png)

![](assets/2019-01-07-18-04-56.png)

Additionally, the `/u` has an "inktrap" which is not present in almost any other character with a similar connection, like `/n`, `/m`, `/r`, etc. I'll remove it.

![](assets/inktrap-u.gif)

This `/x` has two problems:
1. unnecesary control points, with smooth brackets that are overly-pointy
2. misaligned thin stems. They should be offset in the *opposite* direction

![](assets/2019-01-07-18-21-21.png)

Fixed:

![](assets/x.gif)

Some points are not really needed and triggering an "incorrect smooth curve" notice, but not causing visible kinks or lumpy curves. I'll leave them:

![](assets/2019-01-07-18-31-08.png)

### Other issues

The `/Z` and `/z` have an inconsistent approach to these flat bits:

![](assets/2019-01-07-18-27-18.png)

Most of them are angled, while some are flat. This doesn't have a great regular/bold break, so I've made them all slightly-angled:

![](assets/2019-01-07-18-29-10.png)

The cent has no bold:

![](assets/cent.gif)

Now it does:

![](assets/cent2.gif)

The `/sterling` is lumpy and doesn't connect at the curly bit:

![](assets/2019-01-07-18-40-01.png)


Luckily, this will benefit a lot from a non-overlapped drawing ...to be continued.

---

### Rounding Kerning

Because I interpolated the "Regular" master, I've rounded kerns to integers with GlyphsApp Freemix tools.