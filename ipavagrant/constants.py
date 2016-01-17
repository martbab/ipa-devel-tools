#!/usr/bin/python3
# Author: Martin Basti
# See LICENSE file for license

import os


DEFAULT_CONFIG_FILENAME = os.path.expanduser("~/.ipa_vagrant_config.yaml")

RPMS_DIR = "rpms"
PROVISIONING_DIR = "provisioning"
VAGRANT_FILE = "Vagrantfile"
ANSIBLE_FILE = "ansible.yml"
CONTROLLER_SSH_KEY = "controller_rsa"
CONTROLLER_SSH_PUB_KEY = "controller_rsa.pub"
IP_ADDR_FIRST = 100

# please keep ABC order of keys
DEFAULT_CONFIG = dict(
    box="f23",
    ci_config_file="ipa-test-config.yaml",
    domain="ipa.test",
    ipa_ci_ad_admin_name="Administrator",
    ipa_ci_ad_admin_password="Secret123456",
    ipa_ci_admin_name="admin",
    ipa_ci_admin_password="Secret123",
    ipa_ci_debug=False,
    ipa_ci_dirman_dn="cn=Directory Manager",
    ipa_ci_dirman_password="Secret123",
    ipa_ci_dns_forwarder="10.34.78.1",
    ipa_ci_nis_domain="ipatest",
    ipa_ci_ntp_server="1.pool.ntp.org",
    ipa_ci_root_ssh_key_filename="/root/.ssh/id_rsa",
    ipa_ci_test_dir="/root/ipatests",
    memory_client=1024,
    memory_controller=1024,
    memory_server=2048,
    required_copr_repos=[
        "mkosek/freeipa-master"],
    required_packages=[
        "vim",
        "PyYAML",
        "haveged",
        "bind-dyndb-ldap"],
    selinux_enforcing=False,
)

box_mapping = {
    "f22": {"libvirt": { "override.vm.box": "f22",
                         "override.vm.box_url": "http://download.fedoraproject.org/pub/fedora/linux/releases/22/Cloud/x86_64/Images/Fedora-Cloud-Base-Vagrant-22-20150521.x86_64.vagrant-libvirt.box",
                       },
            "virtualbox": { "override.vm.box": "box-cutter/fedora22", },
            "ovirt3": { "domain.template": "ipa-Fedora-23-x86_64-developer-brq", },
    },
    "f23": {"libvirt": { "override.vm.box": "f23",
                         "override.vm.box_url": "http://download.fedoraproject.org/pub/fedora/linux/releases/23/Cloud/x86_64/Images/Fedora-Cloud-Base-Vagrant-23-20151030.x86_64.vagrant-libvirt.box",
                       },
            "virtualbox": { "override.vm.box": "box-cutter/fedora23", },
            "ovirt3": { "domain.template": "ipa-Fedora-22-x86_64-developer-brq", },
    },
}