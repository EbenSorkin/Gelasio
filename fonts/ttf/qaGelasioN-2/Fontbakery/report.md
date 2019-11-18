## Fontbakery report

Fontbakery version: 0.7.15

<details>
<summary><b>[9] Gelasio-Bold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('AE', 2125, 389)
	* ('AEacute', 2125, 389)
	* ('t', 793, 89)
	* ('uni0163', 793, 89)
	* ('uni021B', 793, 89)
	* ('uni1E6D', 793, 89)
	* ('uni1E6F', 793, 89) and ('uni1E6B', 793, 89)

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[14] Gelasio-BoldItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value.</summary>

* [com.google.fonts/check/fsselection](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection)

* 🔥 **FAIL** OS/2 fsSelection BOLD bit should be set. [code: bad-BOLD]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking head.macStyle value.</summary>

* [com.google.fonts/check/mac_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style)
<pre>--- Rationale ---

The values of the flags on the macStyle entry on the &#x27;head&#x27; OpenType table that
describe whether a font is bold and/or italic must be coherent with the actual
style of the font as inferred by its filename.


</pre>

* 🔥 **FAIL** head macStyle BOLD bit should be set. [code: bad-BOLD]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Gelasio" but got "Gelasio Bold". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/subfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname)

* 🔥 **FAIL** SUBFAMILY_NAME for Win "Italic" must be "Bold Italic" [code: bad-familyname]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname)

* 🔥 **FAIL** Font style is "BoldItalic" and, for that reason, it is not expected to have a [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] entry! [code: ribbi]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('uni1EAE', 1236, 2355)
	* ('L', 1353, 514)
	* ('Lacute', 1353, 514)
	* ('uni013B', 1353, 514)
	* ('uni1E36', 1353, 514)
	* ('uni1E3A', 1353, 514)
	* ('S', 1261, 1419)
	* ('Sacute', 1261, 1419)
	* ('uni1E64', 1261, 1419)
	* ('Scedilla', 1261, 1419) and 15 more.

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[9] Gelasio-Italic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('uni1EAE', 1172, 2339)
	* ('V', 1565, 1379)
	* ('two', 1011, 1032)
	* ('two.osf', 1011, 1032)
	* ('quotedbl', 947, 1620)
	* ('uni20BA', 1209, 551)
	* ('estimated', 852, 1359)
	* ('uni02CB', 33.523000000000025, 1154.0)
	* ('breve', 623.5754999999999, 1549.0) and ('uni0312.case', 437.552, 1696.0)

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[9] Gelasio-Medium.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: asciicircum	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: infinity	Contours detected: 2	Expected: 3
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: infinity	Contours detected: 2	Expected: 3
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: asciicircum	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('Ibreve', 757, 1961)
	* ('Ibreve', 757, 1845)
	* ('uni020A', 757, 1686)
	* ('uni020A', 757, 1570)
	* ('uni1E64', 556, 2395)
	* ('uni1E64', 619, 2395)
	* ('uni1E64', 681, 2395)
	* ('uni01D7', 1033, 2394)
	* ('uni01D7', 1059, 2394)
	* ('uni01D7', 1078, 2394) and 111 more.

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[9] Gelasio-MediumItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('Aringacute', 1436, 2279)
	* ('Aringacute', 1462, 2279)
	* ('Aringacute', 1507, 2279)
	* ('uni01C5', 2610, 1528)
	* ('uni1EC0', 1466, 1773)
	* ('uni020A', 920, 1743)
	* ('uni020A', 920, 1655)
	* ('uni020A', 920, 1620)
	* ('uni1ED2', 1526, 1773)
	* ('Racute', 1092, 2000) and 84 more.

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[9] Gelasio-Regular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('uni01F2', 2385, 356)
	* ('uni01C5', 2385, 356)
	* ('R', 593, 1429)
	* ('uni0156', 593, 1429)
	* ('uni1E5A', 593, 1429)
	* ('uni1E5E', 593, 1429)
	* ('uni01F3', 2027, 356)
	* ('uni01C6', 2027, 356)
	* ('z', 851, 356)
	* ('zacute', 851, 356) and 3 more.

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[9] Gelasio-SemiBold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: asciicircum	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: infinity	Contours detected: 2	Expected: 3
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: infinity	Contours detected: 2	Expected: 3
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: asciicircum	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('IJ', 1992, 1379)
	* ('IJ', 1992, 1368)
	* ('IJ', 1992, 1333)
	* ('IJ_acutecomb', 1992, 1379)
	* ('IJ_acutecomb', 1992, 1368)
	* ('IJ_acutecomb', 1992, 1333)
	* ('Ibreve', 87, 1845)
	* ('uni01CF', 77, 1961)
	* ('uni020A', 87, 1686)
	* ('uni01CA', 2787, 1379) and 89 more.

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>
<details>
<summary><b>[9] Gelasio-SemiBoldItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---

This check finds which version of ttfautohint was used, by inspecting name
table entries and then finds which version of ttfautohint is currently
installed in the system.


</pre>

* 🔥 **FAIL** Failed to parse ttfautohint version values: installed = '1.8.3'; used_in_font = '1.7.19-72a1' [code: parse-error]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---

Hinted fonts must have head table flag bit 3 set.

Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.

Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;


</pre>

* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenvpython3 -m venv venv
# activate virtualenvsource venv/bin/activate
# install gftoolspip install git+https://www.github.com/googlefonts/tools [code: bad-flags]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---

A font&#x27;s winAscent and winDescent values should be greater than the head
table&#x27;s yMax, abs(yMin) values. If they are less than these values, clipping
can occur on Windows platforms
(https://github.com/RedHatBrand/Overpass/issues/33).

If the font includes tall/deep writing systems such as Arabic or Devanagari,
the winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.

When the win Metrics are significantly greater than the upm, the linespacing
can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead.
This means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).


</pre>

* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---

Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.

The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.

But value of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.

Another acceptable value is 2000. Since TT outlines are all integers (no
floats), then instances in a VF suffer rounding compromises, and therefore a
1000 UPM is to small because it forces too many such compromises.

Therefore 2000 is a good &#x27;new VF standard&#x27;, because 2000 is a simple 2x
conversion from existing fonts drawn on a 1000 UPM, and anyone who knows what
10 units can do for 1000 UPM will know what 20 units does too.

Additionally, values above 2048 would result in filesize increases with not
much added benefit.


</pre>

* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: uni1E1D	Contours detected: 4	Expected: 3
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: uni02BA	Contours detected: 1	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)

* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases. [code: rfn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* ⚠ **WARN** The following glyphs have coordinates which are out of bounds:
	* ('uni1EA8', 1599, 2096)
	* ('uni1EA8', 1599, 2046)
	* ('uni1EA8', 1599, 1970)
	* ('Atilde', 748, 1867)
	* ('Atilde', 815, 1867)
	* ('Atilde', 861, 1867)
	* ('uni1EBC', 693, 1867)
	* ('uni1EBC', 760, 1867)
	* ('uni1EBC', 806, 1867)
	* ('Itilde', 401, 1867) and 106 more.

This happens a lot when points are not extremes, which is usually bad. However, fixing this alert by adding points on extremes may do more harm than good, especially with italics, calligraphic-script, handwriting, rounded and other fonts. So it is common to ignore this message. [code: points-out-of-bounds]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 37 | 40 | 456 | 41 | 511 | 0 |
| 0% | 3% | 4% | 42% | 4% | 47% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
