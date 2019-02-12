#!/usr/bin/python
from ansible.module_utils.basic import *
import pysftp


def connect(ftp_user, ftp_password, ftp_host):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    sftp = pysftp.Connection(host=ftp_host, username=ftp_user, password=ftp_password, cnopts=cnopts)
    return sftp


def get_size(sftp):
    path = "MANO_DVM_Release_10.1_rc004_6.tar.gz"
    sftp.cwd('/Corp/SandboxBS.Builds/Release/product/prod.inmrnd.mano/deployment-vm/release_10.1_20190131-102258/generic1.0/')
    size = sftp.sftp_client.stat(path)
    return size.st_size


def get_file(sftp):
    path = "MANO_DVM_Release_10.1_rc004_6.tar.gz"
    sftp.cwd('/Corp/SandboxBS.Builds/Release/product/prod.inmrnd.mano/deployment-vm/release_10.1_20190131-102258/generic1.0/')
    result = sftp.sftp_client.get(path, "/tmp")
    return result


def main():
  module = AnsibleModule(
    argument_spec=dict(
        ftp_user=dict(required=True, type='str'),
        ftp_password=dict(required=True, type='str'),
        ftp_host=dict(required=True, type='str'),
        ftp_dvm_path=dict(required=True, type='str'),
        action=dict(required=True, type='str')
    ),
    supports_check_mode=True
  )
  if module.check_mode:
     return result

  ftp_host = module.params['ftp_host']
  ftp_dvm_path = module.params['ftp_dvm_path']
  ftp_user = module.params['ftp_user']
  ftp_password = module.params['ftp_password']
  action = module.params['action']

  if action == "get":
      sftp = connect(ftp_user, ftp_password, ftp_host)
      result = get_file(sftp)
      module.exit_json(changed=False, msg=result)
  elif action == "size":
      sftp = connect(ftp_user, ftp_password, ftp_host)
      result = get_size(sftp)
      module.exit_json(changed=False, size=result)
  else:
      msg = "No set action"
      module.fail_json(failed=True, changed=False, msg=msg)

if __name__ == '__main__':
  main()