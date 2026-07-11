%global tl_name almfixed
%global tl_revision 35065

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.92
Release:	%{tl_revision}.1
Summary:	Arabic-Latin Modern Fixed extends TeX-Gyre Latin Modern Mono 10 Regular to fu...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/almfixed
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/almfixed.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/almfixed.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Arabic-Latin Modern Fixed is an extension of TeX-Gyre Latin Modern Mono
10 Regular. Every glyph and OpenType feature of the Latin Modern Mono
has been retained, with minor improvements. On the other hand, we have
changed the vertical metrics of the font. Although the Arabic script is
designed to use the same x-size as Latin Modern Mono, the former script
needs greater ascender and descender space. Every Arabic glyph in each
Unicode-code block is supported (up to Unicode 7.0): Arabic, Arabic
Supplement, Arabic Extended, Arabic Presentation-Forms A, and Arabic
Presentation-Forms B. There are two versions of the font: otf and ttf.
The ?penType version is for print applications (and usually the default
for TeX). The TrueType version is for on-screen applications such as
text editors. Hinting in the ttf version is much better for on-screen,
at least on Microsoft Windows. The unique feature of Arabic-Latin Modern
is its treatment of vowels and diacritics. Each vowel and diacritic (ALM
Fixed contains a total of 68 such glyphs) may now be edited horizontally
within any text editor or processor. The author believes this is the
very first OpenType Arabic font ever to have this capability. Editing
complex Arabic texts will now be much easier to input and to proofread.

