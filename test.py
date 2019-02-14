import subprocess
import os
ftp_user = "seko0313"
ftp_password = "wup69tyUb"
ftp_host =  "ftpcn.netcracker.com"
ftp_dvm_path = "/Corp/SandboxBS.Builds/Release/product/prod.inmrnd.mano/deployment-vm/release_10.1_20190131-102258/generic1.0/MANO_DVM_Release_10.1_rc004_6.tar.gz"
temp_dir = "/tmp"
#command = "lftp sftp://" + ftp_user + ":" + ftp_password + "@" + ftp_host + " -e " + "'get " + ftp_dvm_path + " -o " + temp_dir + "; bye'"
command = "lftp sftp://" + ftp_user + ":" + ftp_password + "@" + ftp_host + "; " + "get " + ftp_dvm_path  + "; bye"
command_get = "get " + ftp_dvm_path  + ";"
command_bye = "bye"

def get_file_lftp(ftp_user, ftp_password, ftp_host, ftp_dvm_path, temp_dir):
    command = "lftp sftp://" + ftp_user + ":" + ftp_password + "@" + ftp_host + " -e " + "'get " + ftp_dvm_path + " -o " + temp_dir + "; bye'"
    message = subprocess.check_output(command, stderr=subprocess.STDOUT)
    message = subprocess.check_output(command_get, stderr=subprocess.STDOUT)
    message = subprocess.check_output(command_get, stderr=subprocess.STDOUT)
    return message

print get_file_lftp(ftp_user, ftp_password, ftp_host, ftp_dvm_path, temp_dir)

