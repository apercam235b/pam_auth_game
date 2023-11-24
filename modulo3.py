import subprocess

def pam_sm_authenticate(pamh, flags, argv):
        juego = str(input('Ingresa piedra, papel o tijera: '))
        result = subprocess.run(["python3", "/root/juego.py",juego], check=False,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        variable_juego = result.returncode
        print(variable_juego)
        if (variable_juego == 1):
                print('Has acertado, has conseguido logearte')
                return pamh.PAM_SUCCESS
        print('Error al jugar, has sido expulsado.')
        return pamh.PAM_AUTH_ERR    #Cambiar variable por una apropiada

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam__sm_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS


