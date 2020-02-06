import pickle
def IWIQ_update(list):
    filew = open("IWIQ.files", "wb")
    pickle.dump(list, filew)
    filew.close()
def IWIQ_get():
    filer = open("IWIQ.files", "rb")
    list = pickle.load(filer)
    filer.close()
    return list
