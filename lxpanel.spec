Summary:	LXPanel is a lightweight X11 desktop panel
Name:		lxpanel
Version:	0.5.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	3c6b5498b5f4109c3913b10a66809fe6
URL:		http://www.lxde.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	menu-cache-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXPanel is a lightweight X11 desktop panel.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxpanel*
%dir %{_includedir}/lxpanel
%{_includedir}/lxpanel/plugin.h
%dir %{_libdir}/lxpanel
%attr(755,root,root) %{_libdir}/lxpanel/plugins/*.so
%{_pkgconfigdir}/lxpanel.pc
%{_datadir}/lxpanel
%{_mandir}/man1/lxpanel*
