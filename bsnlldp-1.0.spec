# Spec file for Big Switch Networks LLDP Agent.
#
# Copyright 2015, Big Switch Networks, Inc.
#
# Licensed under the Eclipse Public License, Version 1.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#        http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the
# License.
#

Name: bsnlldp
Version: 0.1.0
Release: 1%{?dist}
Summary: Big Switch Networks LLDP Agent

Group: System Environment/Daemons
License: EPL-1.0
URL: http://www.bigswitch.com
Source: bsnlldp.tar.gz

BuildRequires: bash, python, pkgconfig
Requires: 

%description
Big Switch Networks LLDP Agent is used to send LLDP packets with a 
pre-configured system description which is recognized by Big Cloud Fabric
and programs the port groups for the given machine.

%prep
%setup -q -n bsnlldp


%build

%install
install -p -D -m 0644 bsnlldp.service \
        $RPM_BUILD_ROOT%{_unitdir}/bsnlldp.service
install -p -D -m 0644 bsnlldp \
        $RPM_BUILD_ROOT/bin/bsn_lldp

%files
/bin/bsnlldp
%{_unitdir}/bsnlldp.service

%changelog

