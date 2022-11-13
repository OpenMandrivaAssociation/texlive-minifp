Name:		texlive-minifp
Version:	32559
Release:	1
Summary:	Fixed-point real computations to 8 decimals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/minifp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minifp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides basic arithmetic operations to 8 decimal
places for plain TeX or LaTeX. Results are exact when they fit
within the digit limits. Along with the basic package is an
optional extension that adds computation of sin, cos, log,
sqrt, exp, powers and angles. These are also exact when
theoretically possible and are otherwise accurate to at least 7
decimal places. In addition, the package provides a stack-based
programing environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/minifp/mfpextra.tex
%{_texmfdistdir}/tex/generic/minifp/minifp.sty
%doc %{_texmfdistdir}/doc/generic/minifp/README
%doc %{_texmfdistdir}/doc/generic/minifp/minifp.pdf
%doc %{_texmfdistdir}/doc/generic/minifp/test1.tex
%doc %{_texmfdistdir}/doc/generic/minifp/test2.tex
#- source
%doc %{_texmfdistdir}/source/generic/minifp/minifp.dtx
%doc %{_texmfdistdir}/source/generic/minifp/minifp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
