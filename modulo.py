import subprocess

def pam_sm_authenticate(pamh, flags, argv):
        usuario = pamh.get_user(None)
        resultado = ""
        try:
                resultado = subprocess.check_output(['/bin/grep', usuario, '/etc/passwd'])
                return pamh.PAM_SUCCESS
        except:
                return pamh.PAM_AUTH_ERR    #Cambiar variable por una apropiada

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS


