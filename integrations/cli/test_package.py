from common import exec_command


def test_package():
    returncode, stdout, stderr = exec_command(['dcos', 'package', '--help'])

    assert returncode == 0
    assert stdout == b"""Usage:
    dcos package configure <package_name>
    dcos package info
    dcos package install <package_name>
    dcos package list
    dcos package search <query>
    dcos package sources
    dcos package uninstall <package_name>
    dcos package update

Options:
    -h, --help          Show this screen
    --version           Show version

Configuration:
    [package]
    # Path to the local package cache.
    cache_dir = "/var/dcos/cache"

    # List of package sources, in search order.
    #
    # Three protocols are supported:
    #   - Local file
    #   - HTTPS
    #   - Git
    sources = [
      "file:///Users/me/test-registry",
      "https://my.org/registry",
      "git://github.com/mesosphere/universe.git"
    ]
"""
    assert stderr == b''


def test_info():
    returncode, stdout, stderr = exec_command(['dcos', 'package', 'info'])

    assert returncode == 0
    assert stdout == b'Install and manage DCOS software packages\n'
    assert stderr == b''


def test_version():
    returncode, stdout, stderr = exec_command(['dcos', 'package', '--version'])

    assert returncode == 0
    assert stdout == b'dcos-package version 0.1.0\n'
    assert stderr == b''


def test_sources_list():
    returncode, stdout, stderr = exec_command(['dcos', 'package', 'sources'])

    assert returncode == 0
    assert stdout == b"""c3f1a0df1d2068e6b11d40224f5e500d3183a97e \
git://github.com/mesosphere/universe.git
"""
    assert stderr == b''
