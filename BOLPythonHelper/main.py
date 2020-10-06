from BOLHelper import BOLHelper

if __name__ == "__main__":
    i = 0

    bh = BOLHelper.getInstance("demo@demo.com", "cicci0CICCI0_")

    try:
        input("Press a key to continue..")
        y = 6/i

    except Exception as ex:
        bh.Send(ex)