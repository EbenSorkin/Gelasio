## Fontbakery report

Fontbakery version: 0.7.10

<details>
<summary><b>[5] Gelasio-Bold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information.

</details>
<br>
</details>
<details>
<summary><b>[6] Gelasio-Medium.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: asciicircum	Contours detected: 2	Expected: 1
Glyph name: lessequal	Contours detected: 4	Expected: 2
Glyph name: greaterequal	Contours detected: 4	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: less	Contours detected: 3	Expected: 1
Glyph name: greater	Contours detected: 3	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information.

</details>
<br>
</details>
<details>
<summary><b>[5] Gelasio-Regular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information.

</details>
<br>
</details>
<details>
<summary><b>[6] Gelasio-SemiBold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]
* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'" [code: bad-notice-format]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2599, but got 2510 instead [code: ascent]

</details>
<details>
<summary>⚠ <b>WARN:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
* ⚠ **WARN** Even though unitsPerEm (2048) in this font is reasonable. It is strongly advised to consider changing it to 2000, since it will likely improve the quality of Variable Fonts by avoiding excessive rounding of coordinates on interpolations. [code: legacy-value]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: asciicircum	Contours detected: 2	Expected: 1
Glyph name: lessequal	Contours detected: 4	Expected: 2
Glyph name: greaterequal	Contours detected: 4	Expected: 2
Glyph name: hungarumlaut	Contours detected: 1	Expected: 2
Glyph name: dieresis	Contours detected: 1	Expected: 2
Glyph name: less	Contours detected: 3	Expected: 1
Glyph name: greater	Contours detected: 3	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/rfn)
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.
* ⚠ **WARN** Name table entry ("Copyright (c) 2013-2018, Sorkin Type Co with Reserved Font Name 'Gelasio'") contains "Reserved Font Name". This is an error except in a few specific rare cases.

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information.

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS |
|:-----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 14 | 234 | 25 | 270 |
| 0% | 1% | 3% | 42% | 5% | 49% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
