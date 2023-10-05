import paramiko
import time
from faker import Faker


class SSH:
    # fake = Faker()

    def __init__(self, host):
        self.ssh = paramiko.SSHClient()
        self.host = host

    def connect(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname="10.130.6.11", username='pamuser', password='1q2w3e4r5t')
        return self.ssh

    def close_connection(self):
        self.ssh.close()

    def ssh_send_command(self, fake_username) -> str:
        stdin, stdout, stderr = self.ssh.exec_command(f'sudo useradd -p {fake_username} -m {fake_username}')
        print(fake_username)
        return ''.join(stdout.readlines())

    # def ssh_send_command(self) -> str:
    #     fake_username = self.fake.user_name()
    #     stdin, stdout, stderr = self.ssh.exec_command(f'sudo useradd -p {fake_username} -m {fake_username}')
    #     print(fake_username)
    #     return ''.join(stdout.readlines())









