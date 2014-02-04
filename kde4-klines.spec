%define		_state		stable
%define		orgname		klines
%define		qtver		4.8.0

Summary:	Lines for KDE
Summary(pl.UTF-8):	Gra Lines dla KDE
Name:		kde4-%{orgname}
Version:	4.12.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d2e3ad884559b520b179de045dfad41a
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lines for KDE. The main rules of game is as simple as possible: you
move (using mouse) marbles from cell to cell and build lines
(horizontal, vertical or diagonal). When a line contains 5 or more
marbles - they are removed from the field and your score grows. After
each of your turns computer drops three more marbles onto the field.

%description -l pl.UTF-8
Gra Lines dla KDE. Podstawowe zasady gry są najprostsze jak to
możliwe: przesuwa się (przy użyciu muszy) klocki z pola na pole i
buduje linie (poziome, pionowe lub ukośne). Kiedy linia zawiera 5 lub
więcej klocków - są usuwane z pola i wynik wzrasta. Po każdym ruchu
gracza komputer zrzuca trzy dodatkowe klocki.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_desktopdir}/kde4/klines.desktop
%{_datadir}/config.kcfg/klines.kcfg
%{_datadir}/apps/klines
%{_iconsdir}/*/*/apps/klines.png
