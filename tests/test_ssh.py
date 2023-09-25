import time


class TestSSH:

    def test_ssh_send_command_adduser(self, ssh):
        ssh.ssh_send_command()
