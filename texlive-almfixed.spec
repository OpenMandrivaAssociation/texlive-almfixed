Name:		texlive-almfixed
Version:	35065
Release:	2
Summary:	Arabic-Latin Modern Fixed extends TeX-Gyre Latin Modern Mono 10 Regular to full Arabic Unicode support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/almfixed
License:	gfl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/almfixed.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/almfixed.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Arabic-Latin Modern Fixed is an extension of TeX-Gyre Latin
Modern Mono 10 Regular. Every glyph and OpenType feature of the
Latin Modern Mono has been retained, with minor improvements.
On the other hand, we have changed the vertical metrics of the
font. Although the Arabic script is designed to use the same
x-size as Latin Modern Mono, the former script needs greater
ascender and descender space. Every Arabic glyph in each
Unicode-code block is supported (up to Unicode 7.0): Arabic,
Arabic Supplement, Arabic Extended, Arabic Presentation-Forms
A, and Arabic Presentation-Forms B. There are two versions of
the font: otf and ttf. The ?penType version is for print
applications (and usually the default for TeX). The TrueType
version is for on-screen applications such as text editors.
Hinting in the ttf version is much better for on-screen, at
least on Microsoft Windows. The unique feature of Arabic-Latin
Modern is its treatment of vowels and diacritics. Each vowel
and diacritic (ALM Fixed contains a total of 68 such glyphs)
may now be edited horizontally within any text editor or
processor. The author believes this is the very first OpenType
Arabic font ever to have this capability. Editing complex
Arabic texts will now be much easier to input and to proofread.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/almfixed
%{_texmfdistdir}/fonts/opentype/public/almfixed
%doc %{_texmfdistdir}/doc/fonts/almfixed

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
