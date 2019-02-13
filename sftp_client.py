import pysftp

ftp_user = "seko0313"
ftp_password = "wup69tyUb"
ftp_host = "ftpcn.netcracker.com"

def get_size(ftp_user, ftp_password, ftp_host):

    path = "MANO_DVM_Release_10.1_rc004_6.tar.gz"
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    sftp = pysftp.Connection(host=ftp_host, username=ftp_user, password=ftp_password, cnopts=cnopts)
    #sftp.cwd('/Corp/SandboxBS.Builds/Release/product/prod.inmrnd.mano/deployment-vm/release_10.1_20190131-102258/generic1.0/')
    size = sftp.sftp_client.stat('/Corp/SandboxBS.Builds/Release/product/prod.inmrnd.mano/deployment-vm/release_10.1_20190131-102258/generic1.0/MANO_DVM_Release_10.1_rc004_6.tar.gz')
    return size.st_size

print get_size(ftp_user, ftp_password, ftp_host)