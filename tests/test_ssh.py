
class TestSSH:

    def test_ssh_send_command(self, ssh):
        result = ssh.ssh_send_command('pwd')
        print(result)

    # def test_ssh_send_command(self, ssh):
    #     # ssh.ssh_send_command('sudo -s')
    #     # ssh.ssh_send_command('sudo adduser sapm')
    #     # ssh.ssh_send_command('sudo passwd sapm')
    #     # ssh.ssh_send_command('sapm')
    #     # ssh.ssh_send_command('sapm')

