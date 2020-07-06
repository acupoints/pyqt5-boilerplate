class SrcManager():
    def view(self, source_file, encoding="utf-8"):
        "# gullies"
        data = self.read(source_file, encoding=encoding)

        for data_el_index in range(len(data)):
            data_el = data[data_el_index]
            print("--{}-- {}".format(str(data_el_index).rjust(4,'0'), data_el))
        return data

    def read(self, source_file, encoding="utf-8"):
        "# gullies"
        import os
        data = []
        if os.path.exists(source_file):
            with open(source_file, 'r', encoding=encoding) as f:
                data = f.read().splitlines()
            
        return data

    def write(self, source_file, contents, encoding="utf-8"):
        "# gullies"
        with open(source_file, 'w', encoding=encoding) as f:
            f.writelines(contents)

    def append(self, source_file, contents="__main__", encoding="utf-8"):
        "# gullies"
        import re
        new_data = []
        raw_data = self.read(source_file, encoding=encoding)
        class_name = "Ui_Form"
        for raw_data_el in raw_data:
            if re.findall("\s*def setupUi\(self, (.+?)\):", raw_data_el):
                class_name = re.findall("\s*def setupUi\(self, (.+?)\):", raw_data_el)[0]
                break
        for raw_data_el_index in range(len(raw_data)):
            raw_data_el = raw_data[raw_data_el_index]
            if re.findall('if __name__ == "__main__":', raw_data_el):
                raw_data=raw_data[0:raw_data_el_index-2]
                break
        new_data = new_data + raw_data
        if contents == "__main__":
            new_data.append("""\nif __name__ == "__main__":
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    import sys
    app = QApplication(sys.argv)
    {0} = Ui_{1}()
    {0}.show()
    sys.exit(app.exec_())
    # pass""".format(class_name.lower(), class_name))
        else:
            new_data.append(contents)
        self.write(source_file, "\n".join(new_data), encoding=encoding)

    def replace(self, source_file, contents="(object):", encoding="utf-8"):
        "# gullies"
        import re
        new_data = []
        raw_data = self.read(source_file, encoding=encoding)
        class_name = "Ui_Form"
        for raw_data_el in raw_data:
            if re.findall("\s*def setupUi\(self, (.+?)\):", raw_data_el):
                class_name = re.findall("\s*def setupUi\(self, (.+?)\):", raw_data_el)[0]
                break
        for raw_data_el_index in range(len(raw_data)):
            raw_data_el = raw_data[raw_data_el_index]
            if re.findall('class (.+?)\(object\):', raw_data_el):
                if contents == "(object):":
                    raw_data[raw_data_el_index]="""class Ui_{}(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)\n""".format(class_name)
                else:
                    raw_data[raw_data_el_index]=contents
                break
        new_data = new_data + raw_data

        self.write(source_file, "\n".join(new_data), encoding=encoding)

    def entry(self, source_file, contents="App", encoding="utf-8"):
        "# gullies"
        import re
        base_class = "QWidget"
        if contents.startswith("Qfr"):
            base_class = "QMainWindow"
        # Create a template file
        new_data = []
        raw_data = []
        if contents.title() == "App":
            contents = "MainWindow"
        class_name = contents
        raw_data.append("""from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Ui_{1}({2}):
    # Custom signal with a str type parameter
    packed_signal_btn_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        print("## Welcome to PyQt5")
        # Component initialization
        self.initUI()

    def initUI(self):
        self.setWindowTitle('{1}')
        self.resize(320, 180)
        
        btn = QPushButton('{1}-Close', self)
        # Bind multiple slot functions
        btn.clicked.connect(self.slotfunc_btn_clicked)
        self.packed_signal_btn_clicked.connect(self.slotfunc_btn_close)

    def slotfunc_btn_clicked(self):
        msg="## Thanks for trial"
        self.packed_signal_btn_clicked.emit(msg)
    
    def slotfunc_btn_close(self, msg):
        print(msg)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    {0} = Ui_{1}()
    {0}.show()
    sys.exit(app.exec_())
    # pass""".format(class_name.lower(), class_name, base_class))
        new_data = new_data + raw_data

        self.write(source_file, "\n".join(new_data), encoding=encoding)

if __name__ == "__main__":
    rm = SrcManager()
    # Create entry class
    entry_class = "MainFrame"
    source_file = "{}.py".format(entry_class)
    rm.entry(source_file, entry_class)
    rm.view(source_file)
    # Add a whitelist of class name prompts
    # source_file = ".pylintrc"
    # rm.write(source_file, "extension-pkg-whitelist=PyQt5")
    # rm.view(source_file)

    # Add startup code
    # source_file = "Ui_MyTest.py"
    # rm.replace(source_file)
    # rm.append(source_file)
    # rm.view(source_file)
    pass