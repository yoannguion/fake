Name:       fake
Version:    0.0.1
Release:    0%{?dist}
Summary:    fake
URL:        https://github.com/yoannguion/fake
License:     Apache 2.0

Source0:    fake.sh

%description
This package contains fake script.

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT/usr/bin

%files
/usr/bin/fake.sh
