Name:       fake
Version:    0.0.1
Release:    0%{?dist}
Summary:    fake
URL:        https://github.com/yoannguion/fake


Source0:    fake.sh

%description
This package contains fake script.

%install
cp fake.sh /usr/bin

%files
/usr/bin/fake.sh
