Summary:	LZMA Encoder/Decoder
Summary(pl.UTF-8):	Koder/Dekoder LZMA
Name:		p7lzma
Version:	4.57
Release:	1
License:	CPL/LGPL
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/p7zip/p7zip_%{version}_src_all.tar.bz2
# Source0-md5:	773f78d8b297eb858626667d4dfa93c7
Patch0:		%{name}-quiet.patch
Patch1:		%{name}-makefile.patch
URL:		http://www.7-zip.org/sdk.html
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZMA is default and general compression method of 7z format in 7-Zip
program. LZMA provides high compression ratio and very fast
decompression, so it is very suitable for embedded applications. For
example, it can be used for ROM (firmware) compressing.

LZMA features:

- Compressing speed: 500 KB/s on 1 GHz CPU
- Decompressing speed:
  - 8-12 MB/s on 1 GHz Intel Pentium 3 or AMD Athlon.
  - 500-1000 KB/s on 100 MHz ARM, MIPS, PowerPC or other simple RISC
    CPU.
- Small memory requirements for decompressing: 8-32 KB + dictionary
  size
- Small code size for decompressing: 2-8 KB (depending from speed
  optimizations)

%description -l pl.UTF-8
LZMA jest domyślnym i ogólnym algorytmem kompresji formatu 7z
stosowanego przez 7-Zip. LZMA zapewnia wysoki stopień kompresji i
bardzo szybką dekompresję, więc nadaje się do zastosowań
osadzonych. Przykładowo, może być użyty do kompresji ROM-u
(firmware'u).

Cechy LZMA:

- Szybkość kompresowania: 500 KB/s na 1 GHz procesorze,
- Szybkość dekompresowania:
  - 8-12 MB/s na 1 GHz Pentium 3 lub Athlonie,
  - 500-1000 KB/s na 100 MHz procesorach ARM, MIPS, PowerPC lub innych
    prostych RISC-ach,
- Mała ilość pamięci potrzebna do dekompresowania: 8-32 KB +
  rozmiar słownika,
- Mały rozmiar kodu dekompresującego: 2-8 KB (w zależności od
  opcji optymalizacji).

%prep
%setup -q -n p7zip_%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
cd CPP/7zip/Compress/LZMA_Alone
%{__make} -f makefile \
	CXX="%{__cxx}" \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

install CPP/7zip/Compress/LZMA_Alone/lzma $RPM_BUILD_ROOT%{_bindir}/p7lzma

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
