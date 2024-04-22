#
# Conditional build:
%bcond_without	gtk3		# use GTK+3 instead of GTK+2
%bcond_without	appindicator	# libindicator support (only GTK+2 variant supported)

%if %{with gtk3}
%undefine	with_appindicator
%endif
Summary:	LXPanel - a lightweight X11 desktop panel
Summary(pl.UTF-8):	LXPanel - lekki panel pulpitu X11
Name:		lxpanel
Version:	0.10.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	c922d044789c3d7ae028f0e80dea18b0
URL:		http://www.lxde.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.12
BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
%{!?with_gtk3:BuildRequires:	keybinder-devel}
%{?with_gtk3:BuildRequires:	keybinder3-devel}
BuildRequires:	libfm-devel >= 1.2.0
%{?with_appindicator:BuildRequires:	libindicator-devel >= 0.3.0}
BuildRequires:	libiw-devel
BuildRequires:	libtool >= 2:2.2
%{!?with_gtk3:BuildRequires:	libwnck2-devel}
%{?with_gtk3:BuildRequires:	libwnck-devel}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	menu-cache-devel
BuildRequires:	pkgconfig
%{!?with_gtk3:BuildRequires:	pkgconfig(libfm-gtk) >= 1.2.0}
%{?with_gtk3:BuildRequires:	pkgconfig(libfm-gtk3) >= 1.2.0}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	lxmenu-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXPanel is a lightweight X11 desktop panel.

%description -l pl.UTF_8
LXPanel to lekki panel pulpitu X11.

%package libs
Summary:	LXPanel shared library
Summary(pl.UTF-8):	Biblioteka współdzielona LXPanelu
Group:		Libraries
Requires:	libfm >= 1.2.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}

%description libs
LXPanel shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona LXPanelu.

%package devel
Summary:	Header files for lxpanel plugins
Summary(pl.UTF-8):	Pliki nagłówkowe dla wtyczek lxpanelu
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libfm-devel >= 1.2.0
%{!?with_gtk3:Requires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:Requires:	gtk+3-devel >= 3.0.0}

%description devel
Header files for lxpanel plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla wtyczek lxpanelu.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_appindicator:--enable-indicator-support} \
	--disable-silent-rules \
	%{?with_gtk3:--enable-gtk3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lxpanel/liblxpanel.la

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/frp
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxpanel
%attr(755,root,root) %{_bindir}/lxpanelctl
%dir %{_libdir}/lxpanel/plugins
%dir %{_datadir}/lxpanel
%{_datadir}/lxpanel/images
%{_datadir}/lxpanel/ui
%{_datadir}/lxpanel/xkeyboardconfig
%dir %{_sysconfdir}/xdg/lxpanel
%dir %{_sysconfdir}/xdg/lxpanel/default
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/lxpanel/default/config
%dir %{_sysconfdir}/xdg/lxpanel/default/panels
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/lxpanel/default/panels/panel
%dir %{_sysconfdir}/xdg/lxpanel/two_panels
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/lxpanel/two_panels/config
%dir %{_sysconfdir}/xdg/lxpanel/two_panels/panels
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/lxpanel/two_panels/panels/bottom
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/lxpanel/two_panels/panels/top
%{_mandir}/man1/lxpanel.1*
%{_mandir}/man1/lxpanelctl.1*

%attr(755,root,root) %{_libdir}/lxpanel/plugins/batt.so
%attr(755,root,root) %{_libdir}/lxpanel/plugins/cpu.so
%attr(755,root,root) %{_libdir}/lxpanel/plugins/cpufreq.so
%attr(755,root,root) %{_libdir}/lxpanel/plugins/deskno.so
%if %{with appindicator}
# R: libindicator
%attr(755,root,root) %{_libdir}/lxpanel/plugins/indicator.so
%endif
%attr(755,root,root) %{_libdir}/lxpanel/plugins/kbled.so
# R: libfm-gtk
%attr(755,root,root) %{_libdir}/lxpanel/plugins/monitors.so
%attr(755,root,root) %{_libdir}/lxpanel/plugins/netstat.so
# R: libfm-gtk
%attr(755,root,root) %{_libdir}/lxpanel/plugins/netstatus.so
%attr(755,root,root) %{_libdir}/lxpanel/plugins/thermal.so
# R: alsa-lib libfm-gtk
%attr(755,root,root) %{_libdir}/lxpanel/plugins/volume.so
# R: curl-libs libxml2
%attr(755,root,root) %{_libdir}/lxpanel/plugins/weather.so
# R: libX11
%attr(755,root,root) %{_libdir}/lxpanel/plugins/xkb.so

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/lxpanel
%attr(755,root,root) %{_libdir}/lxpanel/liblxpanel.so.*.*.*
%attr(755,root,root) %{_libdir}/lxpanel/liblxpanel.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lxpanel/liblxpanel.so
%{_includedir}/lxpanel
%{_pkgconfigdir}/lxpanel.pc
