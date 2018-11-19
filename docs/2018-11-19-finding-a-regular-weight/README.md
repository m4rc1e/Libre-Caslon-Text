# Finding a "Regular" weight for Text Roman

### Current issue:

Libre Caslon Text "Regular" is significantly lighter in weight than comparable typefaces. It is also slightly lighter in appearance than Libre Caslon Text Italic (in part because the italic keeps roughly the same stroke width, but has a steep slope and slightly-narrow proportions).

## Testing

I spent some time trying to set tests in Drawbot. This was helpful, because it allows for a lot of variations of `wght` values to be tested, quickly.

This led me to belief that a `wght` value of about `440` better matched the Italic style.

However, Drawbot testing had the flaw that different fonts were given different line heights, rather than keeping the same line height as other "Regular" fonts, so it was hard to properly compare to other families.

To keep similar line heights between fonts, I also set some simple tests in Adobe Illustrator. Through this method, the sweet spot appears to be around `wght = 430`.

![](assets/libre-caslon-reg_wght-test-01.png)
![](assets/libre-caslon-reg_wght-test-03.png)
![](assets/libre-caslon-reg_wght-test-04.png)

However, after trying different fonts, I'm seeing that there is some level of variance in the color of different "regular" fonts. With that in mind, I'm going to actually seek to match the Regular to the Italic color, so these can work well together in text. 

It's taken some experimentation to find the right way to visualize this in Drawbot. I've found that setting multiple, alternating lines seems to be a helpful way to match the colors of these fonts. The text has to be at a large enough size to actually show the shapes of letters and to avoid the effect being overly impacted by pixelation of small text, but small enough to avoid this being an irrelevant comparison for text. I've found that 32pt seems to be the most useful size to view the comparison. Probably, it would also be useful to do a static comparison with a sheet printed from a laser printer, at actual text sizes (10pt–16pt). When viewed in a video, the time slider can be scrubbed back and forth to control the Roman weight axis (with extra time, this might form the basis of a useful interactive weight-matching tool). Through this method, the sweet spot appears to be around `wght = 445`.

![](assets/weight-test-roman_italic-noblur-big-111918.gif)

![](assets/libre-caslon-finding_reg_wght.gif)

Because the matching font weight seems to change based on the medium and size tested, I'll do two things:

1. Keep things flexible by making my build script keep the original source, and allow a build-time selection of Roman weight
2. Start with the assumption that the correct Regular weight is somewhere between the test results – I'll choose the current `435` point as the value to export at, for now. 