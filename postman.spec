Name:          postman
Version:       10.18.1
Release:       1%{?dist}
Summary:       Postman
License:       Apache 2.0
URL:           https://www.postman.com/
Packager:      Khalid Alharisi <coder966@gmail.com>


Source0:       https://dl.pstmn.io/download/latest/linux_64
Source1:       https://raw.githubusercontent.com/coder966/postman-rpm/master/postman.desktop


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}


%global build_id 10.18.1


%description
Postman




%prep


# Postman/app is the dir inside the tar
%setup -q -n Postman/app


%build



%install


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 icons/icon_128x128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}




%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*




%changelog
* Fri Sep 15 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.1
- Update to 10.18.1

* Wed Sep 13 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.4
- Update to 10.17.4

* Tue Sep 12 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.0
- Update to 10.18.0

* Fri Aug 25 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.4
- Update to 10.17.4

* Tue Aug 22 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.3
- Update to 10.17.3


* Tue Aug 18 2023 coder966 <coder966@gmail.com> - 10.17.0
- Initial Release
