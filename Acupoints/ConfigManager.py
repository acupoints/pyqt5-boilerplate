class ConfigManager():
    def view(self, json_filename, encoding="utf-8"):
        "# gullies"
        data_dict = self.read(json_filename, encoding=encoding)

        print("--{}-- \n{}".format(data_dict.get('version'), data_dict))
        return data_dict

    def read(self, json_filename, encoding="utf-8"):
        "# gullies"
        import json
        import os

        data = []
        if os.path.exists(json_filename):
            with open(json_filename, 'r', encoding=encoding) as f:
                data = f.read().splitlines()
            
        data_dict = json.loads('\n'.join(data))
        return data_dict

    def write(self, json_filename, data_dict, encoding="utf-8"):
        "# gullies"
        import json
        with open(json_filename, 'w', encoding=encoding) as f:
            json.dump(data_dict, f, sort_keys=False, ensure_ascii=False)

    def get_all_files(self, folder_path, extensions=[], prefix_list=[], suffix_list=[]):
        "# gullies"
        import os
        extensions=[item.lower() for item in extensions]
        
        satisfied_files = []
        for path, dir, filelist in os.walk(folder_path):
            for filename in filelist:
                fn_base = os.path.splitext(filename)[0]
                fn_ext = os.path.splitext(filename)[1]

                satisfied = False

                if extensions:
                    if fn_ext.lower() in extensions:
                        satisfied = True
                    # pass
                elif prefix_list:
                    for prefix_list_el in prefix_list:
                        if fn_base.startswith(prefix_list_el):
                            satisfied = True
                            break
                    # pass
                elif suffix_list:
                    for suffix_list_el in suffix_list:
                        if fn_base.endswith(suffix_list_el):
                            satisfied = True
                            break
                    # pass
                else:
                    satisfied = True
                    # pass
                
                if satisfied:
                    satisfied_files.append((filename,fn_base,fn_ext,os.path.abspath(filename)))
                
        return satisfied_files
        
if __name__ == "__main__":
    configMan = ConfigManager()
    
    # Get configuration information from a file
    # json_filename = "demo.json"
    # json_dict = configMan.read(json_filename)
    # configMan.view(json_filename)

    # Write configuration information to a file
    # json_filename = "demo2.json"
    # json_dict['version']="Version 0.1"
    # json_dict['age']=json_dict['age']+12
    # configMan.write(json_filename,json_dict)
    # configMan.view(json_filename)

    # Iterate through all files in the folder
    # folder_path = "."
    # all_files = configMan.get_all_files(folder_path, extensions=['.json'])
    # print("count: {}".format(len(all_files)))
    # for all_files_el in all_files:
    #     print(all_files_el)
    
    # pass