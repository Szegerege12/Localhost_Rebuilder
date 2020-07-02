import os
from flask_restplus import Resource
import subprocess
import shutil

class CronJob(Resource):
    def get(self, key, domain, repo):
        repo = 'Przemocny/green-djinn-gatsby.git'
        domain = 'greendjinn.page.localhost-group.com'
        git_command = ''

        abs_path_mydewil = '/usr/home/VPPoland/domains/'+domain+'/public_nodejs/public'

        # repo_folder = repo.split('/')[-1].split('.')[0]

        # # if os.path.exists('./gatsby-repo'):
        # #     shutil.rmtree('./gatsby-repo')

        # cwd = os.path.join(os.getcwd(), repo_folder)
        # # subprocess.check_call('eval $(ssh-agent -s)', shell=True)
        # # subprocess.check_call('ssh-add id_rsa', shell=True)
        # subprocess.run(f'git clone git@github.com:{repo} {repo_folder}', shell=True)
        # # subprocess.check_call('elav $(ssh-agent -k)', shell=True)

        # subprocess.Popen('npm install && npm install react && npm install gatsby && gatsby build', cwd=cwd, shell=True).wait()
        
        # shutil.rmtree('../public_tests/')
        # shutil.move(f'./{repo_folder}/public', '../public_test/')