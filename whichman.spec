Summary:	This package holds THREE little search utilities
Summary(pl):	Pakiet zawiera TRZY ma�e narz�dzia do wyszukiwania
Name:		whichman
Version:	2.4
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://pepper.linuxfocus.org/~guido/%{name}-%{version}.tar.gz
# Source0-md5:	cc3d35f26bbd8bf99f4f16b276384333
URL:		http://pepper.linuxfocus.org/~guido/index.html#whichman
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fault-tolerant man-page, file and "which-like" command finders. They
all work by computing the Levenshtein Distance between the search
pattern and the man-page, file, or command name.

%description -l pl
Odporne na b��dy wyszukiwarki stron man, plik�w i polece�. Dzia�aj�
obliczaj�c odleg�o�� Levenshteina pomi�dzy wzorcem wyszukiwania a
nazw� strony man, pliku czy polecenia.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
