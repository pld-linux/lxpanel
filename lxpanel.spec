Summary:	LXPanel is a lightweight X11 desktop panel
Name:		lxpanel
Version:	0.5.12
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	30def9a0aa3c517e102295e8a7bc17fd
Patch0:		%{name}-werror.patch
Patch1:		%{name}-automake.patch
URL:		http://wiki.lxde.org/en/LXPanel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.12
BuildRequires:	alsa-lib-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool
BuildRequires:	libiw-devel
BuildRequires:	libwnck2-devel
BuildRequires:	libtool
BuildRequires:	menu-cache-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXPanel is a lightweight X11 desktop panel.

%package devel
Summary:	Header files for lxpanel library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lxpanel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lxpanel library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lxpanel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoheader}
%{__libtoolize}
%{__intltoolize}
%{__automake}
%{__autoconf}
%configure
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK,tt_RU}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxpanel
%attr(755,root,root) %{_bindir}/lxpanelctl
%dir %{_libdir}/lxpanel
%dir %{_libdir}/lxpanel/plugins
%attr(755,root,root) %{_libdir}/lxpanel/plugins/*.so
%{_mandir}/man1/lxpanel.1*
%{_mandir}/man1/lxpanelctl.1*

%dir %{_datadir}/lxpanel
%{_datadir}/lxpanel/xkeyboardconfig/*.cfg
%{_datadir}/lxpanel/profile
%{_datadir}/lxpanel/ui

%dir %{_datadir}/lxpanel/images
%{_datadir}/lxpanel/images/*.png

%dir %{_datadir}/lxpanel/images/xkb-flags
# TODO: lang tags here
%{_datadir}/lxpanel/images/xkb-flags/*.png

%dir %{_datadir}/lxpanel/xkeyboardconfig
%{_datadir}/lxpanel/xkeyboardconfig/*.cfg

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lxpanel
%{_includedir}/lxpanel/plugin.h
%{_pkgconfigdir}/lxpanel.pc
