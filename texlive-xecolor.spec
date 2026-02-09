Name:		texlive-xecolor
Epoch:		1
Version:	77677
Release:	1
Summary:	Support for color in XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xecolor
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecolor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a simple package which defines about 140 different
colours using XeTeX's colour feature. The colours can be used
in bidirectional texts without any problem.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xecolor/xecolor.sty
%doc %{_texmfdistdir}/doc/xelatex/xecolor/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
