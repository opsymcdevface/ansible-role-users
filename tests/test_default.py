from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_group(Group):
    group = Group("sysadmins")
    assert group.exists


def test_users(User):
    users = ['rj']
    for u in users:
        user = User(u)
        assert user.exists
        assert "sysadmins" in user.groups
        assert "wheel" in user.groups
