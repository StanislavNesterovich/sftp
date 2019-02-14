#!/usr/bin/python
from ansible.module_utils.basic import *
import pysftp
import subprocess
import os

def connect(ftp_user, ftp_password, ftp_host):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    sftp = pysftp.Connection(host=ftp_host, username=ftp_user, password=ftp_password, cnopts=cnopts)
    sftp.timeout = 3600
    return sftp


def get_file_lftp(ftp_user, ftp_password, ftp_host, ftp_dvm_path, temp_dir):
    command = "lftp sftp://" + ftp_user + ":" + ftp_password + "@" + ftp_host + " -e " + "'get " + ftp_dvm_path + " -o " + temp_dir + "; bye'"
    os.system(command)
    return True


def get_size(sftp, ftp_dvm_path):
    size = sftp.sftp_client.stat(ftp_dvm_path)
    return size.st_size


def get_file(sftp, ftp_dvm_path, temp_dir):
    file = ftp_dvm_path.split("/")
    if temp_dir[-1] == "/":
        temp_dir += file[-1]
    else:
        temp_dir = temp_dir + "/" + file[-1]

    result = sftp.sftp_client.get(ftp_dvm_path, temp_dir)
    return result


def main():
  module = AnsibleModule(
    argument_spec=dict(
        ftp_user=dict(required=True, type='str',  no_log=True),
        ftp_password=dict(required=True, type='str', no_log=True),
        ftp_host=dict(required=True, type='str'),
        ftp_dvm_path=dict(required=True, type='str'),
        temp_dir=dict(required=False, type='str'),
        action=dict(required=True, type='str')
    ),
    supports_check_mode=True
  )
  if module.check_mode:
     module.exit_json(changed=False)

  ftp_host = module.params['ftp_host']
  ftp_dvm_path = module.params['ftp_dvm_path']
  ftp_user = module.params['ftp_user']
  ftp_password = module.params['ftp_password']
  action = module.params['action']
  temp_dir = module.params['temp_dir']

  if action == "get":
      sftp = connect(ftp_user, ftp_password, ftp_host)
      result = get_file(sftp, ftp_dvm_path, temp_dir)
      module.exit_json(changed=False, msg=result)
  elif action == "size":
      sftp = connect(ftp_user, ftp_password, ftp_host)
      result = get_size(sftp, ftp_dvm_path)
      module.exit_json(changed=False, size=result)
  elif action == "lftp":
      result = get_file_lftp(ftp_user, ftp_password, ftp_host, ftp_dvm_path, temp_dir)
      module.exit_json(changed=False, size=result)
  else:
      msg = "No set action"
      module.fail_json(failed=True, changed=False, msg=msg)

if __name__ == '__main__':
  main()
