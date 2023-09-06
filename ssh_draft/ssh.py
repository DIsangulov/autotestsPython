import paramiko


class SSH:
    def __init__(self, host):
        self.ssh = paramiko.SSHClient()
        self.host = host

    def connect(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.host, username='pamuser', password='1q2w3e4r5t')
        return self.ssh

    def close_connection(self):
        self.ssh.close()

    def ssh_send_command(self, command) -> str:
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return ''.join(stdout.readlines())

    def sudo(self, password):
        stdin, stdout, stderr = self.ssh.exec_command('sudo -s')
        # Если выполнение команды sudo требует ввода пароля
        if 'Password:' in stdout.read().decode():
            stdin.write(password + '\n')
            stdin.flush()
        stdin.flush()
        output = stdout.read().decode()
        return output







