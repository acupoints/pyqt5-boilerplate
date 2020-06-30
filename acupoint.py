from Acupoints.ResManager import ResManager
import sys

def remove_symbols(plain_text):
    "Remove numbers and symbols from ASCII"
    import string
    # del_estr = string.punctuation + string.digits
    del_estr = string.punctuation
    del_estr = del_estr.replace("_", "")
    replace = "_"*len(del_estr)
    tran_tab = str.maketrans(del_estr, replace)
    plain_text = plain_text.translate(tran_tab)

    return plain_text


arg_count = len(sys.argv)
rm = ResManager()

if arg_count == 2:
    if sys.argv[0] == "acupoint.py" and sys.argv[1].lower() == "purify":
        # Add a whitelist of class name prompts
        source_file = ".pylintrc"
        rm.write(source_file, "extension-pkg-whitelist=PyQt5")
        rm.view(source_file)
    else:
        print("## The provided predicate is not supported yet")
        print("## Please provide appropriate parameters")

elif arg_count == 3:
    if sys.argv[0] == "acupoint.py" and sys.argv[1].lower() == "purify":
        if sys.argv[2].lower().endswith(".py"):
            # Add startup code
            words_text = sys.argv[2]
            source_file = words_text
            rm.replace(source_file)
            rm.append(source_file)
            rm.view(source_file)

        else:
            if "_" in sys.argv[2]:
                words = sys.argv[2].split("_")
                words_text = "".join([word.title() for word in words])
            else:
                words_text = sys.argv[2].title()
            # Create entry class
            words_text = remove_symbols(words_text)
            entry_class = words_text
            source_file = "{}.py".format(entry_class)
            rm.entry(source_file, entry_class)
            rm.view(source_file)
    else:
        print("## The provided predicate is not supported yet")
        print("## Please provide appropriate parameters")

else:
    print("Please use this command set as follows")
    print("-"*48)
    print("# python acupoint.py purify test_widget.py")
    print("# python acupoint.py purify test_widget")
    print("# python acupoint.py purify")
    print("# python acupoint.py")
