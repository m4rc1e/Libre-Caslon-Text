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

Unfortunately, I have already adjusted the weight of the Regular master from an interpolated instance, so I can't simply fix contour order. I will have dig up the deleted file with the too-light "Regular" master, update it to the new `2000` UPM, make a new `440` weigth instance, make that a master, and copy in the glyphs from there. As far as I can tell, it's only a few glyphs, so this won't take long. 