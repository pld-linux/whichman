Summary:	This package holds THREE little search utilities
Summary(pl):	Pakiet zawiera TRZY ma³e narzêdzia do wyszukiwania
Name:		whichman
Version:	1.9
Release:	1
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://www.linuxfocus.org/~guido.socher/%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS.patch
URL:		http://www.linuxfocus.org/~guido.socher/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fault-tolerant man-page, file and "which-like" command finders. They
all work by computing the Levenshtein Distance between the search
pattern and the man-page, file, or command name.

%description -l pl
Odporne na b³êdy wyszukiwarki stron man, plików i komend. Dzia³aj±
obliczaj±c Odleg³o¶æ Levenshteina pomiêdzy wzorcem wyszukiwania a
nazw± strony man, pliku czy komendy.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf README whichman-1.9.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
