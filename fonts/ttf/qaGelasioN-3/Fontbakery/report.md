## Fontbakery report

Fontbakery version: 0.7.15

<details>
<summary><b>[3] Gelasio-Bold.ttf</b></summary>
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

Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[3] Gelasio-BoldItalic.ttf</b></summary>
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

Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[3] Gelasio-Italic.ttf</b></summary>
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

Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[3] Gelasio-Medium.ttf</b></summary>
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
Glyph name: lessequal	Contours detected: 4	Expected: 2
Glyph name: greaterequal	Contours detected: 4	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: less	Contours detected: 3	Expected: 1
Glyph name: greater	Contours detected: 3	Expected: 1
Glyph name: asciicircum	Contours detected: 2	Expected: 1
Glyph name: lessequal	Contours detected: 4	Expected: 2
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: less	Contours detected: 3	Expected: 1
Glyph name: greaterequal	Contours detected: 4	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: greater	Contours detected: 3	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[8] Gelasio-MediumItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value.</summary>

* [com.google.fonts/check/fsselection](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection)

* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection ITALIC bit should be set. [code: bad-ITALIC]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking head.macStyle value.</summary>

* [com.google.fonts/check/mac_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style)
<pre>--- Rationale ---

The values of the flags on the macStyle entry on the &#x27;head&#x27; OpenType table that
describe whether a font is bold and/or italic must be coherent with the actual
style of the font as inferred by its filename.


</pre>

* 🔥 **FAIL** head macStyle ITALIC bit should be set. [code: bad-ITALIC]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Gelasio Medium" but got "Gelasio Medium Italic". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/subfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname)

* 🔥 **FAIL** SUBFAMILY_NAME for Win "Regular" must be "Italic" [code: bad-familyname]

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

Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---

According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.

After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.

[1]
https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179


</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Gelasio Medium Italic' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[3] Gelasio-Regular.ttf</b></summary>
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

Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[3] Gelasio-SemiBold.ttf</b></summary>
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
Glyph name: lessequal	Contours detected: 4	Expected: 2
Glyph name: greaterequal	Contours detected: 4	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: less	Contours detected: 3	Expected: 1
Glyph name: greater	Contours detected: 3	Expected: 1
Glyph name: asciicircum	Contours detected: 2	Expected: 1
Glyph name: lessequal	Contours detected: 4	Expected: 2
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: less	Contours detected: 3	Expected: 1
Glyph name: greaterequal	Contours detected: 4	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: greater	Contours detected: 3	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>
<details>
<summary><b>[8] Gelasio-SemiBoldItalic.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value.</summary>

* [com.google.fonts/check/fsselection](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection)

* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection ITALIC bit should be set. [code: bad-ITALIC]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking head.macStyle value.</summary>

* [com.google.fonts/check/mac_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style)
<pre>--- Rationale ---

The values of the flags on the macStyle entry on the &#x27;head&#x27; OpenType table that
describe whether a font is bold and/or italic must be coherent with the actual
style of the font as inferred by its filename.


</pre>

* 🔥 **FAIL** head macStyle ITALIC bit should be set. [code: bad-ITALIC]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Gelasio SemiBold" but got "Gelasio SemiBold Italic". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/subfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname)

* 🔥 **FAIL** SUBFAMILY_NAME for Win "Regular" must be "Italic" [code: bad-familyname]

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

Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: fl	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: fi	Contours detected: 1	Expected: 3
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---

According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.

After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.

[1]
https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179


</pre>

* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Gelasio SemiBold Italic' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 26 | 464 | 49 | 538 | 0 |
| 0% | 1% | 2% | 43% | 5% | 50% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
