from BOLHelper import AppTypes, BOLHelper, Languages

if __name__ == "__main__":
    i = 0

    BOLHelper.initInstance("demo@demo.com", "cicci0CICCI0_",
                                "main.py", "1.0",
                                AppTypes.Console, Languages.Python)
    bh = BOLHelper.getInstance()

    try:
        input("Press a key to continue..")
        y = 6/i

    except Exception as ex:
        bh.Send(ex)