import os, configparser, paramiko, sys

class Main(object):

    service_commands= {
    'DOCKER_STATUS': {'COMMAND': 'service docker status', 'FORMAT': ''},
    'DOCKER_COMPOSE_STATUS': 'service docker-compose status'
    }
    config_object = None

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('./config.ini')
    
    def _connect(self) -> None:
        k = paramiko.RSAKey.from_private_key_file(self.config['DEFAULT']['ssh'])
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.config['DEFAULT']['host'], username=self.config['DEFAULT']['user'], pkey=k)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls -la")
        print(ssh_stdout.read())
        print(ssh_stderr.read())

    def print(self) -> None:
        #print(self.service_commands)
        print(self.config)
        print(self.config['DEFAULT'])
        foo = self.config['DEFAULT']['host']
        print(foo)

    def list(self):
        return []
    
    def _format_ls():
        pass

    def run(self) -> None:                 
        for command in self.service_commands:
            print(os.system(self.service_commands[command]))
            #stat = os.system(services[service])
            #print(stat)
        self._connect()

if __name__ == "__main__" :
    foo = Main()
    foo.print()
    #foo.run()